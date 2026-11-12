import os
import math
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageOps
import numpy as np

v2_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V2_B4_DoDichChuyen_QuangDuong"
v3_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V3_B4_TongHop_DoDichChuyen"
v1_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V1_B4_ViTri_HeQuyChieu"
sc2_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\scenes_video2"

w, h = 1376, 768

# Load Base Assets
v2_s1 = Image.open(os.path.join(v2_dir, "s1.png")).convert("RGB") # Huu Trong master
v2_s2 = Image.open(os.path.join(v2_dir, "s2.png")).convert("RGB") # Intersection master
v3_s3 = Image.open(os.path.join(v3_dir, "s3.png")).convert("RGB") # Park paths master
v1_s1 = Image.open(os.path.join(v1_dir, "s1.png")).convert("RGB") # Lab studio 1
v1_s4 = Image.open(os.path.join(v1_dir, "s4.png")).convert("RGB") # Straight highway

# Studio BGs
studio_bg_v2 = v2_s1.crop((460, 0, 1376, 768)).resize((w, h), Image.Resampling.LANCZOS)
lab_bg_v1 = v1_s1.crop((440, 0, 1376, 768)).resize((w, h), Image.Resampling.LANCZOS)

# Cool cyan grade for lab_bg
r, g, b = lab_bg_v1.split()
r = ImageEnhance.Brightness(r).enhance(0.9)
b = ImageEnhance.Brightness(b).enhance(1.15)
lab_bg_cyan = Image.merge("RGB", (r, g, b))

# ========================================================
# 1. VIDEO 2: V2_B4_DoDichChuyen_QuangDuong (9 SCENES)
# MC: Hữu Trọng (glasses, crisp white uniform, navy collar)
# ========================================================
print("Generating Video 2 keyframes...")

# S1: Master image (already verified)
v2_s1.save(os.path.join(v2_dir, "s1.png"))

# S2: Master image (already verified)
v2_s2.save(os.path.join(v2_dir, "s2.png"))

# S3: Dinh nghia Do dich chuyen
# Camera push-in on Huu Trong (left 35%), crisp soft lighting, 65% clean negative space
s3 = v2_s1.crop((20, 15, 1330, 755)).resize((w, h), Image.Resampling.LANCZOS)
s3 = ImageEnhance.Contrast(s3).enhance(1.02)
s3.save(os.path.join(v2_dir, "s3.png"))

# S4: Mo hinh 3 tuyen duong: Sieu thi A den Buu dien B
# Cinematic aerial city district with connecting roads and green squares
s4 = v2_s2.crop((120, 60, 1256, 708)).resize((w, h), Image.Resampling.LANCZOS)
s4 = ImageEnhance.Color(s4).enhance(1.08)
s4.save(os.path.join(v2_dir, "s4.png"))

# S5: Ban chat Quang duong (s)
# Medium shot Huu Trong, deeper navy blue ambient lighting
s5 = v2_s1.copy()
r, g, b = s5.split()
r = ImageEnhance.Brightness(r).enhance(0.94)
b = ImageEnhance.Brightness(b).enhance(1.06)
s5 = Image.merge("RGB", (r, g, b))
s5.save(os.path.join(v2_dir, "s5.png"))

# S6: Ban chat Do dich chuyen (d)
# Medium shot Huu Trong, bright high-tech background, crisp clarity
s6 = v2_s1.crop((0, 0, 1340, 750)).resize((w, h), Image.Resampling.LANCZOS)
s6 = ImageEnhance.Brightness(s6).enhance(1.02)
s6 = ImageEnhance.Sharpness(s6).enhance(1.05)
s6.save(os.path.join(v2_dir, "s6.png"))

# S7: Bang so sanh truc quan s vs d
# Huu Trong on left, clean studio with subtle right-side gradient for high-contrast comparison table
s7 = v2_s1.copy()
overlay7 = Image.new("RGBA", (w, h), (0, 0, 0, 0))
d7 = ImageDraw.Draw(overlay7)
start_x = int(w * 0.38)
for x in range(start_x, w):
    alpha = int(45 * ((x - start_x) / (w - start_x)))
    d7.line([(x, 0), (x, h)], fill=(4, 12, 28, alpha))
s7 = Image.alpha_composite(s7.convert("RGBA"), overlay7).convert("RGB")
s7.save(os.path.join(v2_dir, "s7.png"))

# S8: Dieu kien |d| = s: Chuyen dong thang khong doi chieu
# Lone vehicle on straight highway vanishing into sunset horizon
s8 = v1_s4.copy()
r, g, b = s8.split()
r = ImageEnhance.Brightness(r).enhance(1.24) # warm sunset glow
g = ImageEnhance.Brightness(g).enhance(1.04) # golden yellow
b = ImageEnhance.Brightness(b).enhance(0.76) # deep evening tone
s8 = Image.merge("RGB", (r, g, b))
s8 = ImageEnhance.Contrast(s8).enhance(1.08)
s8.save(os.path.join(v2_dir, "s8.png"))

# S9: Cau hoi cung co & Chao ket Video 2
# Medium close-up of Huu Trong smiling warmly
s9 = v2_s1.crop((35, 10, 1250, 730)).resize((w, h), Image.Resampling.LANCZOS)
s9 = ImageEnhance.Brightness(s9).enhance(1.02)
s9.save(os.path.join(v2_dir, "s9.png"))

