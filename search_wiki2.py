import urllib.request
import json

queries = [
    "Vietnamese student",
    "Asian girl portrait glasses",
    "female student portrait",
    "Vietnamese high school",
    "Asian female portrait glasses"
]

for q in queries:
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=8&prop=imageinfo&iiprop=url|size|mime|extmetadata&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'PhysicsEduTool/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            d = json.loads(resp.read().decode())
            pages = d.get('query', {}).get('pages', {})
            print(f"=== Results for: {q} ({len(pages)} hits) ===")
            for pid, p in pages.items():
                ii = p.get('imageinfo', [{}])[0]
                w, h = ii.get('width', 0), ii.get('height', 0)
                if ii.get('mime') in ['image/jpeg', 'image/png'] and w > 800:
                    print(f"  {p.get('title')} [{w}x{h}] -> {ii.get('url')}")
    except Exception as e:
        print(f"Error {q}: {e}")
