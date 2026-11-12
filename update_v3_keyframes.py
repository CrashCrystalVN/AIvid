import os
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import numpy as np

v2_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V2_B4_DoDichChuyen_QuangDuong"
v3_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V3_B4_TongHop_DoDichChuyen"
v1_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V1_B4_ViTri_HeQuyChieu"

w, h = 1376, 768

# Load Base Assets
v1_s1 = Image.open(os.path.join(v1_dir, "s1.png")).convert("RGB") # Lab studio 1
lab_bg_v1 = v1_s1.crop((440, 0, 1376, 768)).resize((w, h), Image.Resampling.LANCZOS)

# Cool cyan grade for lab_bg
r, g, b = lab_bg_v1.split()
r = ImageEnhance.Brightness(r).enhance(0.9)
b = ImageEnhance.Brightness(b).enhance(1.15)
lab_bg_cyan = Image.merge("RGB", (r, g, b))

# The My refined crop
tm_only = Image.open(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\the_my_refined.png")
w_tm, h_tm = tm_only.size

# Build precise polygon mask around The My
mask = Image.new("L", (w_tm, h_tm), 0)
draw = ImageDraw.Draw(mask)
pts = [
    (0, 160), (15, 140), (28, 100), (32, 60), (45, 20), (70, 0),
    (102, 5), (128, 35), (138, 85), (134, 130),
    (155, 155), (170, 185), (180, 230), (185, 290), (184, 355), 
    (170, 405), (150, 440), (157, 470), (155, 557),
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
s1_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=1.0, x_pos=0)
s1_v3.save(os.path.join(v3_dir, "s1.png"))

# S2: Quy tac cong vecto tong quat
s2_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=1.03, x_pos=10, contrast=1.03)
s2_v3.save(os.path.join(v3_dir, "s2.png"))

# S4: Tinh Quang duong (s)
s4_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=0.98, x_pos=0, brightness=1.02)
s4_v3.save(os.path.join(v3_dir, "s4.png"))

# S6: So sanh s vs |d|
s6_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=1.02, x_pos=0, brightness=1.01)
s6_v3.save(os.path.join(v3_dir, "s6.png"))

# S7: 3 Truong hop dac biet
s7_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=0.90, x_pos=0)
s7_v3.save(os.path.join(v3_dir, "s7.png"))

# S8: Cau hoi Pop-up
s8_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=1.12, x_pos=0, brightness=1.03)
s8_v3.save(os.path.join(v3_dir, "s8.png"))

# S9: Tong ket & Cam on
s9_v3 = create_the_my_scene(lab_bg_cyan, scale_factor=0.96, x_pos=10)
s9_v3.save(os.path.join(v3_dir, "s9.png"))

print("Updated Video 3 keyframes successfully!")
