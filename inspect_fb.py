import html
import re
import requests
import subprocess
import imageio_ffmpeg

raw = open("fb_page.html", encoding="utf-8", errors="ignore").read()
text = html.unescape(raw).replace(r"\/", "/")
mp4s = re.findall(r'https://[^\s"\'<>\\]+?\.mp4[^\s"\'<>\\]*', text)
print("MP4s found:", len(mp4s))
if mp4s:
    v_url = mp4s[0].encode('utf-8').decode('unicode_escape', errors='ignore')
    print("URL:", v_url[:120])
    r = requests.get(v_url, headers={"User-Agent": "Mozilla/5.0"}, stream=True)
    print("Status:", r.status_code)
    if r.status_code == 200:
        with open("fb_sample.mp4", "wb") as f:
            for chunk in r.iter_content(chunk_size=1024*256):
                if chunk:
                    f.write(chunk)
        print("Downloaded fb_sample.mp4")
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        for idx, sec in enumerate([1, 5, 12, 20, 35, 50]):
            subprocess.run([ffmpeg_exe, "-y", "-ss", str(sec), "-i", "fb_sample.mp4", "-frames:v", "1", f"fb_frame_{idx}.jpg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Extracted frames!")
