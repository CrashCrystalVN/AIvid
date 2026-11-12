import os
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw

v3_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V3_B4_TongHop_DoDichChuyen"
v1_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V1_B4_ViTri_HeQuyChieu"

w, h = 1376, 768

# Load clean cyan lab background
v1_s1 = Image.open(os.path.join(v1_dir, "s1.png")).convert("RGB")
lab_bg = v1_s1.crop((440, 0, 1376, 768)).resize((w, h), Image.Resampling.LANCZOS)
r, g, b = lab_bg.split()
r = ImageEnhance.Brightness(r).enhance(0.88)
b = ImageEnhance.Brightness(b).enhance(1.15)
lab_bg_cyan = Image.merge("RGB", (r, g, b))

# Load pure The My crop (165 x 558)
tm_pure = Image.open(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\the_my_pure.png")
w_tm, h_tm = tm_pure.size

# Build precise polygon mask around The My
mask = Image.new("L", (w_tm, h_tm), 0)
draw = ImageDraw.Draw(mask)
pts = [
    (0, 160), (6, 140), (10, 100), (15, 60), (25, 20), (48, 0),
    (80, 5), (106, 35), (116, 85), (112, 130),
    (133, 155), (148, 185), (158, 230), (164, 290), (163, 355), 
    (148, 405), (128, 440), (135, 470), (133, 557),
    (0, 557)
]
draw.polygon(pts, fill=255)
mask_feather = mask.filter(ImageFilter.GaussianBlur(radius=2))

def render_v3_scene(scale_factor=1.0, x_pos=20, y_offset=0, brightness=1.0, contrast=1.0):
    canvas = lab_bg_cyan.copy().convert("RGBA")
    base_scale = 680.0 / h_tm
    total_scale = base_scale * scale_factor
    cur_w = int(w_tm * total_scale)
    cur_h = int(h_tm * total_scale)
    
    char = tm_pure.resize((cur_w, cur_h), Image.Resampling.LANCZOS)
    if brightness != 1.0:
        char = ImageEnhance.Brightness(char).enhance(brightness)
    if contrast != 1.0:
        char = ImageEnhance.Contrast(char).enhance(contrast)
    m = mask_feather.resize((cur_w, cur_h), Image.Resampling.LANCZOS)
    
    y = h - cur_h + y_offset
    canvas.paste(char, (x_pos, y), m)
    return canvas.convert("RGB")

# S1: Mo dau & Tieu de Video 3
render_v3_scene(scale_factor=1.0, x_pos=30).save(os.path.join(v3_dir, "s1.png"))

# S2: Quy tac cong vecto tong quat
render_v3_scene(scale_factor=1.03, x_pos=20, contrast=1.03).save(os.path.join(v3_dir, "s2.png"))

# S4: Tinh Quang duong (s)
render_v3_scene(scale_factor=0.98, x_pos=30, brightness=1.02).save(os.path.join(v3_dir, "s4.png"))

# S6: So sanh s vs |d|
render_v3_scene(scale_factor=1.02, x_pos=25, brightness=1.01).save(os.path.join(v3_dir, "s6.png"))

# S7: 3 Truong hop dac biet
render_v3_scene(scale_factor=0.90, x_pos=15).save(os.path.join(v3_dir, "s7.png"))

# S8: Cau hoi Pop-up
render_v3_scene(scale_factor=1.12, x_pos=20, brightness=1.03).save(os.path.join(v3_dir, "s8.png"))

# S9: Tong ket & Cam on
render_v3_scene(scale_factor=0.96, x_pos=35).save(os.path.join(v3_dir, "s9.png"))

print("All V3 character scenes updated with 100% pure cutout!")
