import urllib.request
import json

def search_wiki(q, limit=10):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit={limit}&prop=imageinfo&iiprop=url|size|mime&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'EduPhysicsTool/1.0 (contact: test@school.edu.vn)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            d = json.loads(resp.read().decode())
            pages = d.get('query', {}).get('pages', {})
            for pid, p in pages.items():
                ii = p.get('imageinfo', [{}])[0]
                if ii.get('mime') in ['image/jpeg', 'image/png'] and ii.get('width', 0) >= 1000:
                    print(f"{p.get('title')}: {ii.get('width')}x{ii.get('height')} -> {ii.get('url')}")
    except Exception as e:
        print('Error:', e)

print('--- Search 1: Vietnamese student ---')
search_wiki('Vietnamese high school student')
print('--- Search 2: Vietnamese girl glasses ---')
search_wiki('Vietnamese girl glasses')
print('--- Search 3: Asian student glasses ---')
search_wiki('Asian female student glasses')
