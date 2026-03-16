#!/usr/bin/env python3
"""Execute the translation directly"""
import os
import sys

os.chdir(r'c:\Users\Fo\Documents\danieldietrich.tech')
sys.path.insert(0, r'c:\Users\Fo\Documents\danieldietrich.tech')

# Execute the translation script
with open('translate_de.py', 'r', encoding='utf-8') as f:
    code = f.read()
    exec(code)
