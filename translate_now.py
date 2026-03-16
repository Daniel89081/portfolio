#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GERMAN HTML TRANSLATION SCRIPT
===============================
This script translates all English HTML pages to German versions.

USAGE: python3 translate_now.py
or:    python translate_now.py

The script will read all 11 English HTML files and create German versions
in the /de/ subdirectories with:
- lang="de" (instead of "en")
- Updated meta tags (/de/ paths)
- German translations
- og:locale updated

NO EXTERNAL DEPENDENCIES REQUIRED - Uses only Python standard library (os, re, sys)
"""

import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read_file(path):
    """Read a file with UTF-8 encoding"""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    """Write a file with UTF-8 encoding"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def translate_html(html, page_type='generic'):
    """Apply all translations to HTML content"""
    
    # 1. Change language attribute
    html = html.replace('<html lang="en">', '<html lang="de">')
    
    # 2. Fix author/name references
    html = html.replace('Jannis Alexander Dietrich', 'Daniel Noah Dietrich')
    html = html.replace('Jannis Dietrich', 'Daniel Dietrich')
    html = html.replace('jannisdietrich.com', 'danieldietrich.tech')
    
    # 3. Common UI text
    html = html.replace('&copy; 2026 Daniel Dietrich. All rights reserved', 
                        '&copy; 2026 Daniel Dietrich. Alle Rechte vorbehalten')
    html = html.replace('aria-label="Back to top of page"', 
                        'aria-label="Nach oben scrollen"')
    html = html.replace('>Back to top &uarr;<', '>Nach oben &uarr;<')
    html = html.replace('> Back to top <', '> Nach oben <')
    html = html.replace('> Terms <', '> Nutzungsbedingungen <')
    html = html.replace('> Privacy <', '> Datenschutz <')
    html = html.replace('>Source<', '>Quellcode<')
    html = html.replace('> Source Code </a>', '> Quellcode </a>')
    html = html.replace('> Live Demo </a>', '> Live-Demo </a>')
    
    # 4. Section headings
    html = html.replace('>About</h2>', '>Über mich</h2>')
    html = html.replace('>Education <svg', '>Ausbildung <svg')
    html = html.replace('> Education </h2>', '> Ausbildung </h2>')
    html = html.replace('>Education</h2>', '>Ausbildung</h2>')
    html = html.replace('>Tech Stack / Skills</h2>', '>Tech Stack / Fähigkeiten</h2>')
    html = html.replace('>Experience <svg', '>Berufserfahrung <svg')
    html = html.replace('> Experience </h2>', '> Berufserfahrung </h2>')
    html = html.replace('>Projects <svg', '>Projekte <svg')
    html = html.replace('> Projects </h2>', '> Projekte </h2>')
    html = html.replace('>Contact</h2>', '>Kontakt</h2>')
    html = html.replace('> Projects <', '> Projekte <')
    html = html.replace('> Work <', '> Arbeit <')
    
    # 5. Feature headings
    html = html.replace('<h2 id="features">Features</h2>', '<h2 id="funktionen">Funktionen</h2>')
    html = html.replace('<h2 id="what-i-learned">What I Learned</h2>', '<h2 id="was-ich-gelernt-habe">Was ich gelernt habe</h2>')
    html = html.replace('2 min read', '2 Min. Lesen')
    
    # 6. Work-related content
    html = html.replace('Built responsive web applications using React, Next.js, and TypeScript',
                        'Entwicklung responsiver Webanwendungen mit React, Next.js und TypeScript')
    html = html.replace('Developed cross-platform mobile apps with Flutter and Dart',
                        'Entwicklung plattformübergreifender mobiler Apps mit Flutter und Dart')
    html = html.replace('Integrated backends with Firebase, Supabase, and REST APIs',
                        'Integration von Backends mit Firebase, Supabase und REST-APIs')
    html = html.replace('Maintained clear communication with clients and delivered projects on time',
                        'Klare Kommunikation mit Kunden und pünktliche Projektlieferung')
    html = html.replace('Achieved top-rated status through consistent high-quality work',
                        'Top-Bewertung durch konstant hochwertige Arbeit erhalten')
    html = html.replace('Gained hands-on experience with AI/ML pipelines and natural language processing systems',
                        'Praktische Erfahrung mit KI/ML-Pipelines und Natural Language Processing')
    html = html.replace('Collaborated with cross-functional engineering teams in an agile environment',
                        'Zusammenarbeit mit interdisziplinären Entwicklungsteams in einem agilen Umfeld')
    html = html.replace('Assisted in testing and improving voice recognition features for in-car assistants',
                        'Mitarbeit beim Testen und Verbessern von Spracherkennungsfunktionen für Fahrzeugassistenten')
    html = html.replace('Developed internal tooling to streamline development workflows',
                        'Entwicklung interner Tools zur Optimierung von Entwicklungsabläufen')
    
    # 7. Project features
    feature_map = {
        'Real-time shared lists synced via Firebase across all devices': 'Geteilte Listen in Echtzeit via Firebase über alle Geräte synchronisiert',
        'Offline-first architecture — works without internet': 'Offline-first-Architektur – funktioniert ohne Internet',
        'Published on both App Store and Google Play': 'Im App Store und bei Google Play veröffentlicht',
        'Interactive Three.js 3D phone mockup with React Three Fiber': 'Interaktives Three.js-3D-Telefon-Mockup mit React Three Fiber',
        'Scroll-triggered reveal animations and responsive design': 'Scroll-gesteuerte Einblend-Animationen und responsives Design',
        'Lazy-loaded 3D assets with optimized bundle size': 'Lazy-geladene 3D-Assets mit optimierter Bundle-Größe',
        'Spaced repetition algorithm for effective flashcard review': 'Spaced-Repetition-Algorithmus für effektives Karteikarten-Lernen',
        'Pomodoro timer with session statistics and streaks': 'Pomodoro-Timer mit Sitzungsstatistiken und Streaks',
        'Real-time sync via Supabase with offline fallback': 'Echtzeit-Synchronisierung via Supabase mit Offline-Fallback',
        'Live preview editor with multiple professional templates': 'Live-Vorschau-Editor mit mehreren professionellen Vorlagen',
        'AI-powered suggestions for improving resume bullet points': 'KI-gestützte Vorschläge zur Verbesserung von Lebenslauf-Stichpunkten',
        'High-quality PDF export with proper formatting': 'Hochqualitatives PDF-Export mit korrekter Formatierung',
        'Conversational AI with per-channel context memory': 'Konversations-KI mit kanalbasiertem Kontextgedächtnis',
        'Text-to-image generation from prompts': 'Text-zu-Bild-Generierung aus Eingaben',
        'Modular plugin architecture for adding new AI capabilities': 'Modulare Plugin-Architektur zum Hinzufügen neuer KI-Fähigkeiten',
        'XP-based leveling system with role rewards and leaderboards': 'XP-basiertes Leveling-System mit Rollen-Belohnungen und Bestenlisten',
        'Full moderation suite with audit logging': 'Vollständiges Moderations-Paket mit Audit-Logging',
        'Runs 24/7 on Linux VPS with automatic restarts': 'Läuft rund um die Uhr auf einem Linux-VPS mit automatischen Neustarts',
    }
    for en, de in feature_map.items():
        html = html.replace(en, de)
    
    # 8. Project descriptions
    desc_map = {
        'A cross-platform mobile app for collaborative grocery shopping with real-time sync, smart categories, and offline support. Published on iOS and Android.':
        'Eine plattformübergreifende mobile App für gemeinsames Einkaufen mit Echtzeit-Synchronisierung, smarten Kategorien und Offline-Unterstützung. Verfügbar auf iOS und Android.',
        'A modern marketing website for the Shoply app featuring interactive 3D phone mockups, smooth scroll animations, and optimized performance.':
        'Eine moderne Marketing-Website für die Shoply-App mit interaktiven 3D-Telefon-Mockups, sanften Scroll-Animationen und optimierter Performance.',
        'A mobile learning companion built with React Native and Expo — featuring spaced repetition flashcards, study planning, and progress tracking.':
        'Ein mobiler Lernbegleiter mit React Native und Expo – mit Spaced-Repetition-Karteikarten, Lernplanung und Fortschrittsverfolgung.',
        'A web application that helps users create professional resumes with customizable templates, live preview editing, and AI-powered bullet point suggestions.':
        'Eine Webanwendung, die Nutzern hilft, professionelle Lebensläufe mit anpassbaren Vorlagen, Live-Vorschau und KI-gestützten Verbesserungsvorschlägen zu erstellen.',
        'An AI-powered Discord bot bringing language models and image generation to servers — with context memory, rate limiting, and a modular plugin system.':
        'Ein KI-gesteuerter Discord-Bot, der Sprachmodelle und Bildgenerierung in Server bringt – mit Kontextgedächtnis, Rate-Limiting und modularem Plugin-System.',
        'A feature-rich Discord bot for server management and entertainment — with moderation tools, XP leveling, music playback, and custom commands.':
        'Ein funktionsreicher Discord-Bot für Server-Verwaltung und Unterhaltung – mit Moderations-Tools, XP-Leveling, Musikwiedergabe und benutzerdefinierten Befehlen.',
    }
    for en, de in desc_map.items():
        html = html.replace(en, de)
    
    # 9. Internal links - update body links to use /de/ paths
    body_start = html.find('<body>')
    if body_start > -1:
        head = html[:body_start]
        body = html[body_start:]
        
        link_replacements = [
            ('href="/legal/privacy/"', 'href="/de/legal/privacy/"'),
            ('href="/legal/terms/"', 'href="/de/legal/terms/"'),
            ('href="/projects/resumeme/"', 'href="/de/projects/resumeme/"'),
            ('href="/projects/tharos-discord-bot/"', 'href="/de/projects/tharos-discord-bot/"'),
            ('href="/projects/freeai-discord-bot/"', 'href="/de/projects/freeai-discord-bot/"'),
            ('href="/projects/shoply-landing-page/"', 'href="/de/projects/shoply-landing-page/"'),
            ('href="/projects/shoply-app/"', 'href="/de/projects/shoply-app/"'),
            ('href="/projects/studyapp/"', 'href="/de/projects/studyapp/"'),
            ('href="/projects/"', 'href="/de/projects/"'),
            ('href="/work/"', 'href="/de/work/"'),
        ]
        for old, new in link_replacements:
            body = body.replace(old, new)
        
        html = head + body
    
    return html

