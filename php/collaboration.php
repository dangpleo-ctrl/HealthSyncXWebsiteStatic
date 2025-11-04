<?php
/**
 * Collaboration Form Handler
 * Processes partnership inquiry submissions with hCaptcha validation and PHPMailer
 * 
 * SECURITY: Config file loaded from OUTSIDE web root
 */

// Security: Prevent direct access
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    die(json_encode(['success' => false, 'error' => 'Method not allowed']));
}

// Load configuration from outside web root
// Path explanation: dirname(__DIR__, 2) goes from /public_html/php/ to /home/username/
define('HEALTHSYNCX_CONFIG', true);
$config_path = dirname(__DIR__, 2) . '/config/config.php';

if (!file_exists($config_path)) {
    error_log('Configuration file not found: ' . $config_path);
    http_response_code(500);
    die(json_encode(['success' => false, 'error' => 'Server configuration error. Please contact support.']));
}

require_once $config_path;

// Load Composer autoloader for PHPMailer
require_once dirname(__DIR__) . '/vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Set JSON response header
header('Content-Type: application/json');

// Parse JSON request body
$json = file_get_contents('php://input');
$data = json_decode($json, true);

if (!$data) {
    http_response_code(400);
    die(json_encode(['success' => false, 'error' => 'Invalid request data']));
}

// Validate required fields
$required_fields = ['name', 'email', 'organization', 'phone', 'partnerType', 'description'];
foreach ($required_fields as $field) {
    if (empty($data[$field])) {
        http_response_code(400);
        die(json_encode(['success' => false, 'error' => ucfirst($field) . ' is required']));
    }
}

// Validate email format
if (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    die(json_encode(['success' => false, 'error' => 'Invalid email address']));
}

// Verify hCaptcha if enabled
if (ENABLE_HCAPTCHA) {
    if (empty($data['hcaptchaToken'])) {
        http_response_code(400);
        die(json_encode(['success' => false, 'error' => 'Captcha verification required']));
    }

    $verify_url = 'https://hcaptcha.com/siteverify';
    $verify_data = [
        'secret' => HCAPTCHA_SECRET,
        'response' => $data['hcaptchaToken'],
        'remoteip' => $_SERVER['REMOTE_ADDR']
    ];

    $options = [
        'http' => [
            'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
            'method'  => 'POST',
            'content' => http_build_query($verify_data)
        ]
    ];

    $context  = stream_context_create($options);
    $result = @file_get_contents($verify_url, false, $context);
    
    if ($result === false) {
        error_log('hCaptcha verification failed: Unable to connect');
        http_response_code(500);
        die(json_encode(['success' => false, 'error' => 'Captcha verification failed']));
    }

    $response = json_decode($result);
    if (!$response->success) {
        http_response_code(400);
        die(json_encode(['success' => false, 'error' => 'Captcha verification failed']));
    }
}

// Sanitize inputs
$name = htmlspecialchars(strip_tags($data['name']));
$email = filter_var($data['email'], FILTER_SANITIZE_EMAIL);
$organization = htmlspecialchars(strip_tags($data['organization']));
$phone = htmlspecialchars(strip_tags($data['phone']));
$website = !empty($data['website']) ? filter_var($data['website'], FILTER_SANITIZE_URL) : 'Not provided';
$partnerType = htmlspecialchars(strip_tags($data['partnerType']));
$description = htmlspecialchars(strip_tags($data['description']));
$language = !empty($data['language']) ? $data['language'] : 'en';

// Partnership type labels
$partnershipLabels = [
    'technology' => ['en' => 'Technology Partner', 'vi' => 'Đối tác Công nghệ'],
    'healthcare' => ['en' => 'Healthcare Organization', 'vi' => 'Tổ chức Y tế'],
    'research' => ['en' => 'Research/Academic', 'vi' => 'Nghiên cứu/Học thuật'],
    'other' => ['en' => 'Other', 'vi' => 'Khác']
];

$partnershipLabel = isset($partnershipLabels[$partnerType]) 
    ? $partnershipLabels[$partnerType][$language]
    : $partnerType;

