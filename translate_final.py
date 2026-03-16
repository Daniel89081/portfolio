#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
German HTML Translation - Standalone Execution Script
This script processes ALL English HTML files and creates German translations.

Usage: python translate_final.py
"""

import os
import re
import sys

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

print(f"\n{'='*70}")
print("🌐 German HTML Translation - Processing All Files")
print(f"{'='*70}")
print(f"📂 Working Directory: {BASE_DIR}\n")

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def read_file(path):
    """Read file with UTF-8 encoding"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Failed to read {path}: {e}")
        return None

def write_file(path, content):
    """Write file with UTF-8 encoding and create directories"""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"❌ Failed to write {path}: {e}")
        return False

def replace_meta_urls(html, de_url):
    """Update canonical, og:url, twitter:url meta tags"""
    html = re.sub(r'<link rel="canonical" href="[^"]*">', 
                  f'<link rel="canonical" href="{de_url}">', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', 
                  f'<meta property="og:url" content="{de_url}">', html)
    html = re.sub(r'<meta name="twitter:url" content="[^"]*">', 
                  f'<meta name="twitter:url" content="{de_url}">', html)
    return html

def replace_locale(html):
    """Swap og:locale from en_US to de_DE"""
    html = html.replace(
        'content="en_US"><meta property="og:locale:alternate" content="de_DE"',
        'content="de_DE"><meta property="og:locale:alternate" content="en_US"'
    )
    return html

def update_body_links(html):
    """Replace internal body links to use /de/ paths"""
    body_start = html.find('<body>')
    if body_start == -1:
        body_start = 0
    head = html[:body_start]
    body = html[body_start:]
    
    # Most specific patterns first
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

