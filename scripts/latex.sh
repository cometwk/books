#!/bin/bash

# 检查是否提供了文件名或目录名
if [ -z "$1" ]; then
    echo "Usage: ./run_replace_latex_syntax.sh <file_or_directory>"
    exit 1
fi

# 获取输入的文件或目录
input="$1"

# 处理目录的情况
if [ -d "$input" ]; then
    echo "Processing directory: $input"
    # 遍历目录及其子目录中的所有 .ipynb 和 .md 文件
    find "$input" -type f \( -name "*.ipynb" -o -name "*.md" \) | while read -r file; do
        echo "Processing file: $file"
        python ./scripts/replace_latex_syntax.py "$file"
    done
elif [ -f "$input" ]; then
    # 处理单个文件的情况
    echo "Processing file: $input"
    python ./scripts/replace_latex_syntax.py "$input"
else
    echo "Error: $input is not a valid file or directory"
    exit 1
fi

echo "Processing complete."
