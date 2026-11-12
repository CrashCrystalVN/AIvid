import os
import urllib.request

DEST_DIR = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\scratch\downloads"
os.makedirs(DEST_DIR, exist_ok=True)

urls = {
    "galileo_ramp.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Piano_inclinato%2C_Museo_Galileo%2C_Florence%2C_Inv._104%2C_224108.jpg",
    "voyager_model.png": "https://upload.wikimedia.org/wikipedia/commons/6/60/Voyager_spacecraft_model.png",
    "voyager_space.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/29/Voyager_spacecraft.jpg",
    "nebula_hubble.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/00/Crab_Nebula.jpg",
    "skateboard.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/74/Hippie_jump.jpg"
}

headers = {'User-Agent': 'PhysicsEduTool/1.0 (contact: student@edu.vn)'}

for fname, url in urls.items():
    fpath = os.path.join(DEST_DIR, fname)
    if os.path.exists(fpath) and os.path.getsize(fpath) > 10000:
        print(f"Already exists: {fname} ({os.path.getsize(fpath)} bytes)")
        continue
    print(f"Downloading {fname}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp, open(fpath, "wb") as out:
            out.write(resp.read())
        print(f"Saved {fname}: {os.path.getsize(fpath)} bytes")
    except Exception as e:
        print(f"Error downloading {fname}: {e}")

print("Download script complete.")
