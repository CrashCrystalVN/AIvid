import os
import sys
import subprocess
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

sys.stdout.reconfigure(encoding="utf-8")
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

WORK_DIR = r"c:\Users\huy83\Downloads\AIvid"
SCENE_DIR = os.path.join(WORK_DIR, "scenes_video2")
AUDIO_DIR = os.path.join(WORK_DIR, "audio_video2")

scenes_meta = [
    {
        "id": "s1",
        "img": os.path.join(SCENE_DIR, "01_vecto_do_dich_chuyen.jpg"),
        "speaker": "Anh Thư",
        "duration": 19.99,
        "subs": [
            (0.0, 0.48, "Quay lại ngã tư ban nãy: Xe chạy 100 m về hướng Bắc, ta xác định ngay vị trí ở điểm B."),
            (0.48, 1.0, "Đại lượng vừa cho biết độ dài, vừa cho biết hướng đó chính là Độ dịch chuyển (vectơ d)!")
        ],
        "zoom_mode": "in"
    },
    {
        "id": "s2",
        "img": os.path.join(SCENE_DIR, "02_sieu_thi_buu_dien.jpg"),
        "speaker": "Hữu Trọng",
        "duration": 15.94,
        "subs": [
            (0.0, 0.50, "Hai khái niệm Quãng đường và Độ dịch chuyển rất dễ nhầm lẫn, các bạn chú ý nhé!"),
            (0.50, 1.0, "Ba người đi từ siêu thị A đến bưu điện B theo 3 đường khác nhau (xe máy, đi bộ, ô tô).")
        ],
        "zoom_mode": "pan_right"
    },
    {
        "id": "s3",
        "img": os.path.join(SCENE_DIR, "03_bang_so_sanh_s_va_d.jpg"),
        "speaker": "Anh Thư",
        "duration": 24.17,
        "subs": [
            (0.0, 0.45, "Quãng đường s là độ dài thực tế đã đi: Ba người đi 3 đường nên quãng đường khác nhau: s1 ≠ s2 ≠ s3."),
            (0.45, 1.0, "Thế nhưng độ dịch chuyển d chỉ phụ thuộc điểm đầu A và cuối B: Cả 3 người có độ dịch chuyển NHƯ NHAU!")
        ],
        "zoom_mode": "in"
    },
    {
        "id": "s4",
        "img": os.path.join(SCENE_DIR, "04_dieu_kien_d_bang_s.jpg"),
        "speaker": "Hữu Trọng",
        "duration": 21.07,
        "subs": [
            (0.0, 0.52, "Quy tắc cốt lõi: Chỉ khi vật chuyển động thẳng và KHÔNG ĐỔI CHIỀU thì |d| = s."),
            (0.52, 1.0, "Nếu vật đi đường cong hoặc quay đầu ngược lại, độ lớn độ dịch chuyển luôn nhỏ hơn quãng đường (|d| < s)!")
        ],
        "zoom_mode": "pan_left"
    },
    {
        "id": "s5",
        "img": os.path.join(SCENE_DIR, "05_cau_hoi_tuong_tac.jpg"),
        "speaker": "Thế Mỹ & Nhóm 1",
        "duration": 17.04,
        "subs": [
            (0.0, 0.55, "Câu hỏi tương tác: Khi nào độ lớn độ dịch chuyển bằng đúng quãng đường đi được?"),
            (0.55, 1.0, "Đáp án: Khi vật chuyển động THẲNG và KHÔNG ĐỔI CHIỀU! Cảm ơn thầy cô và các bạn đã theo dõi!")
        ],
        "zoom_mode": "out"
    }
]

total_dur = sum(sc["duration"] for sc in scenes_meta)
print(f"Total video duration: {total_dur:.2f}s")

WIDTH, HEIGHT = 1920, 1080
FPS = 24
TOTAL_FRAMES = int(total_dur * FPS)

font_badge = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
font_sub = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 27)

UP_W, UP_H = 2160, 1215
for sc in scenes_meta:
    img = Image.open(sc["img"]).convert("RGB")
    sc["pil_img"] = img.resize((UP_W, UP_H), Image.Resampling.LANCZOS)

cur_t = 0.0
for sc in scenes_meta:
    sc["start_t"] = cur_t
    sc["end_t"] = cur_t + sc["duration"]
    cur_t = sc["end_t"]

def render_scene_crop(sc, local_p):
    mode = sc["zoom_mode"]
    base = sc["pil_img"]
    if mode == "in":
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
    active_idx = len(scenes_meta) - 1
    for i, sc in enumerate(scenes_meta):
        if sc["start_t"] <= t <= sc["end_t"]:
            active_idx = i
            break

    sc = scenes_meta[active_idx]
    local_t = t - sc["start_t"]
    local_p = min(1.0, max(0.0, local_t / max(0.01, sc["duration"])))

    frame = render_scene_crop(sc, local_p)

    fade_dur = 0.45
    if active_idx > 0 and local_t < fade_dur:
        prev_sc = scenes_meta[active_idx - 1]
        prev_frame = render_scene_crop(prev_sc, 1.0)
        alpha = local_t / fade_dur
        frame = Image.blend(prev_frame, frame, alpha)

    draw = ImageDraw.Draw(frame, "RGBA")

    # Top-left floating badge
    draw.rounded_rectangle([(36, 28), (620, 82)], radius=14, fill=(15, 23, 42, 205), outline=(56, 189, 248, 220), width=2)
    draw.text((54, 36), f"Vật lí 10 • Bài 4 (P.2)  |  🎙️ {sc['speaker']}", font=font_badge, fill=(255, 255, 255, 255))

    # Find active subtitle
    sub_str = ""
    for p_start, p_end, s_txt in sc["subs"]:
        if p_start <= local_p <= p_end:
            sub_str = s_txt
            break

    if sub_str:
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

    prog = min(1.0, max(0.0, t / total_dur))
    draw.rectangle([(0, HEIGHT - 6), (WIDTH, HEIGHT)], fill=(15, 23, 42, 180))
    draw.rectangle([(0, HEIGHT - 6), (int(WIDTH * prog), HEIGHT)], fill=(56, 189, 248, 255))

    return frame

out_mp4 = os.path.join(WORK_DIR, "Video2_DoDichChuyen_QuangDuong.mp4")
audio_path = os.path.join(AUDIO_DIR, "final_audio_video2.mp3")

cmd = [
    ffmpeg_exe, "-y",
    "-f", "rawvideo", "-vcodec", "rawvideo",
    "-s", f"{WIDTH}x{HEIGHT}", "-pix_fmt", "rgb24",
    "-r", str(FPS), "-i", "-",
    "-i", audio_path,
    "-c:v", "libx264", "-preset", "veryfast",
    "-pix_fmt", "yuv420p", "-crf", "19",
    "-c:a", "aac", "-b:a", "192k",
    "-shortest", out_mp4
]

print(f"Rendering {TOTAL_FRAMES} frames ({total_dur:.1f}s) to {out_mp4}...")
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
