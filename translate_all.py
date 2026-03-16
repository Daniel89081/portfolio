#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
German HTML Translation Script for danieldietrich.tech
Translates all English pages to German versions with updated meta tags and content.
"""

import os
import re
import sys

# Set base directory
BASE = os.path.dirname(os.path.abspath(__file__))
print(f"Working directory: {BASE}")

def read_file(path):
    """Read HTML file with UTF-8 encoding"""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    """Write HTML file with UTF-8 encoding"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return path

def replace_meta_urls(html, de_url):
    """Update canonical, og:url, twitter:url to DE version."""
    html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{de_url}">', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{de_url}">', html)
    html = re.sub(r'<meta name="twitter:url" content="[^"]*">', f'<meta name="twitter:url" content="{de_url}">', html)
    return html

def replace_locale(html):
    """Swap og:locale and og:locale:alternate."""
    html = html.replace(
        'content="en_US"><meta property="og:locale:alternate" content="de_DE"',
        'content="de_DE"><meta property="og:locale:alternate" content="en_US"'
    )
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

def translate_common(html):
    """Translate text common to most pages."""
    # Footer
    html = html.replace('&copy; 2026 Daniel Dietrich. All rights reserved', 
                        '&copy; 2026 Daniel Dietrich. Alle Rechte vorbehalten')
    html = html.replace('&copy; 2026 Jannis Dietrich. All rights reserved', 
                        '&copy; 2026 Daniel Dietrich. Alle Rechte vorbehalten')
    html = html.replace('aria-label="Back to top of page"', 
                        'aria-label="Nach oben scrollen"')
    html = html.replace('> Back to top &uarr;\n</button>', 
                        '> Nach oben &uarr;\n</button>')
    
    # Work descriptions
    work_translations = [
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
    
    for en, de in work_translations:
        html = html.replace(f'<li>{en}</li>', f'<li>{de}</li>')
    
    # Project features
    feature_translations = [
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
    
    for en, de in feature_translations:
        html = html.replace(en, de)
    
    # Project descriptions
    project_descriptions = [
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
    
    for en, de in project_descriptions:
        html = html.replace(en, de)
    
    # Link labels
    html = html.replace('\nSource\n', '\nQuellcode\n')
    html = html.replace('> Source Code </a>', '> Quellcode </a>')
    html = html.replace('> Live Demo </a>', '> Live-Demo </a>')
    html = html.replace('2 min read', '2 Min. Lesen')
    
    # Footer links
    html = html.replace('> Terms <', '> Nutzungsbedingungen <')
    html = html.replace('> Privacy <', '> Datenschutz <')
    
    # Headings
    html = html.replace('<h2 id="features">Features</h2>', '<h2 id="funktionen">Funktionen</h2>')
    html = html.replace('<h2 id="what-i-learned">What I Learned</h2>', '<h2 id="was-ich-gelernt-habe">Was ich gelernt habe</h2>')
    
    return html

# Transform index.html
def transform_index():
    """Transform /index.html to /de/index.html"""
    src = os.path.join(BASE, 'index.html')
    dst = os.path.join(BASE, 'de', 'index.html')
    
    print(f"\n📄 Processing: index.html")
    html = read_file(src)
    
    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_meta_urls(html, 'https://danieldietrich.tech/de/')
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)
    
    # Page-specific translations
    html = html.replace('<title>Home | Daniel Dietrich </title>', '<title>Startseite | Daniel Dietrich</title>')
    html = html.replace('content="Home | Daniel Dietrich"', 'content="Startseite | Daniel Dietrich"')
    html = html.replace('"name":"Home"', '"name":"Startseite"')
    
    # Meta descriptions
    html = re.sub(r'<meta name="description" content="CS Student[^"]*">', 
                 '<meta name="description" content="Physik- und Management-Student aus Ulm. Entwickle Apps, Bots und Web-Anwendungen.">', html)
    html = re.sub(r'<meta property="og:description" content="Student from Ulm[^"]*">', 
                 '<meta property="og:description" content="Student aus Ulm, Deutschland.">', html)
    
    # Language switcher
    html = html.replace(
        '<a href="/de" class="font-semibold uppercase tracking-wider hover:text-black dark:hover:text-white blend" data-astro-cid-j7pv25f6> DE </a>',
        '<a href="/" class="uppercase tracking-wider hover:text-black dark:hover:text-white blend" data-astro-cid-j7pv25f6> EN </a> <span class="font-semibold uppercase tracking-wider" data-astro-cid-j7pv25f6>DE</span>'
    )
    
    # Header & content
    html = html.replace('> Physics and Management Student <', '> Physik und Management Student <')
    html = html.replace('> Ulm, Germany <', '> Ulm, Deutschland <')
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
    
    # About text
    html = html.replace(
        'student at Ulm University (graduating Nov 2026, GPA equivalent 1.3) — building on a Bachelor\'s degree in Physics. <br> Current focus: Master\'s thesis on <b>Replica Exchange Monte Carlo methods for quantum computing</b>. <br> Targeting <b>international tech sales</b> roles starting January 2027.',
        'Student an der Universität Ulm (Abschluss Nov 2026, Note äquivalent 1,3) – aufbauend auf einem Bachelor in Physik. <br> Aktueller Schwerpunkt: Masterarbeit über <b>Replica Exchange Monte Carlo-Methoden für Quantencomputing</b>. <br> Angestrebte Zielposition: <b>International Tech Sales</b> ab Januar 2027.'
    )
    
    write_file(dst, html)
    print(f"✅ Created: {dst}")

# Transform work/index.html
def transform_work():
    """Transform /work/index.html to /de/work/index.html"""
    src = os.path.join(BASE, 'work', 'index.html')
    dst = os.path.join(BASE, 'de', 'work', 'index.html')
    
    print(f"\n📄 Processing: work/index.html")
    html = read_file(src)
    
    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_meta_urls(html, 'https://danieldietrich.tech/de/work/')
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)
    
    # Fix domain names
    html = html.replace('https://jannisdietrich.com/', 'https://danieldietrich.tech/')
    html = html.replace('https://jannisdietrich.com', 'https://danieldietrich.tech')
    
    # Page-specific translations
    html = re.sub(r'<title>Work \| [^<]*</title>', '<title>Arbeit | Daniel Dietrich</title>', html)
    html = re.sub(r'content="Work \| [^"]*"', 'content="Arbeit | Daniel Dietrich"', html)
    html = html.replace('"name":"Work"', '"name":"Arbeit"')
    
    html = html.replace('> Work <', '> Arbeit <')
    
    write_file(dst, html)
    print(f"✅ Created: {dst}")

# Transform projects/index.html
def transform_projects():
    """Transform /projects/index.html to /de/projects/index.html"""
    src = os.path.join(BASE, 'projects', 'index.html')
    dst = os.path.join(BASE, 'de', 'projects', 'index.html')
    
    print(f"\n📄 Processing: projects/index.html")
    html = read_file(src)
    
    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_meta_urls(html, 'https://danieldietrich.tech/de/projects/')
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)
    
    # Fix domain names
    html = html.replace('https://jannisdietrich.com/', 'https://danieldietrich.tech/')
    html = html.replace('https://jannisdietrich.com', 'https://danieldietrich.tech')
    
    # Page-specific translations
    html = re.sub(r'<title>Projects \| [^<]*</title>', '<title>Projekte | Daniel Dietrich</title>', html)
    html = html.replace('"name":"Projects"', '"name":"Projekte"')
    
    html = html.replace('> Projects <', '> Projekte <')
    
    write_file(dst, html)
    print(f"✅ Created: {dst}")