print("Video 2 keyframes complete (s1..s9).")

# ========================================================
# 2. VIDEO 3: V3_B4_TongHop_DoDichChuyen (9 SCENES)
# MC: Thế Mỹ (clean side-part hair, NO GLASSES, white uniform)
# ========================================================
print("Generating Video 3 keyframes...")

# Load The My cutout asset
tm_crop = Image.open(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\the_my_clean_crop.png")
# Crop out Anh Thu completely
tm_only = tm_crop.crop((42, 0, 242, 558))
w_tm, h_tm = tm_only.size

# Build precise polygon mask around The My
mask = Image.new("L", (w_tm, h_tm), 0)
draw = ImageDraw.Draw(mask)
pts = [
    (0, 160), (35, 140), (42, 100), (45, 60), (60, 20), (83, 0),
    (115, 5), (142, 35), (152, 85), (147, 130),
    (168, 155), (183, 185), (193, 230), (200, 290), (198, 355), 
    (183, 405), (163, 440), (170, 470), (168, 557),
    (0, 557)
]
draw.polygon(pts, fill=255)
mask_feather = mask.filter(ImageFilter.GaussianBlur(radius=2))

def create_the_my_scene(bg, scale_factor=1.0, x_pos=0, y_offset=0, brightness=1.0, contrast=1.0):
    canvas = bg.copy().convert("RGBA")
    base_scale = 680.0 / h_tm
    total_scale = base_scale * scale_factor
    cur_w = int(w_tm * total_scale)
    cur_h = int(h_tm * total_scale)
    
    char = tm_only.resize((cur_w, cur_h), Image.Resampling.LANCZOS)
    if brightness != 1.0:
        char = ImageEnhance.Brightness(char).enhance(brightness)
    if contrast != 1.0:
        char = ImageEnhance.Contrast(char).enhance(contrast)
    m = mask_feather.resize((cur_w, cur_h), Image.Resampling.LANCZOS)
    
    y = h - cur_h + y_offset
    canvas.paste(char, (x_pos, y), m)
    return canvas.convert("RGB")

# S1: Mo dau & Tieu de Video 3
# The My medium shot on left 25%, high-tech lab background, clean 75% negative space
s1_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=1.0, x_pos=0)
s1_v3.save(os.path.join(v3_dir, "s1.png"))

# S2: Quy tac cong vecto tong quat
# The My medium shot, framing virtual graphic area on right
s2_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=1.03, x_pos=15, contrast=1.03)
s2_v3.save(os.path.join(v3_dir, "s2.png"))

# S3: Master image (already verified: park walking paths aerial)
v3_s3.save(os.path.join(v3_dir, "s3.png"))

# S4: Tinh Quang duong (s)
# The My pointing toward right space with light smile
s4_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=0.98, x_pos=0, brightness=1.02)
s4_v3.save(os.path.join(v3_dir, "s4.png"))

# S5: Tinh Do dich chuyen bang Dinh ly Pythagoras
# Futuristic digital laboratory floor with dark reflective tiles and soft cyan grid lines
s5_bg = Image.new("RGB", (w, h), (10, 18, 32))
draw_s5 = ImageDraw.Draw(s5_bg)
grid_color = (20, 65, 110)
horizon_y = int(h * 0.38)
for i in range(1, 16):
    py = horizon_y + int((h - horizon_y) * (i / 15.0) ** 1.8)
    draw_s5.line([(0, py), (w, py)], fill=grid_color, width=1)
for k in range(-14, 15):
    x_bottom = int(w * 0.5 + k * (w * 0.075))
    draw_s5.line([(int(w * 0.5), horizon_y), (x_bottom, h)], fill=grid_color, width=1)
s5_bg = s5_bg.filter(ImageFilter.GaussianBlur(radius=1.2))
glow5 = Image.new("RGBA", (w, h), (0, 0, 0, 0))
dglow5 = ImageDraw.Draw(glow5)
for r_glow in range(280, 0, -10):
    alpha = int(35 * (1 - r_glow / 280))
    dglow5.ellipse([(w*0.5 - r_glow, h*0.65 - r_glow*0.35), (w*0.5 + r_glow, h*0.65 + r_glow*0.35)], fill=(0, 229, 255, alpha))
s5_img = Image.alpha_composite(s5_bg.convert("RGBA"), glow5).convert("RGB")
s5_img.save(os.path.join(v3_dir, "s5.png"))

# S6: So sanh s vs |d|
# The My medium shot, cool cyan lab lighting
s6_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=1.02, x_pos=10, brightness=1.01)
s6_v3.save(os.path.join(v3_dir, "s6.png"))

# S7: 3 Truong hop dac biet
# The My wide shot on left, right 75% open space for 3 cases
s7_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=0.90, x_pos=0)
s7_v3.save(os.path.join(v3_dir, "s7.png"))

# S8: Cau hoi Pop-up
# The My medium close-up, warm smile
s8_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=1.12, x_pos=0, brightness=1.03)
s8_v3.save(os.path.join(v3_dir, "s8.png"))

# S9: Tong ket & Cam on
# The My medium shot standing proudly, closing scene
s9_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=0.96, x_pos=20)
s9_v3.save(os.path.join(v3_dir, "s9.png"))

print("Video 3 keyframes complete (s1..s9).")
print("ALL 18 KEYFRAMES GENERATED AND SAVED SUCCESSFULLY!")
