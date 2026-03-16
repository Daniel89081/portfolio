#!/usr/bin/env python3
"""
Translator helper module - can be called directly.
This file can be executed with: python -m translate_helper
"""

if __name__ == '__main__':
    import os
    import re
    import sys
    
    BASE = r'c:\Users\Fo\Documents\danieldietrich.tech'
    os.chdir(BASE)
    
    # Import and execute the translation
    exec(open(os.path.join(BASE, 'translate_all.py')).read())
