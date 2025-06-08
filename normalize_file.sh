#!/bin/bash

for file in "$@"; do
  # Remove UTF-8 BOM (using octal escape for compatibility)
  sed -i '' $'1s/\xEF\xBB\xBF//' "$file"  # [1][2]

  # Convert line endings to LF
  dos2unix "$file"  # [5]

  # Remove trailing whitespace
  sed -i '' 's/[[:space:]]\+$//' "$file"  # [1][6]

  echo "Normalized: $file"
done
