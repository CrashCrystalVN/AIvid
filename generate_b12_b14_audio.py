import os
import sys
import json
from gtts import gTTS

def generate_tts(text, out_file):
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    tts = gTTS(text=text, lang="vi", slow=False)
    tts.save(out_file)
    return "gTTS"

def main():
    with open("master_plan_b12_b14.json", encoding="utf-8") as f:
        data = json.load(f)
    
    for v in data["videos"]:
        v_title = v["title"]
        prefix = "B12" if "12" in v_title else "B14"
        folder_name = "B12_ChuyenDongNem" if prefix == "B12" else "B14_DinhLuat1Newton"
        out_dir = os.path.join("audio", folder_name)
        os.makedirs(out_dir, exist_ok=True)
        print(f"\n=== Generating audio for {v_title} ===")
        
        for idx, s in enumerate(v["scenes"], 1):
            text = s["voiceover"]
            out_file = os.path.join(out_dir, f"s{idx}.mp3")
            title = s["title"]
            print(f"  Scene {idx}: {title[:35]}...", end="", flush=True)
            engine = generate_tts(text, out_file)
            sz = os.path.getsize(out_file) / 1024
            print(f" OK [{engine}, {sz:.1f} KB]")

if __name__ == "__main__":
    main()
    print("\nAll Bài 12 and Bài 14 audio generated successfully!")
