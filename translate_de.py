#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate English pages to German for danieldietrich.tech"""

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

def translate_common(html):
    """Translate text common to most pages."""
    # Footer
    html = html.replace('&copy; 2026 Daniel Dietrich. All rights reserved', '&copy; 2026 Daniel Dietrich. Alle Rechte vorbehalten')
    html = html.replace('&copy; 2026 Jannis Dietrich. All rights reserved', '&copy; 2026 Daniel Dietrich. Alle Rechte vorbehalten')
    html = html.replace('aria-label="Back to top of page"', 'aria-label="Nach oben scrollen"')
    html = html.replace('> Back to top &uarr;\n</button>', '> Nach oben &uarr;\n</button>')
    # Work descriptions (shared between work page and index)
    html = html.replace('<li>Built responsive web applications using React, Next.js, and TypeScript</li>',
                        '<li>Entwicklung responsiver Webanwendungen mit React, Next.js und TypeScript</li>')
    html = html.replace('<li>Developed cross-platform mobile apps with Flutter and Dart</li>',
                        '<li>Entwicklung plattformübergreifender mobiler Apps mit Flutter und Dart</li>')
    html = html.replace('<li>Integrated backends with Firebase, Supabase, and REST APIs</li>',
                        '<li>Integration von Backends mit Firebase, Supabase und REST-APIs</li>')
    html = html.replace('<li>Maintained clear communication with clients and delivered projects on time</li>',
                        '<li>Klare Kommunikation mit Kunden und pünktliche Projektlieferung</li>')
    html = html.replace('<li>Achieved top-rated status through consistent high-quality work</li>',
                        '<li>Top-Bewertung durch konstant hochwertige Arbeit erhalten</li>')
    html = html.replace('<li>Gained hands-on experience with AI/ML pipelines and natural language processing systems</li>',
                        '<li>Praktische Erfahrung mit KI/ML-Pipelines und Natural Language Processing</li>')
    html = html.replace('<li>Collaborated with cross-functional engineering teams in an agile environment</li>',
                        '<li>Zusammenarbeit mit interdisziplinären Entwicklungsteams in einem agilen Umfeld</li>')
    html = html.replace('<li>Assisted in testing and improving voice recognition features for in-car assistants</li>',
                        '<li>Mitarbeit beim Testen und Verbessern von Spracherkennungsfunktionen für Fahrzeugassistenten</li>')
    html = html.replace('<li>Developed internal tooling to streamline development workflows</li>',
                        '<li>Entwicklung interner Tools zur Optimierung von Entwicklungsabläufen</li>')
    # Project bullets (shared)
    html = html.replace('Real-time shared lists synced via Firebase across all devices',
                        'Geteilte Listen in Echtzeit via Firebase über alle Geräte synchronisiert')
    html = html.replace('Offline-first architecture — works without internet',
                        'Offline-first-Architektur – funktioniert ohne Internet')
    html = html.replace('Published on both App Store and Google Play',
                        'Im App Store und bei Google Play veröffentlicht')
    html = html.replace('Interactive Three.js 3D phone mockup with React Three Fiber',
                        'Interaktives Three.js-3D-Telefon-Mockup mit React Three Fiber')
    html = html.replace('Scroll-triggered reveal animations and responsive design',
                        'Scroll-gesteuerte Einblend-Animationen und responsives Design')
    html = html.replace('Lazy-loaded 3D assets with optimized bundle size',
                        'Lazy-geladene 3D-Assets mit optimierter Bundle-Größe')
    html = html.replace('Spaced repetition algorithm for effective flashcard review',
                        'Spaced-Repetition-Algorithmus für effektives Karteikarten-Lernen')
    html = html.replace('Pomodoro timer with session statistics and streaks',
                        'Pomodoro-Timer mit Sitzungsstatistiken und Streaks')
    html = html.replace('Real-time sync via Supabase with offline fallback',
                        'Echtzeit-Synchronisierung via Supabase mit Offline-Fallback')
    html = html.replace('Live preview editor with multiple professional templates',
                        'Live-Vorschau-Editor mit mehreren professionellen Vorlagen')
    html = html.replace('AI-powered suggestions for improving resume bullet points',
                        'KI-gestützte Vorschläge zur Verbesserung von Lebenslauf-Stichpunkten')
    html = html.replace('High-quality PDF export with proper formatting',
                        'Hochqualitatives PDF-Export mit korrekter Formatierung')
    html = html.replace('Conversational AI with per-channel context memory',
                        'Konversations-KI mit kanalbasiertem Kontextgedächtnis')
    html = html.replace('Text-to-image generation from prompts',
                        'Text-zu-Bild-Generierung aus Eingaben')
    html = html.replace('Modular plugin architecture for adding new AI capabilities',
                        'Modulare Plugin-Architektur zum Hinzufügen neuer KI-Fähigkeiten')
    html = html.replace('XP-based leveling system with role rewards and leaderboards',
                        'XP-basiertes Leveling-System mit Rollen-Belohnungen und Bestenlisten')
    html = html.replace('Full moderation suite with audit logging',
                        'Vollständiges Moderations-Paket mit Audit-Logging')
    html = html.replace('Runs 24/7 on Linux VPS with automatic restarts',
                        'Läuft rund um die Uhr auf einem Linux-VPS mit automatischen Neustarts')
    # Project descriptions (inline list summaries)
    html = html.replace(
        'A cross-platform mobile app for collaborative grocery shopping with real-time sync, smart categories, and offline support. Published on iOS and Android.',
        'Eine plattformübergreifende mobile App für gemeinsames Einkaufen mit Echtzeit-Synchronisierung, smarten Kategorien und Offline-Unterstützung. Verfügbar auf iOS und Android.')
    html = html.replace(
        'A modern marketing website for the Shoply app featuring interactive 3D phone mockups, smooth scroll animations, and optimized performance.',
        'Eine moderne Marketing-Website für die Shoply-App mit interaktiven 3D-Telefon-Mockups, sanften Scroll-Animationen und optimierter Performance.')
    html = html.replace(
        'A mobile learning companion built with React Native and Expo — featuring spaced repetition flashcards, study planning, and progress tracking.',
        'Ein mobiler Lernbegleiter mit React Native und Expo – mit Spaced-Repetition-Karteikarten, Lernplanung und Fortschrittsverfolgung.')
    html = html.replace(
        'A web application that helps users create professional resumes with customizable templates, live preview editing, and AI-powered bullet point suggestions.',
        'Eine Webanwendung, die Nutzern hilft, professionelle Lebensläufe mit anpassbaren Vorlagen, Live-Vorschau und KI-gestützten Verbesserungsvorschlägen zu erstellen.')
    html = html.replace(
        'An AI-powered Discord bot bringing language models and image generation to servers — with context memory, rate limiting, and a modular plugin system.',
        'Ein KI-gesteuerter Discord-Bot, der Sprachmodelle und Bildgenerierung in Server bringt – mit Kontextgedächtnis, Rate-Limiting und modularem Plugin-System.')
    html = html.replace(
        'A feature-rich Discord bot for server management and entertainment — with moderation tools, XP leveling, music playback, and custom commands.',
        'Ein funktionsreicher Discord-Bot für Server-Verwaltung und Unterhaltung – mit Moderations-Tools, XP-Leveling, Musikwiedergabe und benutzerdefinierten Befehlen.')
    # "Source" and "Demo" link labels in project cards
    html = html.replace('\nSource\n', '\nQuellcode\n')
    html = html.replace('\nDemo\n', '\nDemo\n')
    # "2 min read"
    html = html.replace('2 min read', '2 Min. Lesen')
    # "Source Code" link text
    html = html.replace('> Source Code </a>', '> Quellcode </a>')
    html = html.replace('> Live Demo </a>', '> Live-Demo </a>')
    # article content translations
    html = html.replace(
        '<p>Shoply is a collaborative shopping list app that makes grocery shopping easier for families and roommates. Users can create shared lists, assign items, and see real-time updates as others check off items.</p>',
        '<p>Shoply ist eine kollaborative Einkaufslisten-App, die das Einkaufen für Familien und Mitbewohner einfacher macht. Nutzer können gemeinsame Listen erstellen, Artikel zuweisen und Echtzeit-Updates sehen, wenn andere Artikel abhaken.</p>')
    html = html.replace('<li><strong>Shared Lists</strong> – Create and share shopping lists with family, friends, or roommates</li>',
        '<li><strong>Geteilte Listen</strong> – Erstelle und teile Einkaufslisten mit Familie, Freunden oder Mitbewohnern</li>')
    html = html.replace('<li><strong>Real-time Sync</strong> – Changes sync instantly across all devices via Firebase</li>',
        '<li><strong>Echtzeit-Synchronisierung</strong> – Änderungen synchronisieren sofort auf allen Geräten via Firebase</li>')
    html = html.replace('<li><strong>Smart Categories</strong> – Items are automatically organized by store sections</li>',
        '<li><strong>Intelligente Kategorien</strong> – Artikel werden automatisch nach Supermarktabschnitten sortiert</li>')
    html = html.replace('<li><strong>Offline Support</strong> – Works without internet and syncs when back online</li>',
        '<li><strong>Offline-Unterstützung</strong> – Funktioniert ohne Internet und synchronisiert bei Wiederverbindung</li>')
    html = html.replace('<li><strong>Cross-platform</strong> – Available on both iOS and Android</li>',
        '<li><strong>Plattformübergreifend</strong> – Verfügbar auf iOS und Android</li>')
    html = html.replace(
        '<p>Built with <strong>Flutter</strong> and <strong>Dart</strong> for a smooth cross-platform experience. Firebase handles authentication, real-time database, and cloud storage. The app follows clean architecture principles with BLoC state management.</p>',
        '<p>Entwickelt mit <strong>Flutter</strong> und <strong>Dart</strong> für eine flüssige plattformübergreifende Erfahrung. Firebase übernimmt Authentifizierung, Echtzeit-Datenbank und Cloud-Speicher. Die App folgt Clean-Architecture-Prinzipien mit BLoC-State-Management.</p>')
    html = html.replace(
        "<p>This was my first major Flutter project published to app stores. I gained deep experience with Flutter's widget system, Firebase integration, real-time data synchronization, and the full app store submission process.</p>",
        '<p>Dies war mein erstes großes Flutter-Projekt, das in den App Stores veröffentlicht wurde. Ich sammelte tiefe Erfahrungen mit Flutters Widget-System, Firebase-Integration, Echtzeit-Datensynchronisierung und dem vollständigen App-Store-Einreichungsprozess.</p>')
    html = html.replace(
        '<p>A sleek, modern landing page designed to showcase the Shoply mobile app. Features interactive 3D elements and smooth scroll animations to create an engaging user experience.</p>',
        '<p>Eine elegante, moderne Landing Page zur Präsentation der Shoply-Mobile-App. Mit interaktiven 3D-Elementen und sanften Scroll-Animationen für ein ansprechendes Nutzererlebnis.</p>')
    html = html.replace('<li><strong>3D Phone Mockup</strong> – Interactive Three.js scene showing the app on a rotating phone</li>',
        '<li><strong>3D-Telefon-Mockup</strong> – Interaktive Three.js-Szene mit der App auf einem rotierenden Telefon</li>')
    html = html.replace('<li><strong>Scroll Animations</strong> – Smooth reveal animations as users scroll through features</li>',
        '<li><strong>Scroll-Animationen</strong> – Sanfte Einblend-Animationen beim Durchscrollen der Funktionen</li>')
    html = html.replace('<li><strong>Responsive Design</strong> – Looks great on all screen sizes, from mobile to ultrawide</li>',
        '<li><strong>Responsives Design</strong> – Sieht auf allen Bildschirmgrößen hervorragend aus</li>')
    html = html.replace('<li><strong>Performance Optimized</strong> – Lazy-loaded 3D assets, optimized images, and minimal bundle size</li>',
        '<li><strong>Performance-Optimiert</strong> – Lazy-geladene 3D-Assets, optimierte Bilder und minimale Bundle-Größe</li>')
    html = html.replace(
        '<p>Built with <strong>Next.js 14</strong> and <strong>TypeScript</strong> for a fast, SEO-friendly static site. <strong>Three.js</strong> with React Three Fiber powers the 3D visuals. <strong>Tailwind CSS</strong> handles styling with a custom design system. Deployed on Vercel with automatic previews.</p>',
        '<p>Entwickelt mit <strong>Next.js 14</strong> und <strong>TypeScript</strong> für eine schnelle, SEO-freundliche statische Seite. <strong>Three.js</strong> mit React Three Fiber treibt die 3D-Visualisierungen an. <strong>Tailwind CSS</strong> übernimmt das Styling. Deployed auf Vercel mit automatischen Vorschauen.</p>')
    html = html.replace(
        '<p>This project taught me a lot about combining 3D graphics with web development. I learned to optimize Three.js performance for web, create accessible interactive experiences, and build marketing pages that convert.</p>',
        '<p>Dieses Projekt lehrte mich viel über die Kombination von 3D-Grafik und Webentwicklung. Ich lernte, Three.js-Performance für das Web zu optimieren und Marketing-Seiten zu bauen, die konvertieren.</p>')
    html = html.replace(
        '<p>StudyApp helps students organize their study sessions, track progress, and build effective learning habits. Built with React Native and Expo for a native experience on both platforms.</p>',
        '<p>StudyApp hilft Studierenden, ihre Lernsitzungen zu organisieren, Fortschritte zu verfolgen und effektive Lerngewohnheiten aufzubauen. Entwickelt mit React Native und Expo für eine native Erfahrung auf beiden Plattformen.</p>')
    html = html.replace('<li><strong>Study Planner</strong> – Schedule study sessions with smart reminders</li>',
        '<li><strong>Lernplaner</strong> – Plane Lernsitzungen mit intelligenten Erinnerungen</li>')
    html = html.replace('<li><strong>Flashcards</strong> – Create and review flashcard decks with spaced repetition</li>',
        '<li><strong>Karteikarten</strong> – Erstelle und übe Karteikarten-Sets mit Spaced Repetition</li>')
    html = html.replace('<li><strong>Progress Tracking</strong> – Visualize study time and topic coverage with charts</li>',
        '<li><strong>Fortschrittsverfolgung</strong> – Visualisiere Lernzeit und Themenabdeckung mit Diagrammen</li>')
    html = html.replace('<li><strong>Note Taking</strong> – Rich text notes organized by subject and topic</li>',
        '<li><strong>Notizen</strong> – Rich-Text-Notizen, nach Fach und Thema organisiert</li>')
    html = html.replace('<li><strong>Study Timer</strong> – Pomodoro-style timer with session statistics</li>',
        '<li><strong>Lern-Timer</strong> – Pomodoro-Timer mit Sitzungsstatistiken</li>')
    html = html.replace(
        '<p>Built with <strong>React Native</strong> and <strong>Expo</strong> using <strong>TypeScript</strong> for type safety. <strong>Supabase</strong> provides authentication, database, and real-time sync. Uses React Navigation for routing and Zustand for state management. Charts powered by Victory Native.</p>',
        '<p>Entwickelt mit <strong>React Native</strong> und <strong>Expo</strong> unter Verwendung von <strong>TypeScript</strong>. <strong>Supabase</strong> liefert Authentifizierung, Datenbank und Echtzeit-Sync. Verwendet React Navigation für Routing und Zustand für State-Management. Diagramme mit Victory Native.</p>')
    html = html.replace(
        "This project gave me hands-on experience with React Native's ecosystem and mobile-first UX design. I learned about spaced repetition algorithms, offline-first architecture with Supabase, and building productive study tools that students actually want to use.",
        'Dieses Projekt gab mir praktische Erfahrung mit dem React-Native-Ökosystem und Mobile-First-UX-Design. Ich lernte Spaced-Repetition-Algorithmen, Offline-first-Architektur mit Supabase und den Aufbau produktiver Lerntools.')
    html = html.replace(
        '<p>ResumeMe is a web application that makes creating professional resumes fast and easy. Choose from modern templates, fill in your details, and export a polished PDF ready for job applications.</p>',
        '<p>ResumeMe ist eine Webanwendung, die das Erstellen professioneller Lebensläufe schnell und einfach macht. Wähle aus modernen Vorlagen, fülle deine Daten ein und exportiere ein hochwertiges PDF für Bewerbungen.</p>')
    html = html.replace('<li><strong>Template Gallery</strong> – Multiple professionally designed resume templates</li>',
        '<li><strong>Vorlagengalerie</strong> – Mehrere professionell gestaltete Lebenslauf-Vorlagen</li>')
    html = html.replace('<li><strong>Live Preview</strong> – See changes in real-time as you edit</li>',
        '<li><strong>Live-Vorschau</strong> – Sieh Änderungen in Echtzeit beim Bearbeiten</li>')
    html = html.replace('<li><strong>PDF Export</strong> – High-quality PDF generation with proper formatting</li>',
        '<li><strong>PDF-Export</strong> – Hochqualitatives PDF-Export mit korrekter Formatierung</li>')
    html = html.replace('<li><strong>AI Suggestions</strong> – Smart suggestions for improving resume bullet points</li>',
        '<li><strong>KI-Vorschläge</strong> – Intelligente Vorschläge zur Verbesserung von Lebenslauf-Stichpunkten</li>')
    html = html.replace('<li><strong>Save &#x26; Edit</strong> – Save multiple resumes and come back to edit them anytime</li>',
        '<li><strong>Speichern &amp; Bearbeiten</strong> – Speichere mehrere Lebensläufe und bearbeite sie jederzeit</li>')
    html = html.replace(
        '<p>Built with <strong>Next.js</strong> and <strong>TypeScript</strong> for a fast, SEO-friendly web app. <strong>React</strong> powers the interactive editor with live preview. <strong>Tailwind CSS</strong> provides responsive styling. PDF generation uses react-pdf. Deployed on Vercel.</p>',
        '<p>Entwickelt mit <strong>Next.js</strong> und <strong>TypeScript</strong> für eine schnelle Web-App. <strong>React</strong> treibt den interaktiven Editor mit Live-Vorschau an. <strong>Tailwind CSS</strong> liefert responsives Styling. PDF-Generierung mit react-pdf. Deployed auf Vercel.</p>')
    html = html.replace(
        '<p>Building ResumeMe taught me about complex form management, real-time preview rendering, and PDF generation in the browser. I also explored AI-powered text suggestions and learned how to create tools that help people present themselves professionally.</p>',
        '<p>Der Aufbau von ResumeMe lehrte mich komplexes Formular-Management, Echtzeit-Vorschau-Rendering und PDF-Generierung im Browser. Ich erforschte auch KI-gestützte Textvorschläge und lernte, Tools zu erstellen, die Menschen helfen, sich professionell zu präsentieren.</p>')
    html = html.replace(
        '<p>FreeAI brings the power of AI directly into Discord. Users can chat with language models, generate images, summarize text, and more — all without leaving their Discord server.</p>',
        '<p>FreeAI bringt die Kraft der KI direkt in Discord. Nutzer können mit Sprachmodellen chatten, Bilder generieren, Texte zusammenfassen und mehr – alles ohne ihren Discord-Server zu verlassen.</p>')
    html = html.replace('<li><strong>AI Chat</strong> – Conversational AI powered by language models with context memory</li>',
        '<li><strong>KI-Chat</strong> – Konversations-KI, angetrieben von Sprachmodellen mit Kontextgedächtnis</li>')
    html = html.replace('<li><strong>Image Generation</strong> – Generate images from text prompts using AI models</li>',
        '<li><strong>Bildgenerierung</strong> – Generiere Bilder aus Texteingaben mit KI-Modellen</li>')
    html = html.replace('<li><strong>Text Summarization</strong> – Summarize long messages or articles with a single command</li>',
        '<li><strong>Textzusammenfassung</strong> – Fasse lange Nachrichten oder Artikel mit einem Befehl zusammen</li>')
    html = html.replace('<li><strong>Translation</strong> – Translate text between languages instantly</li>',
        '<li><strong>Übersetzung</strong> – Übersetze Texte sofort zwischen Sprachen</li>')
    html = html.replace('<li><strong>Customizable</strong> – Server admins can configure model behavior and rate limits</li>',
        '<li><strong>Anpassbar</strong> – Server-Admins können das Modellverhalten und Rate-Limits konfigurieren</li>')
    html = html.replace(
        '<p>Built with <strong>Python</strong> and <strong>Discord.py</strong>. Integrates with multiple AI APIs and uses <strong>TensorFlow</strong> for custom model inference. Features a modular plugin architecture that makes it easy to add new AI capabilities.</p>',
        '<p>Entwickelt mit <strong>Python</strong> und <strong>Discord.py</strong>. Integriert mehrere KI-APIs und verwendet <strong>TensorFlow</strong> für benutzerdefinierte Modellinferenz. Verfügt über eine modulare Plugin-Architektur für neue KI-Fähigkeiten.</p>')
    html = html.replace(
        '<p>This project deepened my understanding of AI/ML integration in production applications. I learned about prompt engineering, API rate limiting, managing model inference costs, and building user-friendly interfaces for complex AI features.</p>',
        '<p>Dieses Projekt vertiefte mein Verständnis der KI/ML-Integration. Ich lernte Prompt-Engineering, API-Rate-Limiting, die Verwaltung von Modellinferenz-Kosten und den Aufbau benutzerfreundlicher Oberflächen für komplexe KI-Funktionen.</p>')
    html = html.replace(
        '<p>Tharos is a versatile Discord bot designed to enhance server communities with moderation tools, fun commands, and utility features. Built with Python and the Discord.py library.</p>',
        '<p>Tharos ist ein vielseitiger Discord-Bot, der Server-Communities mit Moderations-Tools, Spaß-Befehlen und Dienstprogramm-Funktionen bereichert. Entwickelt mit Python und der Discord.py-Bibliothek.</p>')
    html = html.replace('<li><strong>Moderation</strong> – Kick, ban, mute, and warn commands with audit logging</li>',
        '<li><strong>Moderation</strong> – Kick-, Ban-, Mute- und Warn-Befehle mit Audit-Logging</li>')
    html = html.replace('<li><strong>Custom Commands</strong> – Server admins can create custom text responses</li>',
        '<li><strong>Eigene Befehle</strong> – Server-Admins können benutzerdefinierte Textantworten erstellen</li>')
    html = html.replace('<li><strong>Leveling System</strong> – XP-based leveling with role rewards and leaderboards</li>',
        '<li><strong>Level-System</strong> – XP-basiertes Leveling mit Rollen-Belohnungen und Bestenlisten</li>')
    html = html.replace('<li><strong>Music Playback</strong> – Stream music from YouTube directly in voice channels</li>',
        '<li><strong>Musikwiedergabe</strong> – Streame Musik direkt von YouTube in Sprachkanäle</li>')
    html = html.replace('<li><strong>Utility Tools</strong> – Polls, reminders, server stats, and user info commands</li>',
        '<li><strong>Hilfsprogramme</strong> – Umfragen, Erinnerungen, Server-Statistiken und Nutzerinfo-Befehle</li>')
    html = html.replace(
        '<p>Written in <strong>Python</strong> using the <strong>Discord.py</strong> library for the Discord API. Uses <strong>SQLite</strong> for persistent data storage including user levels, server settings, and moderation logs. Hosted on a Linux VPS with systemd for automatic restarts.</p>',
        '<p>Geschrieben in <strong>Python</strong> mit der <strong>Discord.py</strong>-Bibliothek. Verwendet <strong>SQLite</strong> für persistente Datenspeicherung. Gehostet auf einem Linux-VPS mit systemd für automatische Neustarts.</p>')
    html = html.replace(
        '<p>Building Tharos was my introduction to asynchronous programming in Python. I learned about event-driven architecture, rate limiting, database design, and how to build reliable services that run 24/7.</p>',
        '<p>Der Aufbau von Tharos war mein Einstieg in die asynchrone Programmierung in Python. Ich lernte ereignisgesteuerte Architektur, Rate-Limiting, Datenbankdesign und den Aufbau zuverlässiger Dienste, die rund um die Uhr laufen.</p>')
    # article section headings
    html = html.replace('<h2 id="features">Features</h2>', '<h2 id="funktionen">Funktionen</h2>')
    html = html.replace('<h2 id="highlights">Highlights</h2>', '<h2 id="highlights">Highlights</h2>')
    html = html.replace('<h2 id="what-i-learned">What I Learned</h2>', '<h2 id="was-ich-gelernt-habe">Was ich gelernt habe</h2>')
    html = html.replace('<h2 id="tech-stack">Tech Stack</h2>', '<h2 id="tech-stack">Tech Stack</h2>')
    return html

