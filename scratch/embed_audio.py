import re

with open("GoogleFlow_B12_B14_Kit.html", "r", encoding="utf-8") as f:
    html_content = f.read()

def add_audio(match):
    full = match.group(0)
    kf_path = match.group(2)
    audio_path = kf_path.replace("keyframes", "audio").replace(".png", ".mp3")
    audio_player = (
        '\n            <div style="margin-top: 10px;">\n'
        '              <label style="font-size: 11px; color: #94a3b8; display: block; margin-bottom: 4px;">🔊 Lời thoại AI:</label>\n'
        f'              <audio controls style="width: 100%; height: 32px; border-radius: 6px;" src="{audio_path}"></audio>\n'
        '            </div>'
    )
    return full + audio_player

new_html = re.sub(r'(<div class="keyframe-box">[\s\S]*?<img src="([^"]+)"[\s\S]*?</div>)', add_audio, html_content)

with open("GoogleFlow_B12_B14_Kit.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Updated GoogleFlow_B12_B14_Kit.html with embedded audio players!")
