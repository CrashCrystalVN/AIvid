import os
import sys
import shutil
import subprocess
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

sys.stdout.reconfigure(encoding="utf-8")
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

ARTIFACT_DIR = r"C:\Users\huy83\.gemini\antigravity\brain\ec3ca795-2d6c-492f-b2d4-d72c0b302dbe"
WORK_DIR = r"c:\Users\huy83\Downloads\AIvid"
SCENE_DIR = os.path.join(WORK_DIR, "scenes_video1")
os.makedirs(SCENE_DIR, exist_ok=True)

# 1. Copy the 5 AI-generated images to scenes_video1
src_files = [
    ("scene1_car_intersection_1794106386229.jpg", "01_nga_tu_oto.jpg"),
    ("scene2_student_question_1794106413123.jpg", "02_hoc_sinh_dat_van_de.jpg"),
    ("scene3_student_coordinates_1794106438848.jpg", "03_he_toa_do_oxy.jpg"),
    ("scene4_student_reference_frame_1794106506479.jpg", "04_he_quy_chieu_chat_diem.jpg"),
    ("scene5_student_quiz_1794106533762.jpg", "05_cau_hoi_tuong_tac.jpg"),
]

for src_name, dst_name in src_files:
    src_path = os.path.join(ARTIFACT_DIR, src_name)
    dst_path = os.path.join(SCENE_DIR, dst_name)
    shutil.copy2(src_path, dst_path)
    print(f"Copied {dst_name}")

# 2. Define 5 narration segments matching the 5 visual scenes, using both Female (Anh Thư) & Male (Hữu Trọng) voices
scenes_meta = [
    {
        "id": "s1",
        "img": os.path.join(SCENE_DIR, "01_nga_tu_oto.jpg"),
        "voice": "vi-VN-HoaiMyNeural",
        "speaker": "Anh Thư",
        "text": "Chào thầy cô và các bạn! Hãy cùng nhóm mình bắt đầu bằng một tình huống thực tế nhé: Một chiếc ô tô đi qua ngã tư O với tốc độ 36 km/h. Sau 10 giây, xe đi được quãng đường 100 mét.",
        "subs": [
            (0.0, 0.45, "Chào thầy cô và các bạn! Hãy cùng nhóm mình bắt đầu bằng một tình huống thực tế nhé:"),
            (0.45, 1.0, "Một chiếc ô tô đi qua ngã tư O với tốc độ 36 km/h. Sau 10 giây, xe đi được quãng đường 100 m.")
        ],
        "zoom_mode": "in"
    },
    {
        "id": "s2",
        "img": os.path.join(SCENE_DIR, "02_hoc_sinh_dat_van_de.jpg"),
        "voice": "vi-VN-HoaiMyNeural",
        "speaker": "Anh Thư",
        "text": "Câu hỏi đặt ra là: Liệu chỉ biết quãng đường 100 mét, chúng mình có thể xác định chính xác xe đang ở đâu trên bản đồ không? Chắc chắn là chưa thể rồi, vì ta chưa biết xe đi về hướng Đông, Tây, Nam hay Bắc!",
        "subs": [
            (0.0, 0.52, "Câu hỏi đặt ra là: Liệu chỉ biết quãng đường 100 m, ta có biết chính xác xe đang ở đâu không?"),
            (0.52, 1.0, "Chắc chắn là chưa thể rồi! Vì ta chưa biết xe đi về hướng Đông, Tây, Nam hay Bắc!")
        ],
        "zoom_mode": "pan_right"
    },
    {
        "id": "s3",
        "img": os.path.join(SCENE_DIR, "03_he_toa_do_oxy.jpg"),
        "voice": "vi-VN-NamMinhNeural",
        "speaker": "Hữu Trọng",
        "text": "Để biết chính xác vị trí, chúng ta cần một hệ tọa độ gắn với vật mốc. Trong đời sống, các bạn thường thấy hệ tọa độ địa lí với trục Ox theo hướng Tây – Đông và trục Oy theo hướng Bắc – Nam. Ví dụ điểm A cách O 20 mét theo hướng 45 độ Đông – Bắc.",
        "subs": [
            (0.0, 0.35, "Để biết chính xác vị trí, chúng ta cần một hệ tọa độ gắn với vật mốc."),
            (0.35, 0.72, "Trong đời sống, hệ tọa độ địa lí có trục Ox hướng Tây – Đông và trục Oy hướng Bắc – Nam."),
            (0.72, 1.0, "Ví dụ: Điểm A được xác định chính xác ở vị trí cách O 20 m, hướng 45° Đông – Bắc.")
        ],
        "zoom_mode": "in"
    },
    {
        "id": "s4",
        "img": os.path.join(SCENE_DIR, "04_he_quy_chieu_chat_diem.jpg"),
        "voice": "vi-VN-HoaiMyNeural",
        "speaker": "Anh Thư",
        "text": "Khi chúng mình kết hợp hệ tọa độ này cùng với mốc thời gian và một chiếc đồng hồ bấm giờ, ta sẽ có một hệ quy chiếu hoàn chỉnh. Nếu xe chỉ chạy thẳng trên một đường, ta chỉ cần chọn một trục Ox trùng với đường đi. Và khi kích thước xe rất nhỏ so với quãng đường 100 mét, tụi mình hoàn toàn có thể coi nó là một chất điểm!",
        "subs": [
            (0.0, 0.36, "Khi kết hợp hệ tọa độ cùng với mốc thời gian và đồng hồ đo, ta có một Hệ quy chiếu hoàn chỉnh."),
            (0.36, 0.66, "Nếu xe chỉ chạy thẳng một chiều, chúng mình chỉ cần chọn duy nhất một trục Ox trùng với đường đi."),
            (0.66, 1.0, "Và khi kích thước xe rất nhỏ so với quãng đường 100 m, tụi mình có thể coi nó là một Chất điểm!")
        ],
        "zoom_mode": "pan_left"
    },
    {
        "id": "s5",
        "img": os.path.join(SCENE_DIR, "05_cau_hoi_tuong_tac.jpg"),
        "voice": "vi-VN-NamMinhNeural",
        "speaker": "Thế Mỹ & Nhóm 1",
        "text": "Câu hỏi tương tác dành cho cả lớp: Khi nào độ dài quãng đường cho phép coi vật là chất điểm? Đó là khi kích thước của vật rất nhỏ so với độ dài đường đi! Cảm ơn thầy cô và các bạn đã lắng nghe!",
        "subs": [
            (0.0, 0.42, "Câu hỏi tương tác: Khi nào độ dài quãng đường cho phép coi vật là chất điểm?"),
            (0.42, 0.78, "Đáp án: Khi kích thước của vật rất nhỏ so với độ dài quãng đường đi được!"),
            (0.78, 1.0, "Cảm ơn thầy cô và các bạn đã theo dõi bài thuyết trình của nhóm mình!")
        ],
        "zoom_mode": "out"
    }
]