# ─────────────────────────────────────────────
# 1. Main index.html
# ─────────────────────────────────────────────
def transform_index():
    src = os.path.join(BASE, 'index.html')
    dst = os.path.join(BASE, 'de', 'index.html')
    html = read_file(src)

    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_meta_urls(html, 'https://danieldietrich.tech/de/')
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)

    # Title & meta
    html = html.replace('<title>Home | Daniel Dietrich </title>', '<title>Startseite | Daniel Dietrich</title>')
    html = html.replace('content="Home | Daniel Dietrich"', 'content="Startseite | Daniel Dietrich"')
    html = html.replace('"name":"Home"', '"name":"Startseite"')
    html = html.replace('title="Home | Daniel Dietrich"', 'title="Startseite | Daniel Dietrich"')
    html = re.sub(r'<meta name="description" content="CS Student[^"]*">', '<meta name="description" content="Physik- und Management-Student aus Ulm. Entwickle Apps, Bots und Web-Anwendungen.">', html)
    html = re.sub(r'<meta property="og:description" content="Student from Ulm[^"]*">', '<meta property="og:description" content="Student aus Ulm, Deutschland.">', html)
    html = re.sub(r'<meta name="twitter:description" content="CS Student[^"]*">', '<meta name="twitter:description" content="Physik- und Management-Student aus Ulm. Entwickle Apps, Bots und Web-Anwendungen.">', html)
    html = html.replace('title="Home | Daniel Dietrich" href="https://danieldietrich.tech/rss.xml"',
                        'title="Startseite | Daniel Dietrich" href="https://danieldietrich.tech/rss.xml"')

    # Language switcher: in EN page there's just a DE link; in DE page we show EN → / and bold DE
    html = html.replace(
        '<a href="/de" class="font-semibold uppercase tracking-wider hover:text-black dark:hover:text-white blend" data-astro-cid-j7pv25f6> DE </a>',
        '<a href="/" class="uppercase tracking-wider hover:text-black dark:hover:text-white blend" data-astro-cid-j7pv25f6> EN </a> <span class="font-semibold uppercase tracking-wider" data-astro-cid-j7pv25f6>DE</span>'
    )

    # Header
    html = html.replace('> Physics and Management Student <', '> Physik und Management Student <')
    html = html.replace('> Ulm, Germany <', '> Ulm, Deutschland <')

    # Section headings
    html = html.replace('>About</h2>', '>Über mich</h2>')
    # Education heading with chevron arrow (clickable)
    html = html.replace('>Education <svg', '>Ausbildung <svg')
    # Education standalone heading
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

    # Tech stack text
    html = html.replace(
        'I regularly work with Python (NumPy/SciPy), MATLAB, Java, LaTeX, Git, Microsoft Office (Excel, Word &amp; PowerPoint), and AutoCAD for simulations, analysis, documentation, and projects.',
        'Ich arbeite regelmäßig mit Python (NumPy/SciPy), MATLAB, Java, LaTeX, Git, Microsoft Office (Excel, Word &amp; PowerPoint) und AutoCAD für Simulationen, Analysen, Dokumentationen und Projekte.')
    html = html.replace(
        'Languages: German – native, English – fluent (C2)',
        'Sprachen: Deutsch – Muttersprache, Englisch – fließend (C2)')

    # Experience short labels on resume view
    html = html.replace('>Freelance Software Engineer<', '>Freelance-Softwareentwickler<')
    html = html.replace('>Legal Intern<', '>Praktikant Rechtsanwaltskanzlei<')
    html = html.replace('>Private Tutor<', '>Nachhilfelehrer<')
    html = html.replace('>Physics and Mathematics<', '>Physik und Mathematik<')

    # Research projects on resume
    html = html.replace('>Research Study: Quantum Sensor Technology<', '>Forschungsstudie: Quantensensortechnologie<')
    html = html.replace(">Bachelor's Thesis: Construction of a TIRF Microscope<", '>Bachelorarbeit: Konstruktion eines TIRF-Mikroskops<')
    html = html.replace('> Relativistic Simulation of the Solar System <', '> Relativistische Simulation des Sonnensystems <')

    # Contact text
    html = html.replace('>Reach out to me via email or on LinkedIn.</p>', '>Kontaktiere mich per E-Mail oder auf LinkedIn.</p>')

    # Back buttons
    html = html.replace('> Back to resume <', '> Zurück zum Lebenslauf <')
    html = html.replace('> Back to projects <', '> Zurück zu den Projekten <')

    # Education detail view subtitle
    html = html.replace('> B.Sc. Computer Science &middot; Ulm University <', '> M.Sc. Physik und Management &middot; Universität Ulm <')
    html = html.replace('Oct 2024 - Present', 'Okt. 2024 – heute')
    html = html.replace('>Semester 3 of 4 completed · 90/120 LP<', '>Semester 3 von 4 abgeschlossen · 90/120 LP<')

    # Semester status badges
    html = html.replace('> completed <', '> abgeschlossen <')
    html = html.replace('> in progress <', '> laufend <')

    # Course names
    course_map = [
        ('> Foundations of Practical CS <', '> Grundlagen der Praktischen Informatik <'),
        ('> Foundations of Theoretical CS <', '> Grundlagen der Theoretischen Informatik <'),
        ('> Foundations of Computer Engineering <', '> Grundlagen der Technischen Informatik <'),
        ('> Mathematics for CS I <', '> Mathematik für Informatiker I <'),
        ('> Object-Oriented Programming <', '> Objektorientierte Programmierung <'),
        ('> Computer Architecture <', '> Rechnerarchitektur <'),
        ('> Operating Systems <', '> Betriebssysteme <'),
        ('> Mathematics for CS II <', '> Mathematik für Informatiker II <'),
        ('> Software Engineering <', '> Software Engineering <'),
        ('> Software Project Part 1 <', '> Softwareprojekt Teil 1 <'),
        ('> Algorithms &amp; Data Structures <', '> Algorithmen &amp; Datenstrukturen <'),
        ('> Networked Systems <', '> Vernetzte Systeme <'),
        ('> Applied Numerical Methods <', '> Angewandte Numerische Methoden <'),
        ('> Software Project Part 2 <', '> Softwareprojekt Teil 2 <'),
        ('> Human-Computer Interaction <', '> Mensch-Computer-Interaktion <'),
        ('> Logic <', '> Logik <'),
        ('> Computability &amp; Complexity <', '> Berechenbarkeit &amp; Komplexität <'),
        ('> Applied Stochastics <', '> Angewandte Stochastik <'),
        ('> Supplementary Module <', '> Ergänzungsmodul <'),
        ('> Databases &amp; Information Systems <', '> Datenbanken &amp; Informationssysteme <'),
        ('> AI &amp; Neuroinformatics <', '> KI &amp; Neuroinformatik <'),
        ('> Seminar <', '> Seminar <'),
        ('> Elective Specialization <', '> Wahlpflicht Vertiefung <'),
        ('> CS &amp; Society <', '> Informatik &amp; Gesellschaft <'),
        ('> Empirical Research Methods <', '> Empirische Forschungsmethoden <'),
        ('> IT Security <', '> IT-Sicherheit <'),
        ('> Bachelor&#39;s Thesis <', '> Bachelorarbeit <'),
    ]
    for en, de in course_map:
        html = html.replace(en, de)

    # Course categories
    html = html.replace('>Practical CS<', '>Praktische Informatik<')
    html = html.replace('>Theoretical CS<', '>Theoretische Informatik<')
    html = html.replace('>Computer Engineering<', '>Technische Informatik<')
    html = html.replace('>Mathematics<', '>Mathematik<')
    html = html.replace('>Supplementary<', '>Ergänzung<')
    html = html.replace('>Specialization<', '>Vertiefung<')
    html = html.replace('>Key Qualifications<', '>Schlüsselqualifikationen<')
    html = html.replace('>Seminar<', '>Seminar<')
    html = html.replace('>Thesis<', '>Abschlussarbeit<')

    # Experience expanded view
    html = html.replace('> Jan 2024 – Current <', '> Jan. 2024 – heute <')
    html = html.replace('Jan 2024 – Current', 'Jan. 2024 – heute')
    html = html.replace('Mar 2023 – Sep 2023', 'März 2023 – Sep 2023')
    html = html.replace('<p>Working as a freelancer ersetzen on UpWork, delivering custom web and mobile applications for clients across various industries. Specializing in React, Next.js, and Flutter development.</p>',
        '<p>Als Freelancer auf UpWork tätig, entwickle ich maßgeschneiderte Web- und Mobile-Anwendungen für Kunden verschiedener Branchen. Schwerpunkte: React, Next.js und Flutter.</p>')
    html = html.replace('<p>Working as a freelance developer on UpWork, delivering custom web and mobile applications for clients across various industries. Specializing in React, Next.js, and Flutter development.</p>',
        '<p>Als Freelancer auf UpWork tätig, entwickle ich maßgeschneiderte Web- und Mobile-Anwendungen für Kunden verschiedener Branchen. Schwerpunkte: React, Next.js und Flutter.</p>')
    html = html.replace('Freelance Full-Stack Developer', 'Freelance Full-Stack Entwickler')
    html = html.replace('Software Engineering Intern', 'Praktikant Softwareentwicklung')
    html = html.replace('>Places I have worked.</p>', '>Arbeitsstationen im Überblick.</p>')
    html = html.replace(
        '<p>Worked as a software engineering intern at Cerence, a global leader in AI-powered automotive solutions. Contributed to the development of voice-assistant and conversational AI technologies used by major car manufacturers worldwide.</p>',
        '<p>Praktikum als Softwareentwickler bei Cerence, einem globalen Marktführer für KI-gestützte Automotive-Lösungen. Mitarbeit an der Entwicklung von Sprachassistenz- und Conversational-AI-Technologien für führende Automobilhersteller weltweit.</p>')

    # Projects expanded view
    html = html.replace('>Apps, bots, and tools I have built.</p>', '>Apps, Bots und Tools, die ich entwickelt habe.</p>')

    # Footer links text (after body links were updated to /de/ paths)
    html = html.replace('> Terms <', '> Nutzungsbedingungen <')
    html = html.replace('> Privacy <', '> Datenschutz <')

    write_file(dst, html)
    print(f'Written: {dst}')