def translate_text(html):
    """Apply all text translations"""
    # Footer
    html = html.replace('&copy; 2026 Daniel Dietrich. All rights reserved', 
                        '&copy; 2026 Daniel Dietrich. Alle Rechte vorbehalten')
    html = html.replace('&copy; 2026 Jannis Dietrich. All rights reserved', 
                        '&copy; 2026 Daniel Dietrich. Alle Rechte vorbehalten')
    
    # Language/Author fixes
    html = html.replace('Jannis Alexander Dietrich', 'Daniel Noah Dietrich')
    html = html.replace('Jannis Dietrich', 'Daniel Dietrich')
    html = html.replace('jannisdietrich.com', 'danieldietrich.tech')
    html = html.replace('Jannis-', 'Daniel-')
    
    # Common UI elements
    html = html.replace('aria-label="Back to top of page"', 'aria-label="Nach oben scrollen"')
    html = html.replace('>Back to top &uarr;<', '>Nach oben &uarr;<')
    html = html.replace('> Back to top <', '> Nach oben <')
    html = html.replace('> Terms <', '> Nutzungsbedingungen <')
    html = html.replace('> Privacy <', '> Datenschutz <')
    html = html.replace('> Demo <', '> Demo <')
    html = html.replace('>Source<', '>Quellcode<')
    html = html.replace('> Source <', '> Quellcode <')
    html = html.replace('> Source Code </a>', '> Quellcode </a>')
    html = html.replace('> Live Demo </a>', '> Live-Demo </a>')
    html = html.replace('> Contact <', '> Kontakt <')
    html = html.replace('> Home <', '> Startseite <')
    
    # Common section headings
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
    
    # Headings and titles
    html = html.replace('<h2 id="features">Features</h2>', '<h2 id="funktionen">Funktionen</h2>')
    html = html.replace('<h2 id="what-i-learned">What I Learned</h2>', '<h2 id="was-ich-gelernt-habe">Was ich gelernt habe</h2>')
    html = html.replace('2 min read', '2 Min. Lesen')
    
    # Page titles
    html = html.replace('<title>Home | Daniel Dietrich </title>', '<title>Startseite | Daniel Dietrich</title>')
    html = html.replace('content="Home | Daniel Dietrich"', 'content="Startseite | Daniel Dietrich"')
    html = html.replace('title="Home | Daniel Dietrich"', 'title="Startseite | Daniel Dietrich"')
    html = re.sub(r'<title>Work \| [^<]*</title>', '<title>Arbeit | Daniel Dietrich</title>', html)
    html = re.sub(r'<title>Projects \| [^<]*</title>', '<title>Projekte | Daniel Dietrich</title>', html)
    html = re.sub(r'<title>Privacy Policy \| [^<]*</title>', '<title>Datenschutzerklärung | Daniel Dietrich</title>', html)
    html = re.sub(r'<title>Terms of Use \| [^<]*</title>', '<title>Nutzungsbedingungen | Daniel Dietrich</title>', html)
    
    # Breadcrumbs
    html = html.replace('"name":"Home"', '"name":"Startseite"')
    html = html.replace('"name":"Work"', '"name":"Arbeit"')
    html = html.replace('"name":"Projects"', '"name":"Projekte"')
    html = html.replace('"name":"Privacy Policy"', '"name":"Datenschutzerklärung"')
    html = html.replace('"name":"Terms of Use"', '"name":"Nutzungsbedingungen"')
    
    # Work/Experience content
    work_items = [
        ('Built responsive web applications using React, Next.js, and TypeScript',
         'Entwicklung responsiver Webanwendungen mit React, Next.js und TypeScript'),
        ('Developed cross-platform mobile apps with Flutter and Dart',
         'Entwicklung plattformübergreifender mobiler Apps mit Flutter und Dart'),
        ('Integrated backends with Firebase, Supabase, and REST APIs',
         'Integration von Backends mit Firebase, Supabase und REST-APIs'),
        ('Maintained clear communication with clients and delivered projects on time',
         'Klare Kommunikation mit Kunden und pünktliche Projektlieferung'),
        ('Achieved top-rated status through consistent high-quality work',
         'Top-Bewertung durch konstant hochwertige Arbeit erhalten'),
        ('Gained hands-on experience with AI/ML pipelines and natural language processing systems',
         'Praktische Erfahrung mit KI/ML-Pipelines und Natural Language Processing'),
        ('Collaborated with cross-functional engineering teams in an agile environment',
         'Zusammenarbeit mit interdisziplinären Entwicklungsteams in einem agilen Umfeld'),
        ('Assisted in testing and improving voice recognition features for in-car assistants',
         'Mitarbeit beim Testen und Verbessern von Spracherkennungsfunktionen für Fahrzeugassistenten'),
        ('Developed internal tooling to streamline development workflows',
         'Entwicklung interner Tools zur Optimierung von Entwicklungsabläufen'),
    ]
    
    for en, de in work_items:
        html = html.replace(f'<li>{en}</li>', f'<li>{de}</li>')
    
    # Project features
    features = [
        ('Real-time shared lists synced via Firebase across all devices',
         'Geteilte Listen in Echtzeit via Firebase über alle Geräte synchronisiert'),
        ('Offline-first architecture — works without internet',
         'Offline-first-Architektur – funktioniert ohne Internet'),
        ('Published on both App Store and Google Play',
         'Im App Store und bei Google Play veröffentlicht'),
        ('Interactive Three.js 3D phone mockup with React Three Fiber',
         'Interaktives Three.js-3D-Telefon-Mockup mit React Three Fiber'),
        ('Scroll-triggered reveal animations and responsive design',
         'Scroll-gesteuerte Einblend-Animationen und responsives Design'),
        ('Lazy-loaded 3D assets with optimized bundle size',
         'Lazy-geladene 3D-Assets mit optimierter Bundle-Größe'),
        ('Spaced repetition algorithm for effective flashcard review',
         'Spaced-Repetition-Algorithmus für effektives Karteikarten-Lernen'),
        ('Pomodoro timer with session statistics and streaks',
         'Pomodoro-Timer mit Sitzungsstatistiken und Streaks'),
        ('Real-time sync via Supabase with offline fallback',
         'Echtzeit-Synchronisierung via Supabase mit Offline-Fallback'),
        ('Live preview editor with multiple professional templates',
         'Live-Vorschau-Editor mit mehreren professionellen Vorlagen'),
        ('AI-powered suggestions for improving resume bullet points',
         'KI-gestützte Vorschläge zur Verbesserung von Lebenslauf-Stichpunkten'),
        ('High-quality PDF export with proper formatting',
         'Hochqualitatives PDF-Export mit korrekter Formatierung'),
        ('Conversational AI with per-channel context memory',
         'Konversations-KI mit kanalbasiertem Kontextgedächtnis'),
        ('Text-to-image generation from prompts',
         'Text-zu-Bild-Generierung aus Eingaben'),
        ('Modular plugin architecture for adding new AI capabilities',
         'Modulare Plugin-Architektur zum Hinzufügen neuer KI-Fähigkeiten'),
        ('XP-based leveling system with role rewards and leaderboards',
         'XP-basiertes Leveling-System mit Rollen-Belohnungen und Bestenlisten'),
        ('Full moderation suite with audit logging',
         'Vollständiges Moderations-Paket mit Audit-Logging'),
        ('Runs 24/7 on Linux VPS with automatic restarts',
         'Läuft rund um die Uhr auf einem Linux-VPS mit automatischen Neustarts'),
    ]
    
    for en, de in features:
        html = html.replace(en, de)
    
    # Project descriptions
    descriptions = [
        ('A cross-platform mobile app for collaborative grocery shopping with real-time sync, smart categories, and offline support. Published on iOS and Android.',
         'Eine plattformübergreifende mobile App für gemeinsames Einkaufen mit Echtzeit-Synchronisierung, smarten Kategorien und Offline-Unterstützung. Verfügbar auf iOS und Android.'),
        ('A modern marketing website for the Shoply app featuring interactive 3D phone mockups, smooth scroll animations, and optimized performance.',
         'Eine moderne Marketing-Website für die Shoply-App mit interaktiven 3D-Telefon-Mockups, sanften Scroll-Animationen und optimierter Performance.'),
        ('A mobile learning companion built with React Native and Expo — featuring spaced repetition flashcards, study planning, and progress tracking.',
         'Ein mobiler Lernbegleiter mit React Native und Expo – mit Spaced-Repetition-Karteikarten, Lernplanung und Fortschrittsverfolgung.'),
        ('A web application that helps users create professional resumes with customizable templates, live preview editing, and AI-powered bullet point suggestions.',
         'Eine Webanwendung, die Nutzern hilft, professionelle Lebensläufe mit anpassbaren Vorlagen, Live-Vorschau und KI-gestützten Verbesserungsvorschlägen zu erstellen.'),
        ('An AI-powered Discord bot bringing language models and image generation to servers — with context memory, rate limiting, and a modular plugin system.',
         'Ein KI-gesteuerter Discord-Bot, der Sprachmodelle und Bildgenerierung in Server bringt – mit Kontextgedächtnis, Rate-Limiting und modularem Plugin-System.'),
        ('A feature-rich Discord bot for server management and entertainment — with moderation tools, XP leveling, music playback, and custom commands.',
         'Ein funktionsreicher Discord-Bot für Server-Verwaltung und Unterhaltung – mit Moderations-Tools, XP-Leveling, Musikwiedergabe und benutzerdefinierten Befehlen.'),
    ]
    
    for en, de in descriptions:
        html = html.replace(en, de)
    
    # Lang attribute
    html = html.replace('<html lang="en">', '<html lang="de">')
    
    return html

