#!/usr/bin/env python3
"""Minimal translator - read and transform files directly"""
import os

def main():
    base = r'c:\Users\Fo\Documents\danieldietrich.tech'
    os.chdir(base)
    
    # Read English index
    with open(os.path.join(base, 'index.html'), 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Apply critical transformations
    transformations = [
        ('<html lang="en">', '<html lang="de">'),
        ('https://danieldietrich.tech/">', 'https://danieldietrich.tech/de/">'),
        ('canonical" href="https://danieldietrich.tech/"', 'canonical" href="https://danieldietrich.tech/de/"'),
        ('<meta property="og:url" content="https://danieldietrich.tech/">', 
         '<meta property="og:url" content="https://danieldietrich.tech/de/">'),
        ('<meta name="twitter:url" content="https://danieldietrich.tech/">', 
         '<meta name="twitter:url" content="https://danieldietrich.tech/de/">'),
        ('og:locale" content="en_US"><meta property="og:locale:alternate" content="de_DE"',
         'og:locale" content="de_DE"><meta property="og:locale:alternate" content="en_US"'),
    ]
    
    for old, new in transformations:
        html = html.replace(old, new)
    
    # Write output
    os.makedirs(os.path.join(base, 'de'), exist_ok=True)
    with open(os.path.join(base, 'de', 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✅ Created /de/index.html")

if __name__ == '__main__':
    main()