// Email subject and body based on language
if ($language === 'vi') {
    $subject = '[HealthSyncX] Yêu cầu Đối tác từ ' . $organization;
    $htmlBody = '
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
            .container { max-width: 600px; margin: 0 auto; padding: 20px; }
            .header { background: linear-gradient(135deg, #F97316 0%, #14B8A6 100%); color: white; padding: 30px; text-align: center; border-radius: 8px 8px 0 0; }
            .content { background: #f9fafb; padding: 30px; border-radius: 0 0 8px 8px; }
            .field { margin-bottom: 20px; }
            .label { font-weight: bold; color: #F97316; margin-bottom: 5px; }
            .value { padding: 10px; background: white; border-left: 3px solid #14B8A6; margin-top: 5px; }
            .badge { display: inline-block; padding: 4px 12px; background: #F97316; color: white; border-radius: 4px; font-size: 12px; }
            .footer { text-align: center; margin-top: 30px; color: #6b7280; font-size: 12px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>HealthSyncX</h1>
                <p>Yêu cầu Đối tác Mới</p>
            </div>
            <div class="content">
                <div class="field">
                    <div class="label">Loại Đối tác:</div>
                    <div class="value"><span class="badge">' . $partnershipLabel . '</span></div>
                </div>
                <div class="field">
                    <div class="label">Tên Tổ chức:</div>
                    <div class="value">' . $organization . '</div>
                </div>
                <div class="field">
                    <div class="label">Người liên hệ:</div>
                    <div class="value">' . $name . '</div>
                </div>
                <div class="field">
                    <div class="label">Email:</div>
                    <div class="value"><a href="mailto:' . $email . '">' . $email . '</a></div>
                </div>
                <div class="field">
                    <div class="label">Điện thoại:</div>
                    <div class="value">' . $phone . '</div>
                </div>
                <div class="field">
                    <div class="label">Website:</div>
                    <div class="value">' . $website . '</div>
                </div>
                <div class="field">
                    <div class="label">Mô tả:</div>
                    <div class="value">' . nl2br($description) . '</div>
                </div>
            </div>
            <div class="footer">
                <p>Email này được gửi từ biểu mẫu đối tác HealthSyncX</p>
            </div>
        </div>
    </body>
    </html>';
} else {
    $subject = '[HealthSyncX] Partnership Inquiry from ' . $organization;
    $htmlBody = '
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
            .container { max-width: 600px; margin: 0 auto; padding: 20px; }
            .header { background: linear-gradient(135deg, #F97316 0%, #14B8A6 100%); color: white; padding: 30px; text-align: center; border-radius: 8px 8px 0 0; }
            .content { background: #f9fafb; padding: 30px; border-radius: 0 0 8px 8px; }
            .field { margin-bottom: 20px; }
            .label { font-weight: bold; color: #F97316; margin-bottom: 5px; }
            .value { padding: 10px; background: white; border-left: 3px solid #14B8A6; margin-top: 5px; }
            .badge { display: inline-block; padding: 4px 12px; background: #F97316; color: white; border-radius: 4px; font-size: 12px; }
            .footer { text-align: center; margin-top: 30px; color: #6b7280; font-size: 12px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>HealthSyncX</h1>
                <p>New Partnership Inquiry</p>
            </div>
            <div class="content">
                <div class="field">
                    <div class="label">Partnership Type:</div>
                    <div class="value"><span class="badge">' . $partnershipLabel . '</span></div>
                </div>
                <div class="field">
                    <div class="label">Organization:</div>
                    <div class="value">' . $organization . '</div>
                </div>
                <div class="field">
                    <div class="label">Contact Person:</div>
                    <div class="value">' . $name . '</div>
                </div>
                <div class="field">
                    <div class="label">Email:</div>
                    <div class="value"><a href="mailto:' . $email . '">' . $email . '</a></div>
                </div>
                <div class="field">
                    <div class="label">Phone:</div>
                    <div class="value">' . $phone . '</div>
                </div>
                <div class="field">
                    <div class="label">Website:</div>
                    <div class="value">' . $website . '</div>
                </div>
                <div class="field">
                    <div class="label">Description:</div>
                    <div class="value">' . nl2br($description) . '</div>
                </div>
            </div>
            <div class="footer">
                <p>This email was sent from the HealthSyncX partnership form</p>
            </div>
        </div>
    </body>
    </html>';
}

// Plain text version
$textBody = "HealthSyncX - " . ($language === 'vi' ? 'Yêu cầu Đối tác Mới' : 'New Partnership Inquiry') . "\n\n";
$textBody .= ($language === 'vi' ? 'Loại Đối tác' : 'Partnership Type') . ": $partnershipLabel\n";
$textBody .= ($language === 'vi' ? 'Tổ chức' : 'Organization') . ": $organization\n";
$textBody .= ($language === 'vi' ? 'Người liên hệ' : 'Contact Person') . ": $name\n";
$textBody .= "Email: $email\n";
$textBody .= ($language === 'vi' ? 'Điện thoại' : 'Phone') . ": $phone\n";
$textBody .= "Website: $website\n\n";
$textBody .= ($language === 'vi' ? 'Mô tả' : 'Description') . ":\n$description";

// Send email using PHPMailer
try {
    $mail = new PHPMailer(true);
    
    // Server settings
    $mail->isSMTP();
    $mail->Host       = SMTP_HOST;
    $mail->SMTPAuth   = true;
    $mail->Username   = SMTP_USERNAME;
    $mail->Password   = SMTP_PASSWORD;
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;
    $mail->Port       = SMTP_PORT;
    $mail->CharSet    = 'UTF-8';
    
    // Recipients
    $mail->setFrom(SMTP_FROM_EMAIL, SMTP_FROM_NAME);
    $mail->addAddress(COLLABORATION_FORM_RECIPIENT);
    $mail->addReplyTo($email, $name);
    
    // Content
    $mail->isHTML(true);
    $mail->Subject = $subject;
    $mail->Body    = $htmlBody;
    $mail->AltBody = $textBody;
    
    $mail->send();
    
    http_response_code(200);
    echo json_encode([
        'success' => true, 
        'message' => $language === 'vi' 
            ? 'Cảm ơn bạn quan tâm đến hợp tác! Chúng tôi sẽ liên hệ sớm.'
            : 'Thank you for your interest in partnership! We will be in touch soon.'
    ]);
    
} catch (Exception $e) {
    error_log('PHPMailer Error: ' . $mail->ErrorInfo);
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Failed to send email. Please try again later.']);
}
?>
