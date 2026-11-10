#!/usr/bin/env python3
"""把仓库内容复制到 _site_src/ 当 MkDocs 的文档源（不复制 .git、.github、网站配置、缓存）。工作流和本地测试都用它。"""
import shutil, os
IGN = shutil.ignore_patterns('.git', '.github', '_site_src', 'site', 'mkdocs.yml', '__pycache__', '.gitignore')
shutil.rmtree('_site_src', ignore_errors=True)
shutil.copytree('.', '_site_src', ignore=IGN)
os.replace(os.path.join('_site_src', 'README.md'), os.path.join('_site_src', 'index.md'))
print('文档源已生成：_site_src/')
