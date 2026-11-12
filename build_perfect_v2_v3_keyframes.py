import os
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw

v2_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V2_B4_DoDichChuyen_QuangDuong"
v3_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V3_B4_TongHop_DoDichChuyen"
v1_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V1_B4_ViTri_HeQuyChieu"

w, h = 1376, 768

# Load Base Assets
v2_s1 = Image.open(os.path.join(v2_dir, "s1.png")).convert("RGB") # Huu Trong master
v2_s2 = Image.open(os.path.join(v2_dir, "s2.png")).convert("RGB") # Intersection master
v3_s3 = Image.open(os.path.join(v3_dir, "s3.png")).convert("RGB") # Park paths master
v1_s4 = Image.open(os.path.join(v1_dir, "s4.png")).convert("RGB") # Straight highway

# 1. VIDEO 2 GENERATION
print("Generating Video 2 keyframes...")
v2_s1.save(os.path.join(v2_dir, "s1.png"))
v2_s2.save(os.path.join(v2_dir, "s2.png"))

# S3: Dinh nghia Do dich chuyen
s3 = v2_s1.crop((20, 15, 1330, 755)).resize((w, h), Image.Resampling.LANCZOS)
s3 = ImageEnhance.Contrast(s3).enhance(1.02)
s3.save(os.path.join(v2_dir, "s3.png"))

# S4: Mo hinh 3 tuyen duong
s4 = v2_s2.crop((120, 60, 1256, 708)).resize((w, h), Image.Resampling.LANCZOS)
s4 = ImageEnhance.Color(s4).enhance(1.08)
s4.save(os.path.join(v2_dir, "s4.png"))

# S5: Ban chat Quang duong (s)
s5 = v2_s1.copy()
r, g, b = s5.split()
r = ImageEnhance.Brightness(r).enhance(0.94)
b = ImageEnhance.Brightness(b).enhance(1.06)
s5 = Image.merge("RGB", (r, g, b))
s5.save(os.path.join(v2_dir, "s5.png"))

# S6: Ban chat Do dich chuyen (d)
s6 = v2_s1.crop((0, 0, 1340, 750)).resize((w, h), Image.Resampling.LANCZOS)
s6 = ImageEnhance.Brightness(s6).enhance(1.02)
s6 = ImageEnhance.Sharpness(s6).enhance(1.05)
s6.save(os.path.join(v2_dir, "s6.png"))

# S7: Bang so sanh truc quan s vs d
s7 = v2_s1.copy()
overlay7 = Image.new("RGBA", (w, h), (0, 0, 0, 0))
d7 = ImageDraw.Draw(overlay7)
start_x = int(w * 0.38)
for x in range(start_x, w):
    alpha = int(45 * ((x - start_x) / (w - start_x)))
    d7.line([(x, 0), (x, h)], fill=(4, 12, 28, alpha))
s7 = Image.alpha_composite(s7.convert("RGBA"), overlay7).convert("RGB")
s7.save(os.path.join(v2_dir, "s7.png"))

# S8: Dieu kien |d| = s
s8 = v1_s4.copy()
r, g, b = s8.split()
r = ImageEnhance.Brightness(r).enhance(1.24)
g = ImageEnhance.Brightness(g).enhance(1.04)
b = ImageEnhance.Brightness(b).enhance(0.76)
s8 = Image.merge("RGB", (r, g, b))
s8 = ImageEnhance.Contrast(s8).enhance(1.08)
s8.save(os.path.join(v2_dir, "s8.png"))

# S9: Cau hoi cung co & Chao ket Video 2
s9 = v2_s1.crop((35, 10, 1250, 730)).resize((w, h), Image.Resampling.LANCZOS)
s9 = ImageEnhance.Brightness(s9).enhance(1.02)
s9.save(os.path.join(v2_dir, "s9.png"))
print("Video 2 keyframes complete.")

# 2. VIDEO 3 GENERATION
print("Generating Video 3 keyframes...")
pure_studio = Image.open(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\pure_studio.png").convert("RGB")
tm = Image.open(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\tm_from_02.png")
w_tm, h_tm = tm.size

mask = Image.new("L", (w_tm, h_tm), 0)
draw = ImageDraw.Draw(mask)
pts = [
    (70, 587), (70, 480), (45, 420), (40, 260), (40, 200), 
    (45, 170), (95, 150), (105, 100), (100, 50),
    (150, 0), (220, 10), (240, 50), (235, 120), (270, 160), (300, 220),
    (300, 587)
]
draw.polygon(pts, fill=255)
mask_f = mask.filter(ImageFilter.GaussianBlur(radius=2))

def render_v3_mc(scale_factor=1.0, x_pos=0, y_offset=0, brightness=1.0, contrast=1.0):
    canvas = pure_studio.copy().convert("RGBA")
    base_scale = 720.0 / h_tm
    total_scale = base_scale * scale_factor
    cur_w = int(w_tm * total_scale)
    cur_h = int(h_tm * total_scale)
    
    char = tm.resize((cur_w, cur_h), Image.Resampling.LANCZOS)
    if brightness != 1.0:
        char = ImageEnhance.Brightness(char).enhance(brightness)
    if contrast != 1.0:
        char = ImageEnhance.Contrast(char).enhance(contrast)
    m = mask_f.resize((cur_w, cur_h), Image.Resampling.LANCZOS)
    
    y = h - cur_h + y_offset
    canvas.paste(char, (x_pos, y), m)
    return canvas.convert("RGB")

# S1: Mo dau & Tieu de Video 3
render_v3_mc(scale_factor=1.0, x_pos=0).save(os.path.join(v3_dir, "s1.png"))

# S2: Quy tac cong vecto tong quat
render_v3_mc(scale_factor=1.03, x_pos=10, contrast=1.03).save(os.path.join(v3_dir, "s2.png"))

# S3: Master image (park walking paths aerial)
v3_s3.save(os.path.join(v3_dir, "s3.png"))

# S4: Tinh Quang duong (s)
render_v3_mc(scale_factor=0.98, x_pos=0, brightness=1.02).save(os.path.join(v3_dir, "s4.png"))

# S5: Tinh Do dich chuyen bang Dinh ly Pythagoras
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
render_v3_mc(scale_factor=1.02, x_pos=0, brightness=1.01).save(os.path.join(v3_dir, "s6.png"))

# S7: 3 Truong hop dac biet
render_v3_mc(scale_factor=0.90, x_pos=0).save(os.path.join(v3_dir, "s7.png"))

# S8: Cau hoi Pop-up
render_v3_mc(scale_factor=1.12, x_pos=0, brightness=1.03).save(os.path.join(v3_dir, "s8.png"))

# S9: Tong ket & Cam on
render_v3_mc(scale_factor=0.96, x_pos=15).save(os.path.join(v3_dir, "s9.png"))

print("Video 3 keyframes complete.")
print("ALL 18 KEYFRAMES FINALIZED PERFECTLY!")