# ─────────────────────────────────────────────
# 2. work/index.html
# ─────────────────────────────────────────────
def transform_work():
    src = os.path.join(BASE, 'work', 'index.html')
    dst = os.path.join(BASE, 'de', 'work', 'index.html')
    html = read_file(src)

    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_meta_urls(html, 'https://danieldietrich.tech/de/work/')
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)

    # Hreflang & canonical use jannisdietrich.com – update to danieldietrich.tech
    html = html.replace('https://jannisdietrich.com/work/', 'https://danieldietrich.tech/work/')
    html = html.replace('https://jannisdietrich.com/de/work/', 'https://danieldietrich.tech/de/work/')
    html = html.replace('https://jannisdietrich.com/', 'https://danieldietrich.tech/')
    html = html.replace('https://jannisdietrich.com', 'https://danieldietrich.tech')

    # Fix canonical / og:url / twitter:url again after domain fix (already set by replace_meta_urls with original URL)
    # re-apply to make sure they point to /de/work/
    html = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://danieldietrich.tech/de/work/">', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="https://danieldietrich.tech/de/work/">', html)
    html = re.sub(r'<meta name="twitter:url" content="[^"]*">', '<meta name="twitter:url" content="https://danieldietrich.tech/de/work/">', html)

    # Titles
    html = re.sub(r'<title>Work \| [^<]*</title>', '<title>Arbeit | Daniel Dietrich</title>', html)
    html = re.sub(r'content="Work \| [^"]*"', 'content="Arbeit | Daniel Dietrich"', html)
    html = re.sub(r'<meta name="description" content="Places I have worked[^"]*">', '<meta name="description" content="Orte, an denen ich gearbeitet habe.">', html)
    html = re.sub(r'<meta property="og:description" content="Places I have worked[^"]*">', '<meta property="og:description" content="Orte, an denen ich gearbeitet habe.">', html)
    html = re.sub(r'<meta name="twitter:description" content="Places I have worked[^"]*">', '<meta name="twitter:description" content="Orte, an denen ich gearbeitet habe.">', html)
    html = html.replace('"name":"Work"', '"name":"Arbeit"')

    # Body
    html = html.replace('> Work <', '> Arbeit <')
    html = html.replace('>Places I have worked.</p>', '>Orte, an denen ich gearbeitet habe.</p>')
    html = html.replace('Jan 2024 - Current', 'Jan. 2024 – heute')
    html = html.replace('Mar 2023 - Sep 2023', 'März 2023 – Sep. 2023')
    html = html.replace('Freelance Full-Stack Developer', 'Freelance Full-Stack Entwickler')
    html = html.replace('Software Engineering Intern', 'Praktikant Softwareentwicklung')
    html = html.replace(
        '<p>Working as a freelance developer on UpWork, delivering custom web and mobile applications for clients across various industries. Specializing in React, Next.js, and Flutter development.</p>',
        '<p>Als Freelancer auf UpWork tätig, entwickle ich maßgeschneiderte Web- und Mobile-Anwendungen für Kunden verschiedener Branchen. Schwerpunkte: React, Next.js und Flutter.</p>')
    html = html.replace(
        '<p>Worked as a software engineering intern at Cerence, a global leader in AI-powered automotive solutions. Contributed to the development of voice-assistant and conversational AI technologies used by major car manufacturers worldwide.</p>',
        '<p>Praktikum als Softwareentwickler bei Cerence, einem globalen Marktführer für KI-gestützte Automotive-Lösungen. Mitarbeit an der Entwicklung von Sprachassistenz- und Conversational-AI-Technologien für führende Automobilhersteller weltweit.</p>')

    html = html.replace('> Terms <', '> Nutzungsbedingungen <')
    html = html.replace('> Privacy <', '> Datenschutz <')

    write_file(dst, html)
    print(f'Written: {dst}')

