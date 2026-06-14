#!/bin/bash

# Image optimization script for WebP conversion using cwebp (as specified in issue #31)
# Run in WSL Ubuntu or compatible Linux after `sudo apt install webp` (or equivalent binary in PATH)
# Creates optimized/ subdir with .webp versions (quality 80 default)

# Create output directory
mkdir -p assets/img/optimized

# Counter for stats
echo "Starting WebP conversion using cwebp..."
count=0
total_size_before=0
total_size_after=0

for img in assets/img/*.{jpg,jpeg,png,JPG,JPEG,PNG}; do
  if [ -f "$img" ]; then
    filename=$(basename "$img")
    name="${filename%.*}"
    
    # Get original size
    orig_size=$(stat -c%s "$img" 2>/dev/null || echo 0)
    total_size_before=$((total_size_before + orig_size))
    
    # Convert to WebP with quality 80 (good balance of size/quality). 
    # For hero images use slightly higher if needed, but batch 80 here.
    cwebp -q 80 "$img" -o "assets/img/optimized/${name}.webp" -quiet
    
    webp_file="assets/img/optimized/${name}.webp"
    if [ -f "$webp_file" ]; then
      webp_size=$(stat -c%s "$webp_file")
      total_size_after=$((total_size_after + webp_size))
      savings=$((100 - (webp_size * 100 / orig_size)))
      echo "Converted: $filename -> ${name}.webp (${savings}% smaller, $orig_size -> $webp_size bytes)"
      ((count++))
    else
      echo "Failed to convert: $filename"
    fi
  fi
done

echo ""
echo "Conversion complete! Converted $count images."
echo "Total original size: $((total_size_before / 1024)) KB"
echo "Total WebP size:    $((total_size_after / 1024)) KB"
if [ $total_size_before -gt 0 ]; then
  overall=$((100 - (total_size_after * 100 / total_size_before)))
  echo "Overall savings: ~${overall}%"
fi
echo "Optimized files are in assets/img/optimized/"
echo "Next: Review files (compare visually), move/adjust as needed, update HTML references (use <picture> for fallback), then commit."
echo ""
echo "To use cwebp directly: cwebp -q 80 input.jpg -o output.webp"
