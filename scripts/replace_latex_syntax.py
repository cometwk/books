import json
import os
import sys

def replace_latex_syntax_in_ipynb(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        notebook = json.load(file)
    
    # 定义替换规则
    replacements = {
        '\\(': '$',
        '\\)': '$',
        '\\[': '$$',
        '\\]': '$$'
    }
    
    # 遍历所有单元格
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            for i, line in enumerate(cell['source']):
                for old, new in replacements.items():
                    if old in line:
                        cell['source'][i] = line.replace(old, new)

    # 保存修改后的文件
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(notebook, file, indent=2, ensure_ascii=False)

def replace_latex_syntax_in_md(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 定义替换规则
    replacements = {
        '\\(': '$',
        '\\)': '$',
        '\\[': '$$',
        '\\]': '$$'
    }
    
    # 替换内容
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # 保存修改后的文件
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def replace_latex_syntax(filename):
    _, ext = os.path.splitext(filename)
    if ext == '.ipynb':
        replace_latex_syntax_in_ipynb(filename)
    elif ext == '.md':
        replace_latex_syntax_in_md(filename)
    else:
        print(f"Unsupported file type: {ext}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replace_latex_syntax.py <filename>")
    else:
        filename = sys.argv[1]
        replace_latex_syntax(filename)
