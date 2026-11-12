import urllib.request, urllib.parse, json

def search(q):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=5&prop=imageinfo&iiprop=url|size|mime&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'PhysicsEdu/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            pages = data.get('query', {}).get('pages', {})
            print(f"=== Results for: {q} ===")
            for pid, p in pages.items():
                ii = p.get('imageinfo', [{}])[0]
                if ii.get('mime') in ['image/jpeg', 'image/png'] and ii.get('width', 0) >= 1200:
                    print(f"{p.get('title')}: {ii.get('width')}x{ii.get('height')} -> {ii.get('url')}")
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    search('Basketball shot outdoor')
    search('Air track physics')
    search('Linear air track')
    search('Water fountain arc')
    search('Skateboard jump trick')
    search('Physics laboratory mechanics')