# ─────────────────────────────────────────────
# 3. projects/index.html
# ─────────────────────────────────────────────
def transform_projects():
    src = os.path.join(BASE, 'projects', 'index.html')
    dst = os.path.join(BASE, 'de', 'projects', 'index.html')
    html = read_file(src)

    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)

    # Domain fix
    html = html.replace('https://jannisdietrich.com/', 'https://danieldietrich.tech/')
    html = html.replace('https://jannisdietrich.com', 'https://danieldietrich.tech')

    html = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://danieldietrich.tech/de/projects/">', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="https://danieldietrich.tech/de/projects/">', html)
    html = re.sub(r'<meta name="twitter:url" content="[^"]*">', '<meta name="twitter:url" content="https://danieldietrich.tech/de/projects/">', html)

    html = re.sub(r'<title>Projects \| [^<]*</title>', '<title>Projekte | Daniel Dietrich</title>', html)
    html = re.sub(r'content="Projects \| [^"]*"', 'content="Projekte | Daniel Dietrich"', html)
    html = re.sub(r'<meta name="description" content="Apps, bots[^"]*">', '<meta name="description" content="Apps, Bots und Tools, die ich entwickelt habe.">', html)
    html = re.sub(r'<meta property="og:description" content="Apps, bots[^"]*">', '<meta property="og:description" content="Apps, Bots und Tools, die ich entwickelt habe.">', html)
    html = re.sub(r'<meta name="twitter:description" content="Apps, bots[^"]*">', '<meta name="twitter:description" content="Apps, Bots und Tools, die ich entwickelt habe.">', html)
    html = html.replace('"name":"Projects"', '"name":"Projekte"')

    html = html.replace('> Projects <', '> Projekte <')
    html = html.replace('> Apps, bots, and tools I have built. <', '> Apps, Bots und Tools, die ich entwickelt habe. <')

    html = html.replace('> Terms <', '> Nutzungsbedingungen <')
    html = html.replace('> Privacy <', '> Datenschutz <')

    write_file(dst, html)
    print(f'Written: {dst}')

