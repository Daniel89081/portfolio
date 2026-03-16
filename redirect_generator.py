import os

redirect_template = '<!DOCTYPE html><html><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url={url}"><link rel="canonical" href="{url}"><script>window.location.replace("{url}");</script></head><body></body></html>'

mappings = {
    r"c:\Users\Fo\Documents\danieldietrich.tech\de\index.html": "/",
    r"c:\Users\Fo\Documents\danieldietrich.tech\de\work\index.html": "/work/",
    r"c:\Users\Fo\Documents\danieldietrich.tech\de\projects\index.html": "/projects/",
    r"c:\Users\Fo\Documents\danieldietrich.tech\de\projects\resumeme\index.html": "/projects/resumeme/",
    r"c:\Users\Fo\Documents\danieldietrich.tech\de\projects\tharos-discord-bot\index.html": "/projects/tharos-discord-bot/",
    r"c:\Users\Fo\Documents\danieldietrich.tech\de\projects\freeai-discord-bot\index.html": "/projects/freeai-discord-bot/",
    r"c:\Users\Fo\Documents\danieldietrich.tech\de\projects\shoply-landing-page\index.html": "/projects/shoply-landing-page/",
    r"c:\Users\Fo\Documents\danieldietrich.tech\de\projects\shoply-app\index.html": "/projects/shoply-app/",
    r"c:\Users\Fo\Documents\danieldietrich.tech\de\projects\studyapp\index.html": "/projects/studyapp/",
    r"c:\Users\Fo\Documents\danieldietrich.tech\de\legal\privacy\index.html": "/legal/privacy/",
    r"c:\Users\Fo\Documents\danieldietrich.tech\de\legal\terms\index.html": "/legal/terms/",
}

for filepath, url in mappings.items():
    content = redirect_template.replace("{url}", url)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {filepath} -> {url}")

print("Done!")