def get_audio_duration(path):
    res = subprocess.run([ffmpeg_exe, "-i", path], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    for line in res.stderr.split("\n"):
        if "Duration:" in line:
            t_str = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = t_str.split(":")
            return float(h)*3600 + float(m)*60 + float(s)
    return 10.0

# Generate TTS audio for each scene
concat_lines = []
import time
for sc in scenes_meta:
    txt_file = f"tts_{sc['id']}.txt"
    mp3_file = f"tts_{sc['id']}.mp3"
    if not (os.path.exists(mp3_file) and os.path.getsize(mp3_file) > 1000):
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(sc["text"])
        for attempt in range(5):
            res = subprocess.run([
                sys.executable, "-m", "edge_tts",
                "--voice", sc["voice"],
                "-f", txt_file,
                "--write-media", mp3_file
            ])
            if res.returncode == 0 and os.path.exists(mp3_file) and os.path.getsize(mp3_file) > 1000:
                break
            time.sleep(1.5)
    dur = get_audio_duration(mp3_file)
    sc["duration"] = dur
    concat_lines.append(f"file '{mp3_file}'")
    print(f"Scene {sc['id']} ({sc['speaker']}): {dur:.2f}s")

with open("concat_huong1.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(concat_lines) + "\n")

subprocess.run([
    ffmpeg_exe, "-y", "-f", "concat", "-safe", "0",
    "-i", "concat_huong1.txt", "-c", "copy", "voice_huong1.mp3"
], check=True)

total_dur = sum(sc["duration"] for sc in scenes_meta)
print(f"Total narration duration: {total_dur:.2f}s")

# Mix with background music (bg_music.wav generated earlier)
subprocess.run([
    ffmpeg_exe, "-y",
    "-i", "voice_huong1.mp3",
    "-i", "bg_music.wav",
    "-filter_complex", "[0:a]volume=1.25[a0];[1:a]aloop=loop=-1:size=2e+09,volume=0.22[a1];[a0][a1]amix=inputs=2:duration=first:dropout_transition=2[aout]",
    "-map", "[aout]",
    "-c:a", "libmp3lame", "-b:a", "192k",
    "final_audio_huong1.mp3"
], check=True)

# 3. Render 1920x1080 @ 24fps with smooth Ken Burns effect, crossfades, speaker badge, and captions
WIDTH, HEIGHT = 1920, 1080
FPS = 24
TOTAL_FRAMES = int(total_dur * FPS)

font_badge = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
font_sub = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 27)
font_lesson = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 20)