# ─────────────────────────────────────────────
# Helper: transform a project sub-page
# ─────────────────────────────────────────────
def transform_project_page(slug, en_title_de, en_desc_de, de_url, en_path_part):
    src = os.path.join(BASE, 'projects', slug, 'index.html')
    dst = os.path.join(BASE, 'de', 'projects', slug, 'index.html')
    html = read_file(src)

    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)

    # Domain fix
    html = html.replace('https://jannisdietrich.com/', 'https://danieldietrich.tech/')
    html = html.replace('https://jannisdietrich.com', 'https://danieldietrich.tech')

    html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{de_url}">', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{de_url}">', html)
    html = re.sub(r'<meta name="twitter:url" content="[^"]*">', f'<meta name="twitter:url" content="{de_url}">', html)

    # Title
    html = re.sub(r'<title>[^|]*\| [^<]*</title>', f'<title>{en_title_de} | Daniel Dietrich</title>', html)
    html = re.sub(r'<meta name="title" content="[^|]*\|[^"]*">', f'<meta name="title" content="{en_title_de} | Daniel Dietrich">', html)
    html = re.sub(r'<meta property="og:title" content="[^|]*\|[^"]*">', f'<meta property="og:title" content="{en_title_de} | Daniel Dietrich">', html)
    html = re.sub(r'<meta name="twitter:title" content="[^|]*\|[^"]*">', f'<meta name="twitter:title" content="{en_title_de} | Daniel Dietrich">', html)
    html = re.sub(r'<meta property="og:image:alt" content="[^|]*\|[^"]*">', f'<meta property="og:image:alt" content="{en_title_de} | Daniel Dietrich">', html)
    html = re.sub(r'<meta name="twitter:image:alt" content="[^|]*\|[^"]*">', f'<meta name="twitter:image:alt" content="{en_title_de} | Daniel Dietrich">', html)
    # Description
    html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{en_desc_de}">', html, count=1)
    html = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{en_desc_de}">', html, count=1)
    html = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{en_desc_de}">', html, count=1)
    # Breadcrumb name
    html = html.replace(f'"name":"{en_path_part}"', f'"name":"{en_title_de}"')

    # Back link text
    html = html.replace('&larr; Back Projects', '&larr; Zurück zu Projekte')

    html = html.replace('> Terms <', '> Nutzungsbedingungen <')
    html = html.replace('> Privacy <', '> Datenschutz <')

    write_file(dst, html)
    print(f'Written: {dst}')

