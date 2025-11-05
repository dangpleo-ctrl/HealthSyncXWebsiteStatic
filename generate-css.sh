#!/bin/bash
# Scan all PHP files and generate complete Tailwind CSS
find . -name "*.php" -type f | xargs cat | grep -o 'class="[^"]*"' | sed 's/class="//g' | sed 's/"//g' | tr ' ' '\n' | sort -u > /tmp/classes.txt
npx tailwindcss -i tailwind-input.css -o assets/css/styles.css --minify