# Transform project pages
def transform_project_page(slug, title_de, desc_de, url_de):
    """Transform individual project pages"""
    src = os.path.join(BASE, 'projects', slug, 'index.html')
    dst = os.path.join(BASE, 'de', 'projects', slug, 'index.html')
    
    print(f"\n📄 Processing: projects/{slug}/index.html")
    html = read_file(src)
    
    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_meta_urls(html, url_de)
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)
    
    # Fix domain names
    html = html.replace('https://jannisdietrich.com/', 'https://danieldietrich.tech/')
    html = html.replace('https://jannisdietrich.com', 'https://danieldietrich.tech')
    
    # Page-specific translations
    html = re.sub(r'<title>[^|]*\| [^<]*</title>', f'<title>{title_de} | Daniel Dietrich</title>', html)
    html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc_de}">', html, count=1)
    
    # Back button
    html = html.replace('&larr; Back Projects', '&larr; Zurück zu Projekte')
    
    write_file(dst, html)
    print(f"✅ Created: {dst}")

# Transform legal pages
def transform_legal_privacy():
    """Transform privacy policy page"""
    src = os.path.join(BASE, 'legal', 'privacy', 'index.html')
    dst = os.path.join(BASE, 'de', 'legal', 'privacy', 'index.html')
    
    print(f"\n📄 Processing: legal/privacy/index.html")
    html = read_file(src)
    
    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_meta_urls(html, 'https://danieldietrich.tech/de/legal/privacy/')
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)
    
    # Fix domain names
    html = html.replace('https://jannisdietrich.com/', 'https://danieldietrich.tech/')
    html = html.replace('https://jannisdietrich.com', 'https://danieldietrich.tech')
    
    # Page-specific translations
    html = re.sub(r'<title>Privacy Policy \| [^<]*</title>', '<title>Datenschutzerklärung | Daniel Dietrich</title>', html)
    html = html.replace('"name":"Privacy Policy"', '"name":"Datenschutzerklärung"')
    html = html.replace('> Privacy Policy <', '> Datenschutzerklärung <')
    
    write_file(dst, html)
    print(f"✅ Created: {dst}")