# ─────────────────────────────────────────────
# Legal pages
# ─────────────────────────────────────────────
def transform_legal_privacy():
    src = os.path.join(BASE, 'legal', 'privacy', 'index.html')
    dst = os.path.join(BASE, 'de', 'legal', 'privacy', 'index.html')
    html = read_file(src)

    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)

    html = html.replace('https://jannisdietrich.com/', 'https://danieldietrich.tech/')
    html = html.replace('https://jannisdietrich.com', 'https://danieldietrich.tech')

    html = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://danieldietrich.tech/de/legal/privacy/">', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="https://danieldietrich.tech/de/legal/privacy/">', html)
    html = re.sub(r'<meta name="twitter:url" content="[^"]*">', '<meta name="twitter:url" content="https://danieldietrich.tech/de/legal/privacy/">', html)

    html = re.sub(r'<title>Privacy Policy \| [^<]*</title>', '<title>Datenschutzerklärung | Daniel Dietrich</title>', html)
    html = re.sub(r'content="Privacy Policy \| [^"]*"', 'content="Datenschutzerklärung | Daniel Dietrich"', html)
    html = re.sub(r'<meta name="description" content="Privacy Policy[^"]*">', '<meta name="description" content="Datenschutzerklärung für Daniel Dietrich">', html)
    html = re.sub(r'<meta property="og:description" content="Privacy Policy[^"]*">', '<meta property="og:description" content="Datenschutzerklärung für Daniel Dietrich">', html)
    html = re.sub(r'<meta name="twitter:description" content="Privacy Policy[^"]*">', '<meta name="twitter:description" content="Datenschutzerklärung für Daniel Dietrich">', html)
    html = html.replace('"name":"Privacy Policy"', '"name":"Datenschutzerklärung"')

    # Body translations
    html = html.replace('> Privacy Policy <', '> Datenschutzerklärung <')
    html = html.replace('Last updated: Mar 07, 2024', 'Zuletzt aktualisiert: 07. März 2024')
    html = html.replace(
        '<p>This Privacy Policy governs the manner in which [Your Company Name] collects, uses, maintains, and discloses information collected from users (each, a "User") of the [Your Website URL] website ("Site"). This privacy policy applies to the Site and all products and services offered by [Your Company Name].</p>',
        '<p>Diese Datenschutzerklärung regelt den Umgang mit personenbezogenen Daten, die von Nutzern der Website danieldietrich.tech erhoben werden.</p>')
    html = html.replace('<h4 id="personal-identification-information">Personal identification information</h4>',
        '<h4 id="personenbezogene-daten">Personenbezogene Daten</h4>')
    html = html.replace('<h4 id="non-personal-identification-information">Non-personal identification information</h4>',
        '<h4 id="nicht-personenbezogene-daten">Nicht-personenbezogene Daten</h4>')
    html = html.replace('<h4 id="web-browser-cookies">Web browser cookies</h4>',
        '<h4 id="cookies">Web-Browser-Cookies</h4>')
    html = html.replace('<h4 id="how-we-use-collected-information">How we use collected information</h4>',
        '<h4 id="verwendung-der-daten">Verwendung erhobener Daten</h4>')
    html = html.replace('<h4 id="how-we-protect-your-information">How we protect your information</h4>',
        '<h4 id="datenschutz">Schutz Ihrer Daten</h4>')
    html = html.replace('<h4 id="sharing-your-personal-information">Sharing your personal information</h4>',
        '<h4 id="weitergabe-von-daten">Weitergabe Ihrer Daten</h4>')
    html = html.replace('<h4 id="changes-to-this-privacy-policy">Changes to this privacy policy</h4>',
        '<h4 id="aenderungen">Änderungen dieser Datenschutzerklärung</h4>')

    html = html.replace('> Terms <', '> Nutzungsbedingungen <')
    html = html.replace('> Privacy <', '> Datenschutz <')

    write_file(dst, html)
    print(f'Written: {dst}')

