"""
RENDERER: BÀI 12 & BÀI 14 SMARTBOARD HYBRID PRESENTATION VIDEO
Render video thuyết trình Vật lí 10 Full HD 1080p @ 24fps chuẩn phong cách cô Nguyễn Bích Nhung:
  - Keyframes 16:9 sắc nét với chuyển động điện ảnh Ken Burns (zoom-in, pan-left, pan-right, zoom-out)
  - Giọng thuyết minh AI tiếng Việt từng cảnh nối tiếp mượt mà
  - Nhạc nền (BGM) du dương được tự động mix ở mức 15%
  - Bảng định danh MC Presenter Badge neon góc trái
  - Chỉ số tiến trình phân cảnh (Cảnh 1/5 -> Cảnh 5/5) góc phải
  - Hộp phụ đề nổi bật dạng kính mờ Dark Glass với viền phát sáng Neon Cyan
  - Hiệu ứng chuyển cảnh Crossfade mượt mà giữa các cảnh
"""

import os
import sys
import json
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

sys.stdout.reconfigure(encoding="utf-8")
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WIDTH, HEIGHT = 1920, 1080
FPS = 24
UP_W, UP_H = 2160, 1215

# Load fonts
font_badge = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
font_sub = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 28)
font_prog = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)

def get_audio_duration(p):
    res = subprocess.run([ffmpeg_exe, "-i", p], stderr=subprocess.PIPE, text=True)
    for line in res.stderr.split("\n"):
        if "Duration:" in line:
            parts = line.split("Duration:")[1].split(",")[0].strip().split(":")
            return float(parts[0])*3600 + float(parts[1])*60 + float(parts[2])
    return 15.0