def process_file(en_path, de_path, de_url):
    """Process a single English HTML file and create German version"""
    try:
        html = read_file(en_path)
        html = translate_html(html)
        
        # Update meta URLs
        html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{de_url}">', html)
        html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{de_url}">', html)
        html = re.sub(r'<meta name="twitter:url" content="[^"]*">', f'<meta name="twitter:url" content="{de_url}">', html)
        
        # Swap locales
        html = html.replace(
            'content="en_US"><meta property="og:locale:alternate" content="de_DE"',
            'content="de_DE"><meta property="og:locale:alternate" content="en_US"'
        )
        
        # Write output
        write_file(de_path, html)
        print(f"✓ Created: {de_path}")
        return True
    except Exception as e:
        print(f"✗ Error processing {en_path}: {e}")
        return False

def main():
    """Main execution"""
    print("\n" + "="*70)
    print("German HTML Translation")
    print("="*70 + "\n")
    
    success_count = 0
    
    # Process all 11 files
    files = [
        ('index.html', 'de/index.html', 'https://danieldietrich.tech/de/'),
        ('work/index.html', 'de/work/index.html', 'https://danieldietrich.tech/de/work/'),
        ('projects/index.html', 'de/projects/index.html', 'https://danieldietrich.tech/de/projects/'),
        ('projects/resumeme/index.html', 'de/projects/resumeme/index.html', 'https://danieldietrich.tech/de/projects/resumeme/'),
        ('projects/tharos-discord-bot/index.html', 'de/projects/tharos-discord-bot/index.html', 'https://danieldietrich.tech/de/projects/tharos-discord-bot/'),
        ('projects/freeai-discord-bot/index.html', 'de/projects/freeai-discord-bot/index.html', 'https://danieldietrich.tech/de/projects/freeai-discord-bot/'),
        ('projects/shoply-landing-page/index.html', 'de/projects/shoply-landing-page/index.html', 'https://danieldietrich.tech/de/projects/shoply-landing-page/'),
        ('projects/shoply-app/index.html', 'de/projects/shoply-app/index.html', 'https://danieldietrich.tech/de/projects/shoply-app/'),
        ('projects/studyapp/index.html', 'de/projects/studyapp/index.html', 'https://danieldietrich.tech/de/projects/studyapp/'),
        ('legal/privacy/index.html', 'de/legal/privacy/index.html', 'https://danieldietrich.tech/de/legal/privacy/'),
        ('legal/terms/index.html', 'de/legal/terms/index.html', 'https://danieldietrich.tech/de/legal/terms/'),
    ]
    
    for en_path, de_path, de_url in files:
        en_full = os.path.join(BASE_DIR, en_path)
        de_full = os.path.join(BASE_DIR, de_path)
        if process_file(en_full, de_full, de_url):
            success_count += 1
    
    print("\n" + "="*70)
    print(f"Translation Complete: {success_count}/11 files translated")
    print("="*70 + "\n")
    
    return 0 if success_count == 11 else 1

if __name__ == '__main__':
    sys.exit(main())