def transform_legal_terms():
    src = os.path.join(BASE, 'legal', 'terms', 'index.html')
    dst = os.path.join(BASE, 'de', 'legal', 'terms', 'index.html')
    html = read_file(src)

    html = html.replace('<html lang="en">', '<html lang="de">')
    html = replace_locale(html)
    html = update_body_links(html)
    html = translate_common(html)

    html = html.replace('https://jannisdietrich.com/', 'https://danieldietrich.tech/')
    html = html.replace('https://jannisdietrich.com', 'https://danieldietrich.tech')

    html = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://danieldietrich.tech/de/legal/terms/">', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="https://danieldietrich.tech/de/legal/terms/">', html)
    html = re.sub(r'<meta name="twitter:url" content="[^"]*">', '<meta name="twitter:url" content="https://danieldietrich.tech/de/legal/terms/">', html)

    html = re.sub(r'<title>Terms of Use \| [^<]*</title>', '<title>Nutzungsbedingungen | Daniel Dietrich</title>', html)
    html = re.sub(r'content="Terms of Use \| [^"]*"', 'content="Nutzungsbedingungen | Daniel Dietrich"', html)
    html = re.sub(r'<meta name="description" content="Terms of Use[^"]*">', '<meta name="description" content="Nutzungsbedingungen für Daniel Dietrich">', html)
    html = re.sub(r'<meta property="og:description" content="Terms of Use[^"]*">', '<meta property="og:description" content="Nutzungsbedingungen für Daniel Dietrich">', html)
    html = re.sub(r'<meta name="twitter:description" content="Terms of Use[^"]*">', '<meta name="twitter:description" content="Nutzungsbedingungen für Daniel Dietrich">', html)
    html = html.replace('"name":"Terms of Use"', '"name":"Nutzungsbedingungen"')

    html = html.replace('> Terms of Use <', '> Nutzungsbedingungen <')
    html = html.replace('Last updated: Mar 07, 2024', 'Zuletzt aktualisiert: 07. März 2024')
    html = html.replace(
        '<p>Please read these Terms of Use ("Terms", "Terms of Use") carefully before using the [Your Website URL] website (the "Service") operated by [Your Company Name] ("us", "we", or "our").</p>',
        '<p>Bitte lesen Sie diese Nutzungsbedingungen sorgfältig durch, bevor Sie die Website danieldietrich.tech nutzen.</p>')
    html = html.replace('<h4 id="agreement-to-terms">Agreement to Terms</h4>',
        '<h4 id="zustimmung-zu-bedingungen">Zustimmung zu den Bedingungen</h4>')
    html = html.replace('<h4 id="intellectual-property-rights">Intellectual Property Rights</h4>',
        '<h4 id="geistiges-eigentum">Geistige Eigentumsrechte</h4>')
    html = html.replace('<h4 id="user-representations">User Representations</h4>',
        '<h4 id="nutzererklarungen">Nutzererklärungen</h4>')
    html = html.replace('<h4 id="links-to-other-websites">Links to Other Websites</h4>',
        '<h4 id="links-zu-anderen-websites">Links zu anderen Websites</h4>')
    html = html.replace('<h4 id="termination">Termination</h4>',
        '<h4 id="kuendigung">Kündigung</h4>')
    html = html.replace('<h4 id="governing-law">Governing Law</h4>',
        '<h4 id="anwendbares-recht">Anwendbares Recht</h4>')
    html = html.replace('<h4 id="changes-to-these-terms-of-use">Changes to These Terms of Use</h4>',
        '<h4 id="aenderungen-der-nutzungsbedingungen">Änderungen der Nutzungsbedingungen</h4>')

    html = html.replace('> Terms <', '> Nutzungsbedingungen <')
    html = html.replace('> Privacy <', '> Datenschutz <')

    write_file(dst, html)
    print(f'Written: {dst}')