def split_text_to_subtitles(text, max_chars=80):
    sentences = [s.strip() for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
    chunks = []
    current = ""
    for s in sentences:
        if len(current) + len(s) < max_chars:
            current = (current + " " + s).strip()
        else:
            if current:
                chunks.append(current)
            current = s
    if current:
        chunks.append(current)
    if not chunks:
        chunks = [text]
    return chunks

def render_lesson(lesson_key):
    with open("master_plan_b12_b14.json", encoding="utf-8") as f:
        plan = json.load(f)

    lesson_idx = 0 if lesson_key == "12" else 1
    v_data = plan["videos"][lesson_idx]
    v_title = v_data["title"]
    folder_name = "B12_ChuyenDongNem" if lesson_key == "12" else "B14_DinhLuat1Newton"
    short_title = "Bài 12: Chuyển động ném" if lesson_key == "12" else "Bài 14: Định luật 1 Newton"

    print(f"\n=======================================================")
    print(f"🎬 BẮT ĐẦU RENDER VIDEO: {v_title}")
    print(f"=======================================================")

    scenes_meta = []
    zoom_modes = ["in", "pan_right", "in", "pan_left", "out"]

    for idx, s in enumerate(v_data["scenes"], 1):
        img_path = os.path.join(BASE_DIR, "keyframes", folder_name, f"s{idx}.png")
        audio_path = os.path.join(BASE_DIR, "audio", folder_name, f"s{idx}.mp3")
        dur = get_audio_duration(audio_path)
        
        # Split voiceover text into proportional subtitles
        sub_texts = split_text_to_subtitles(s["voiceover"])
        num_subs = len(sub_texts)
        subs = []
        for s_i, sub_t in enumerate(sub_texts):
            p0 = s_i / num_subs
            p1 = (s_i + 1) / num_subs
            subs.append((p0, p1, sub_t))

        img = Image.open(img_path).convert("RGB")
        pil_img = img.resize((UP_W, UP_H), Image.Resampling.LANCZOS)

        scenes_meta.append({
            "idx": idx,
            "title": s["title"],
            "pil_img": pil_img,
            "duration": dur,
            "subs": subs,
            "zoom_mode": zoom_modes[(idx - 1) % len(zoom_modes)]
        })
        print(f"  Phân cảnh {idx}: {dur:.2f}s | {len(subs)} phụ đề | {s['title'][:40]}")

    # Set timeline
    cur_t = 0.0
    for sc in scenes_meta:
        sc["start_t"] = cur_t
        sc["end_t"] = cur_t + sc["duration"]
        cur_t = sc["end_t"]
    total_dur = cur_t
    total_frames = int(total_dur * FPS)
    print(f"\nTổng thời lượng: {total_dur:.2f}s ({total_frames} frames @ 24fps)")

    # Prepare audio mix with background music
    dir_audio = os.path.join(BASE_DIR, "audio", folder_name)
    concat_txt = os.path.join(dir_audio, "concat.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for i in range(1, 6):
            p = os.path.abspath(os.path.join(dir_audio, f"s{i}.mp3")).replace(chr(92), "/")
            f.write(f"file '{p}'\n")
    
    voice_track = os.path.join(dir_audio, "voice_concat.mp3")
    subprocess.run([ffmpeg_exe, "-y", "-f", "concat", "-safe", "0", "-i", concat_txt, "-c", "copy", voice_track],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    mixed_audio = os.path.join(dir_audio, "mixed_full_audio.mp3")
    bgm_path = os.path.join(BASE_DIR, "bg_music.wav")
    
    if os.path.exists(bgm_path):
        # Mix voiceover with ducked BGM (volume=0.15)
        cmd_mix = [
            ffmpeg_exe, "-y",
            "-i", voice_track,
            "-stream_loop", "-1", "-i", bgm_path,
            "-filter_complex",
            "[0:a]volume=1.0[v];[1:a]volume=0.15[m];[v][m]amix=inputs=2:duration=first:dropout_transition=2[a]",
            "-map", "[a]",
            "-c:a", "libmp3lame", "-b:a", "192k",
            mixed_audio
        ]
        subprocess.run(cmd_mix, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        final_audio_input = mixed_audio
    else:
        final_audio_input = voice_track

    # Setup video output
    out_dir = os.path.join(BASE_DIR, "output_videos")
    os.makedirs(out_dir, exist_ok=True)
    out_video = os.path.join(out_dir, f"Video_Bai{lesson_key}_{folder_name.split('_')[1]}.mp4")

    def render_scene_crop(sc, local_p):
        mode = sc["zoom_mode"]
        base = sc["pil_img"]
        if mode == "in":
            scale = 1.08 - 0.08 * local_p
            cw, ch = int(WIDTH * scale), int(HEIGHT * scale)
            x0 = (UP_W - cw) // 2
            y0 = (UP_H - ch) // 2
        elif mode == "out":
            scale = 1.00 + 0.08 * local_p
            cw, ch = int(WIDTH * scale), int(HEIGHT * scale)
            x0 = (UP_W - cw) // 2
            y0 = (UP_H - ch) // 2
        elif mode == "pan_right":
            cw, ch = int(WIDTH * 1.04), int(HEIGHT * 1.04)
            max_dx = UP_W - cw
            x0 = int(max_dx * local_p)
            y0 = (UP_H - ch) // 2
        else: # pan_left
            cw, ch = int(WIDTH * 1.04), int(HEIGHT * 1.04)
            max_dx = UP_W - cw
            x0 = int(max_dx * (1.0 - local_p))
            y0 = (UP_H - ch) // 2
        cropped = base.crop((x0, y0, x0 + cw, y0 + ch))
        return cropped.resize((WIDTH, HEIGHT), Image.Resampling.BILINEAR)

    # Launch FFmpeg pipe
    ffmpeg_cmd = [
        ffmpeg_exe, "-y",
        "-f", "rawvideo",
        "-pix_fmt", "rgb24",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-r", str(FPS),
        "-i", "-",
        "-i", final_audio_input,
        "-map", "0:v:0", "-map", "1:a:0",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        out_video
    ]

    pipe = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

    print(f"  ⚡ Đang render khung hình (pumping frames into encoder)...")
    last_pct = -1

    for frame_idx in range(total_frames):
        t = frame_idx / FPS
        active_idx = len(scenes_meta) - 1
        for i, sc in enumerate(scenes_meta):
            if sc["start_t"] <= t <= sc["end_t"]:
                active_idx = i
                break
        
        sc = scenes_meta[active_idx]
        local_t = t - sc["start_t"]
        local_p = min(1.0, max(0.0, local_t / max(0.01, sc["duration"])))

        frame = render_scene_crop(sc, local_p)

        # Crossfade transition (0.45s)
        fade_dur = 0.45
        if active_idx > 0 and local_t < fade_dur:
            prev_sc = scenes_meta[active_idx - 1]
            prev_frame = render_scene_crop(prev_sc, 1.0)
            alpha = local_t / fade_dur
            frame = Image.blend(prev_frame, frame, alpha)

        draw = ImageDraw.Draw(frame, "RGBA")

        # 1. Floating Presenter Badge (Top Left)
        draw.rounded_rectangle([(36, 28), (680, 84)], radius=14, fill=(15, 23, 42, 215), outline=(56, 189, 248, 220), width=2)
        draw.text((54, 38), f"Vật lí 10 • {short_title}  |  🎙️ Cô Bích Nhung", font=font_badge, fill=(255, 255, 255, 255))

        # 2. Scene Progress Indicator (Top Right)
        draw.rounded_rectangle([(WIDTH - 220, 28), (WIDTH - 36, 84)], radius=14, fill=(15, 23, 42, 215), outline=(52, 211, 153, 220), width=2)
        draw.text((WIDTH - 200, 38), f"Phân cảnh {sc['idx']}/5", font=font_prog, fill=(52, 211, 153, 255))

        # 3. Dynamic Subtitles (Bottom Center)
        sub_str = ""
        for p_start, p_end, s_txt in sc["subs"]:
            if p_start <= local_p <= p_end:
                sub_str = s_txt
                break

        if sub_str:
            bbox = draw.textbbox((0, 0), sub_str, font=font_sub)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            pad_x, pad_y = 36, 16
            bx0 = (WIDTH - tw) // 2 - pad_x
            bx1 = (WIDTH + tw) // 2 + pad_x
            by0 = HEIGHT - 110
            by1 = by0 + th + pad_y * 2
            # Dark glass pill background with neon cyan glow
            draw.rounded_rectangle([(bx0, by0), (bx1, by1)], radius=12, fill=(11, 19, 43, 225), outline=(0, 229, 255, 200), width=2)
            draw.text((bx0 + pad_x, by0 + pad_y - 2), sub_str, font=font_sub, fill=(255, 255, 255, 255))

        # Pipe raw RGB bytes
        pipe.stdin.write(frame.tobytes())

        pct = int((frame_idx + 1) / total_frames * 100)
        if pct != last_pct and pct % 10 == 0:
            print(f"    Tiến độ: {pct}% ({frame_idx+1}/{total_frames} frames)", flush=True)
            last_pct = pct

    pipe.stdin.close()
    pipe.wait()

    sz_mb = os.path.getsize(out_video) / (1024 * 1024)
    print(f"✅ RENDER HOÀN TẤT! Video thành phẩm: {out_video} ({sz_mb:.2f} MB)")
    return out_video

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--lesson", choices=["12", "14"], default="12", help="Bài cần render (12 hoặc 14)")
    args = parser.parse_args()
    render_lesson(args.lesson)
