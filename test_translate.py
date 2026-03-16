#!/usr/bin/env python3
# Test script to verify translate_de.py runs properly

import sys
import os

# Add the directory to path
sys.path.insert(0, r'c:\Users\Fo\Documents\danieldietrich.tech')

# Try importing and running
try:
    import translate_de
    print("✅ Successfully imported translate_de module")
    
    # Check if files exist
    base = r'c:\Users\Fo\Documents\danieldietrich.tech'
    source_files = [
        os.path.join(base, 'index.html'),
        os.path.join(base, 'work', 'index.html'),
        os.path.join(base, 'projects', 'index.html'),
        os.path.join(base, 'projects', 'resumeme', 'index.html'),
        os.path.join(base, 'projects', 'tharos-discord-bot', 'index.html'),
        os.path.join(base, 'projects', 'freeai-discord-bot', 'index.html'),
        os.path.join(base, 'projects', 'shoply-landing-page', 'index.html'),
        os.path.join(base, 'projects', 'shoply-app', 'index.html'),
        os.path.join(base, 'projects', 'studyapp', 'index.html'),
        os.path.join(base, 'legal', 'privacy', 'index.html'),
        os.path.join(base, 'legal', 'terms', 'index.html'),
    ]
    
    print("\n📋 Checking source files:")
    for f in source_files:
        exists = "✅" if os.path.exists(f) else "❌"
        print(f"  {exists} {f}")
    
    print("\n🚀 Running translation...")
    exec(open(r'c:\Users\Fo\Documents\danieldietrich.tech\translate_de.py').read())
    print("\n✅ Translation completed successfully!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