# ─────────────────────────────────────────────
# Run all transformations
# ─────────────────────────────────────────────
if __name__ == '__main__':
    transform_index()
    transform_work()
    transform_projects()

    # Project sub-pages
    transform_project_page(
        'resumeme',
        'ResumeMe – Web-App',
        'Eine Webanwendung, die Nutzern hilft, professionelle Lebensläufe mit anpassbaren Vorlagen, Live-Vorschau und KI-gestützten Verbesserungsvorschlägen zu erstellen.',
        'https://danieldietrich.tech/de/projects/resumeme/',
        'ResumeMe \u2013 Web App'
    )
    transform_project_page(
        'tharos-discord-bot',
        'Tharos – Discord Bot',
        'Ein funktionsreicher Discord-Bot für Server-Verwaltung und Unterhaltung – mit Moderations-Tools, XP-Leveling, Musikwiedergabe und benutzerdefinierten Befehlen.',
        'https://danieldietrich.tech/de/projects/tharos-discord-bot/',
        'Tharos \u2013 Discord Bot'
    )
    transform_project_page(
        'freeai-discord-bot',
        'FreeAI – KI Discord Bot',
        'Ein KI-gesteuerter Discord-Bot, der Sprachmodelle und Bildgenerierung in Server bringt – mit Kontextgedächtnis, Rate-Limiting und modularem Plugin-System.',
        'https://danieldietrich.tech/de/projects/freeai-discord-bot/',
        'FreeAI \u2013 AI Discord Bot'
    )
    transform_project_page(
        'shoply-landing-page',
        'Shoply Landing Page',
        'Eine moderne Marketing-Website für die Shoply-App mit interaktiven 3D-Telefon-Mockups, sanften Scroll-Animationen und optimierter Performance.',
        'https://danieldietrich.tech/de/projects/shoply-landing-page/',
        'Shoply Landing Page'
    )
    transform_project_page(
        'shoply-app',
        'Shoply – Kollaborative Shopping-App',
        'Eine plattformübergreifende mobile App für gemeinsames Einkaufen mit Echtzeit-Synchronisierung, smarten Kategorien und Offline-Unterstützung. Verfügbar auf iOS und Android.',
        'https://danieldietrich.tech/de/projects/shoply-app/',
        'Shoply \u2013 Collaborative Shopping App'
    )
    transform_project_page(
        'studyapp',
        'StudyApp – Lernbegleiter',
        'Ein mobiler Lernbegleiter mit React Native und Expo – mit Spaced-Repetition-Karteikarten, Lernplanung und Fortschrittsverfolgung.',
        'https://danieldietrich.tech/de/projects/studyapp/',
        'StudyApp \u2013 Learning Companion'
    )

    transform_legal_privacy()
    transform_legal_terms()

    print('\nAll done!')
