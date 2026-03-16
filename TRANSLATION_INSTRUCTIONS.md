# German HTML Translation - Instructions

## Overview
This task involves translating all English HTML pages on the danieldietrich.tech website to German versions.

## Files to Use

There are multiple translation scripts available in your project directory:

### Primary Script (Recommended)
- **`translate_now.py`** - The recommended script. Most comprehensive and up-to-date.

### Alternative Scripts
- `translate_final.py` - Also comprehensive
- `translate_de.py` - Original script (may need updates for Daniel vs Jannis)
- `translate_all.py` - Another comprehensive version

## How to Run

### Option 1: Windows Command Prompt or PowerShell
```batch
cd c:\Users\Fo\Documents\danieldietrich.tech
python translate_now.py
```

or

```batch
python3 translate_now.py
```

### Option 2: Using the provided batch file
```batch
translate.bat
```

or double-click `translate.bat` from File Explorer.

## What the Script Does

The `translate_now.py` script will:

1. **Read all 11 English HTML source files**:
   - index.html (homepage)
   - work/index.html
   - projects/index.html
   - projects/resumeme/index.html
   - projects/tharos-discord-bot/index.html
   - projects/freeai-discord-bot/index.html
   - projects/shoply-landing-page/index.html
   - projects/shoply-app/index.html
   - projects/studyapp/index.html
   - legal/privacy/index.html
   - legal/terms/index.html

2. **Create German translations** by:
   - Changing `lang="en"` to `lang="de"`
   - Updating meta tags (canonical, og:url, twitter:url) to use `/de/` paths
   - Swapping `og:locale` from `en_US` to `de_DE`
   - Translating all visible text content to German
   - Updating internal links from `/path/` to `/de/path/`
   - Fixing name/author references from "Jannis" to "Daniel"
   - Fixing domain from "jannisdietrich.com" to "danieldietrich.tech"

3. **Write German files** to:
   - de/index.html
   - de/work/index.html
   - de/projects/index.html
   - de/projects/resumeme/index.html
   - de/projects/tharos-discord-bot/index.html
   - de/projects/freeai-discord-bot/index.html
   - de/projects/shoply-landing-page/index.html
   - de/projects/shoply-app/index.html
   - de/projects/studyapp/index.html
   - de/legal/privacy/index.html
   - de/legal/terms/index.html

## Requirements

- **Python 3.6+** (or Python 2.7+)
- **No external dependencies** - The script uses only Python's built-in `os`, `re`, and `sys` modules

## Success Indicators

When you run the script, you should see:

```
======================================================================
German HTML Translation
======================================================================

✓ Created: c:\Users\Fo\Documents\danieldietrich.tech\de\index.html
✓ Created: c:\Users\Fo\Documents\danieldietrich.tech\de\work\index.html
✓ Created: c:\Users\Fo\Documents\danieldietrich.tech\de\projects\index.html
✓ Created: c:\Users\Fo\Documents\danieldietrich.tech\de\projects\resumeme\index.html
✓ Created: c:\Users\Fo\Documents\danieldietrich.tech\de\projects\tharos-discord-bot\index.html
✓ Created: c:\Users\Fo\Documents\danieldietrich.tech\de\projects\freeai-discord-bot\index.html
✓ Created: c:\Users\Fo\Documents\danieldietrich.tech\de\projects\shoply-landing-page\index.html
✓ Created: c:\Users\Fo\Documents\danieldietrich.tech\de\projects\shoply-app\index.html
✓ Created: c:\Users\Fo\Documents\danieldietrich.tech\de\projects\studyapp\index.html
✓ Created: c:\Users\Fo\Documents\danieldietrich.tech\de\legal\privacy\index.html
✓ Created: c:\Users\Fo\Documents\danieldietrich.tech\de\legal\terms\index.html

======================================================================
Translation Complete: 11/11 files translated
======================================================================
```

## Troubleshooting

### "python: command not found"
Try using `python3` instead:
```batch
python3 translate_now.py
```

### "No such file or directory"
Make sure you're in the correct directory:
```batch
cd c:\Users\Fo\Documents\danieldietrich.tech
```

### Encoding errors
The script explicitly uses UTF-8 encoding, so this shouldn't happen. If it does, try running from a terminal that supports UTF-8.

## Verification

After running the script, verify the results:

1. Check that `/de/` directory exists and contains all subdirectories
2. Check that all 11 HTML files were created in `/de/` and its subdirectories
3. Open a German file (e.g., `/de/index.html`) in a text editor
4. Verify:
   - `lang="de"` is present
   - Canonical URL contains `/de/`
   - Text is in German (e.g., "Über mich", "Projekte", etc.)
   - Internal links point to `/de/` paths

## Manual Verification Checklist

After running the script:

```
[ ] de/index.html exists
[ ] de/work/index.html exists  
[ ] de/projects/index.html exists
[ ] de/projects/resumeme/index.html exists
[ ] de/projects/tharos-discord-bot/index.html exists
[ ] de/projects/freeai-discord-bot/index.html exists
[ ] de/projects/shoply-landing-page/index.html exists
[ ] de/projects/shoply-app/index.html exists
[ ] de/projects/studyapp/index.html exists
[ ] de/legal/privacy/index.html exists
[ ] de/legal/terms/index.html exists

[ ] All files contain lang="de"
[ ] All files have /de/ in canonical URLs
[ ] German text visible in content
[ ] og:locale set to de_DE
```

## Questions?

The script is self-documenting. For more details, see the header comments in `translate_now.py`.