def transform_legal_terms():
    """Transform terms of use page"""
    src = os.path.join(BASE, 'legal', 'terms', 'index.html')
    dst = os.path.join(BASE, 'de', 'legal', 'terms', 'index.html')
    
    print(f"\n📄 Processing: legal/terms/index.html")
    html = read_file(src)
    
    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_meta_urls(html, 'https://danieldietrich.tech/de/legal/terms/')
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)
    
    # Fix domain names
    html = html.replace('https://jannisdietrich.com/', 'https://danieldietrich.tech/')
    html = html.replace('https://jannisdietrich.com', 'https://danieldietrich.tech')
    
    # Page-specific translations
    html = re.sub(r'<title>Terms of Use \| [^<]*</title>', '<title>Nutzungsbedingungen | Daniel Dietrich</title>', html)
    html = html.replace('"name":"Terms of Use"', '"name":"Nutzungsbedingungen"')
    html = html.replace('> Terms of Use <', '> Nutzungsbedingungen <')
    
    write_file(dst, html)
    print(f"✅ Created: {dst}")

# Main execution
if __name__ == '__main__':
    try:
        print("=" * 60)
        print("🌐 German HTML Translation Script")
        print("=" * 60)
        
        # Transform main pages
        transform_index()
        transform_work()
        transform_projects()
        
        # Transform project detail pages
        transform_project_page(
            'resumeme',
            'ResumeMe – Web-App',
            'Eine Webanwendung, die Nutzern hilft, professionelle Lebensläufe zu erstellen.',
            'https://danieldietrich.tech/de/projects/resumeme/'
        )
        transform_project_page(
            'tharos-discord-bot',
            'Tharos – Discord Bot',
            'Ein funktionsreicher Discord-Bot für Server-Verwaltung und Unterhaltung.',
            'https://danieldietrich.tech/de/projects/tharos-discord-bot/'
        )
        transform_project_page(
            'freeai-discord-bot',
            'FreeAI – KI Discord Bot',
            'Ein KI-gesteuerter Discord-Bot mit Sprachmodellen und Bildgenerierung.',
            'https://danieldietrich.tech/de/projects/freeai-discord-bot/'
        )
        transform_project_page(
            'shoply-landing-page',
            'Shoply Landing Page',
            'Eine moderne Marketing-Website für die Shoply-App.',
            'https://danieldietrich.tech/de/projects/shoply-landing-page/'
        )
        transform_project_page(
            'shoply-app',
            'Shoply – Kollaborative Shopping-App',
            'Eine plattformübergreifende mobile App für gemeinsames Einkaufen.',
            'https://danieldietrich.tech/de/projects/shoply-app/'
        )
        transform_project_page(
            'studyapp',
            'StudyApp – Lernbegleiter',
            'Ein mobiler Lernbegleiter mit React Native und Expo.',
            'https://danieldietrich.tech/de/projects/studyapp/'
        )
        
        # Transform legal pages
        transform_legal_privacy()
        transform_legal_terms()
        
        print("\n" + "=" * 60)
        print("✅ All translations completed successfully!")
        print("=" * 60)
        sys.exit(0)
        
    except Exception as e:
        print(f"\n❌ Error during translation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