# Preload and resize base images to 2160x1215 (1.125x of 1920x1080) for smooth Ken Burns cropping
UP_W, UP_H = 2160, 1215
for sc in scenes_meta:
    img = Image.open(sc["img"]).convert("RGB")
    sc["pil_img"] = img.resize((UP_W, UP_H), Image.Resampling.LANCZOS)

# Calculate cumulative start/end times
cur_t = 0.0
for sc in scenes_meta:
    sc["start_t"] = cur_t
    sc["end_t"] = cur_t + sc["duration"]
    cur_t = sc["end_t"]

def render_scene_crop(sc, local_p):
    # local_p in [0.0, 1.0]
    mode = sc["zoom_mode"]
    base = sc["pil_img"]
    if mode == "in":
        # Crop from 2120x1192 down to 1920x1080 centered
        scale = 1.10 - 0.10 * local_p
        cw, ch = int(WIDTH * scale), int(HEIGHT * scale)
        x0 = (UP_W - cw) // 2
        y0 = (UP_H - ch) // 2
    elif mode == "out":
        scale = 1.00 + 0.10 * local_p
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

def get_frame(t):
    # Find active scene
    active_idx = len(scenes_meta) - 1
    for i, sc in enumerate(scenes_meta):
        if sc["start_t"] <= t <= sc["end_t"]:
            active_idx = i
            break

    sc = scenes_meta[active_idx]
    local_t = t - sc["start_t"]
    local_p = min(1.0, max(0.0, local_t / max(0.01, sc["duration"])))

    frame = render_scene_crop(sc, local_p)

    # Crossfade transition (0.45s at the beginning of scenes 2..5)
    fade_dur = 0.45
    if active_idx > 0 and local_t < fade_dur:
        prev_sc = scenes_meta[active_idx - 1]
        prev_frame = render_scene_crop(prev_sc, 1.0)
        alpha = local_t / fade_dur
        frame = Image.blend(prev_frame, frame, alpha)

    draw = ImageDraw.Draw(frame, "RGBA")

    # Top-left floating badge: Lesson + Speaker
    draw.rounded_rectangle([(36, 28), (580, 82)], radius=14, fill=(15, 23, 42, 205), outline=(56, 189, 248, 220), width=2)
    draw.text((54, 36), f"Vật lí 10 • Bài 4  |  🎙️ Thuyết trình: {sc['speaker']}", font=font_badge, fill=(255, 255, 255, 255))

    # Find active subtitle
    sub_str = ""
    for p_start, p_end, s_txt in sc["subs"]:
        if p_start <= local_p <= p_end:
            sub_str = s_txt
            break

    if sub_str:
        # Measure text width to center it nicely
        bbox = draw.textbbox((0, 0), sub_str, font=font_sub)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        pad_x, pad_y = 32, 16
        bx0 = (WIDTH - tw) // 2 - pad_x
        bx1 = (WIDTH + tw) // 2 + pad_x
        by0 = HEIGHT - 105
        by1 = by0 + th + pad_y * 2
        draw.rounded_rectangle([(bx0, by0), (bx1, by1)], radius=16, fill=(10, 15, 30, 215), outline=(251, 191, 36, 200), width=2)
        draw.text(((WIDTH - tw) // 2, by0 + pad_y - 2), sub_str, font=font_sub, fill=(255, 255, 255, 255))

    # Bottom thin progress bar
    prog = min(1.0, max(0.0, t / total_dur))
    draw.rectangle([(0, HEIGHT - 6), (WIDTH, HEIGHT)], fill=(15, 23, 42, 180))
    draw.rectangle([(0, HEIGHT - 6), (int(WIDTH * prog), HEIGHT)], fill=(56, 189, 248, 255))

    return frame

out_mp4 = os.path.join(WORK_DIR, "Video1_Sample_Huong1_Smartboard.mp4")
cmd = [
    ffmpeg_exe, "-y",
    "-f", "rawvideo", "-vcodec", "rawvideo",
    "-s", f"{WIDTH}x{HEIGHT}", "-pix_fmt", "rgb24",
    "-r", str(FPS), "-i", "-",
    "-i", "final_audio_huong1.mp3",
    "-c:v", "libx264", "-preset", "veryfast",
    "-pix_fmt", "yuv420p", "-crf", "19",
    "-c:a", "aac", "-b:a", "192k",
    "-shortest", out_mp4
]

print(f"Rendering {TOTAL_FRAMES} frames to {out_mp4}...")
proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
for f_idx in range(TOTAL_FRAMES):
    t = f_idx / FPS
    im = get_frame(t)
    proc.stdin.write(im.tobytes())
    if f_idx % 240 == 0:
        print(f"Progress: {f_idx}/{TOTAL_FRAMES} ({f_idx*100//TOTAL_FRAMES}%)")

proc.stdin.close()
proc.wait()
print("DONE! Saved:", out_mp4)