# =============================================================================
# PAGE TRANSFORMERS
# =============================================================================

def process_page(en_path, de_path, de_url, page_title=None):
    """Generic page transformer"""
    html = read_file(en_path)
    if html is None:
        return False
    
    html = translate_text(html)
    html = replace_meta_urls(html, de_url)
    html = replace_locale(html)
    html = update_body_links(html)
    
    # Language switcher for index pages
    if 'index.html' in en_path:
        html = html.replace(
            '<a href="/de" class="font-semibold uppercase tracking-wider hover:text-black dark:hover:text-white blend" data-astro-cid-j7pv25f6> DE </a>',
            '<a href="/" class="uppercase tracking-wider hover:text-black dark:hover:text-white blend" data-astro-cid-j7pv25f6> EN </a> <span class="font-semibold uppercase tracking-wider" data-astro-cid-j7pv25f6>DE</span>'
        )
    
    if write_file(de_path, html):
        print(f"✅ {de_path.replace(BASE_DIR, '')}")
        return True
    return False

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main translation process"""
    files_processed = 0
    
    # 1. Main index.html
    files_processed += process_page(
        os.path.join(BASE_DIR, 'index.html'),
        os.path.join(BASE_DIR, 'de', 'index.html'),
        'https://danieldietrich.tech/de/'
    )
    
    # 2. Work page
    files_processed += process_page(
        os.path.join(BASE_DIR, 'work', 'index.html'),
        os.path.join(BASE_DIR, 'de', 'work', 'index.html'),
        'https://danieldietrich.tech/de/work/'
    )
    
    # 3. Projects page
    files_processed += process_page(
        os.path.join(BASE_DIR, 'projects', 'index.html'),
        os.path.join(BASE_DIR, 'de', 'projects', 'index.html'),
        'https://danieldietrich.tech/de/projects/'
    )
    
    # 4. Project detail pages
    projects = [
        ('resumeme', 'https://danieldietrich.tech/de/projects/resumeme/'),
        ('tharos-discord-bot', 'https://danieldietrich.tech/de/projects/tharos-discord-bot/'),
        ('freeai-discord-bot', 'https://danieldietrich.tech/de/projects/freeai-discord-bot/'),
        ('shoply-landing-page', 'https://danieldietrich.tech/de/projects/shoply-landing-page/'),
        ('shoply-app', 'https://danieldietrich.tech/de/projects/shoply-app/'),
        ('studyapp', 'https://danieldietrich.tech/de/projects/studyapp/'),
    ]
    
    for proj_slug, proj_url in projects:
        files_processed += process_page(
            os.path.join(BASE_DIR, 'projects', proj_slug, 'index.html'),
            os.path.join(BASE_DIR, 'de', 'projects', proj_slug, 'index.html'),
            proj_url
        )
    
    # 5. Legal pages
    files_processed += process_page(
        os.path.join(BASE_DIR, 'legal', 'privacy', 'index.html'),
        os.path.join(BASE_DIR, 'de', 'legal', 'privacy', 'index.html'),
        'https://danieldietrich.tech/de/legal/privacy/'
    )
    
    files_processed += process_page(
        os.path.join(BASE_DIR, 'legal', 'terms', 'index.html'),
        os.path.join(BASE_DIR, 'de', 'legal', 'terms', 'index.html'),
        'https://danieldietrich.tech/de/legal/terms/'
    )
    
    # Print summary
    print(f"\n{'='*70}")
    print(f"✅ Translation Complete: {files_processed}/11 files processed")
    print(f"{'='*70}\n")
    
    return 0 if files_processed == 11 else 1

if __name__ == '__main__':
    sys.exit(main())
