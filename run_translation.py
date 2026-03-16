#!/usr/bin/env python3
"""
Standalone script to execute the German HTML translation.
This script directly executes the translation logic from translate_de.py.
"""
import os
import re

BASE = r'c:\Users\Fo\Documents\danieldietrich.tech'

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def replace_meta_urls(html, de_url):
    """Update canonical, og:url, twitter:url to DE version."""
    html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{de_url}">', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{de_url}">', html)
    html = re.sub(r'<meta name="twitter:url" content="[^"]*">', f'<meta name="twitter:url" content="{de_url}">', html)
    return html

def replace_locale(html):
    """Swap og:locale and og:locale:alternate."""
    html = html.replace('content="en_US"><meta property="og:locale:alternate" content="de_DE"',
                        'content="de_DE"><meta property="og:locale:alternate" content="en_US"')
    return html

def update_body_links(html):
    """Replace internal body links with /de/ prefixed versions."""
    body_start = html.find('<body>')
    if body_start == -1:
        body_start = 0
    head = html[:body_start]
    body = html[body_start:]

    # Order matters: most specific first
    link_maps = [
        ('href="/legal/privacy/"', 'href="/de/legal/privacy/"'),
        ('href="/legal/terms/"', 'href="/de/legal/terms/"'),
        ('href="/legal/privacy"', 'href="/de/legal/privacy/"'),
        ('href="/legal/terms"', 'href="/de/legal/terms/"'),
        ('href="/projects/resumeme/"', 'href="/de/projects/resumeme/"'),
        ('href="/projects/resumeme"', 'href="/de/projects/resumeme/"'),
        ('href="/projects/tharos-discord-bot/"', 'href="/de/projects/tharos-discord-bot/"'),
        ('href="/projects/tharos-discord-bot"', 'href="/de/projects/tharos-discord-bot/"'),
        ('href="/projects/freeai-discord-bot/"', 'href="/de/projects/freeai-discord-bot/"'),
        ('href="/projects/freeai-discord-bot"', 'href="/de/projects/freeai-discord-bot/"'),
        ('href="/projects/shoply-landing-page/"', 'href="/de/projects/shoply-landing-page/"'),
        ('href="/projects/shoply-landing-page"', 'href="/de/projects/shoply-landing-page/"'),
        ('href="/projects/shoply-app/"', 'href="/de/projects/shoply-app/"'),
        ('href="/projects/shoply-app"', 'href="/de/projects/shoply-app/"'),
        ('href="/projects/studyapp/"', 'href="/de/projects/studyapp/"'),
        ('href="/projects/studyapp"', 'href="/de/projects/studyapp/"'),
        ('href="/projects/"', 'href="/de/projects/"'),
        ('href="/projects"', 'href="/de/projects/"'),
        ('href="/work/"', 'href="/de/work/"'),
        ('href="/work"', 'href="/de/work/"'),
    ]
    for old, new in link_maps:
        body = body.replace(old, new)

    return head + body

print("Starting German HTML translation...")
print(f"Base directory: {BASE}")

# Import and run the actual translation module
try:
    import sys
    sys.path.insert(0, BASE)
    exec(open(os.path.join(BASE, 'translate_de.py')).read())
    print("\n✅ Translation completed successfully!")
except Exception as e:
    print(f"\n❌ Error during translation: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
