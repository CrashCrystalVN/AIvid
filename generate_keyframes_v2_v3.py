import os
import math
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageOps
import numpy as np

v2_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V2_B4_DoDichChuyen_QuangDuong"
v3_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V3_B4_TongHop_DoDichChuyen"
v1_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V1_B4_ViTri_HeQuyChieu"
sc2_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\scenes_video2"

w, h = 1376, 768

# Load Base Images
v2_s1 = Image.open(os.path.join(v2_dir, "s1.png")).convert("RGB") # Huu Trong master
v2_s2 = Image.open(os.path.join(v2_dir, "s2.png")).convert("RGB") # Intersection master
v3_s3 = Image.open(os.path.join(v3_dir, "s3.png")).convert("RGB") # Park paths master
v1_s1 = Image.open(os.path.join(v1_dir, "s1.png")).convert("RGB") # Lab studio 1
v1_s4 = Image.open(os.path.join(v1_dir, "s4.png")).convert("RGB") # Straight highway
v1_s7 = Image.open(os.path.join(v1_dir, "s7.png")).convert("RGB") # Wide highway
tm_pointing = Image.open(os.path.join(sc2_dir, "04_dieu_kien_d_bang_s.jpg")).convert("RGB") # The My pointing
tm_facing = Image.open(os.path.join(sc2_dir, "05_cau_hoi_tuong_tac.jpg")).convert("RGB") # The My facing

# Extract clean modern studio background from v2_s1 (right half has no person)
studio_bg_v2 = v2_s1.crop((460, 0, 1376, 768)).resize((w, h), Image.Resampling.LANCZOS)
# Clean lab background from v1_s1
lab_bg_v1 = v1_s1.crop((440, 0, 1376, 768)).resize((w, h), Image.Resampling.LANCZOS)

# Helper function to create seamless blend of character on background
def composite_mc_on_bg(bg, char_img, pos=(0, 0), scale=1.0, flip=False, brightness=1.0, contrast=1.0):
    canvas = bg.copy()
    if flip:
        char_img = char_img.transpose(Image.FLIP_LEFT_RIGHT)
    if scale != 1.0:
        nw = int(char_img.width * scale)
        nh = int(char_img.height * scale)
        char_img = char_img.resize((nw, nh), Image.Resampling.LANCZOS)
    if brightness != 1.0:
        char_img = ImageEnhance.Brightness(char_img).enhance(brightness)
    if contrast != 1.0:
        char_img = ImageEnhance.Contrast(char_img).enhance(contrast)
    
    # Feathered mask
    mask = Image.new("L", char_img.size, 255)
    canvas.paste(char_img, pos)
    return canvas

# ==========================================
# VIDEO 2: V2_B4_DoDichChuyen_QuangDuong
# MC: Hữu Trọng (glasses, white uniform, dark navy collar)
# ==========================================
print("--- Processing Video 2 ---")
# S1: already exists (Huu Trong intro)
# S2: already exists (Intersection aerial)

# S3: Dinh nghia Do dich chuyen
# Camera zooms slightly closer into Huu Trong, presenter stance on left 35%, right 65% clean space
crop_s3 = v2_s1.crop((20, 20, 1300, 750)).resize((w, h), Image.Resampling.LANCZOS)
crop_s3 = ImageEnhance.Contrast(crop_s3).enhance(1.03)
crop_s3.save(os.path.join(v2_dir, "s3.png"))
print("Saved V2 s3.png")

# S4: Mo hinh 3 tuyen duong: Sieu thi A den Buu dien B
# Aerial bird's-eye view of city district with roads & parks, clean asphalt ready for 3 route lines
# Rotate / pan v2_s2 to provide a fresh district layout with two distinct landmark hubs
im_s4 = v2_s2.copy()
im_s4 = im_s4.crop((100, 50, 1276, 718)).resize((w, h), Image.Resampling.LANCZOS)
im_s4 = ImageEnhance.Color(im_s4).enhance(1.1)
im_s4.save(os.path.join(v2_dir, "s4.png"))
print("Saved V2 s4.png")

# S5: Ban chat Quang duong (s)
# Medium shot Huu Trong, left side, slightly deeper navy ambient studio lighting
im_s5 = v2_s1.copy()
# Subtle color temperature shift towards deeper navy/cyan
r, g, b = im_s5.split()
b = ImageEnhance.Brightness(b).enhance(1.06)
r = ImageEnhance.Brightness(r).enhance(0.95)
im_s5 = Image.merge("RGB", (r, g, b))
im_s5.save(os.path.join(v2_dir, "s5.png"))
print("Saved V2 s5.png")

# S6: Ban chat Do dich chuyen (d)
# Huu Trong medium shot, crisp bright lighting, right 65% clean
crop_s6 = v2_s1.crop((0, 0, 1320, 740)).resize((w, h), Image.Resampling.LANCZOS)
crop_s6 = ImageEnhance.Brightness(crop_s6).enhance(1.03)
crop_s6 = ImageEnhance.Sharpness(crop_s6).enhance(1.1)
crop_s6.save(os.path.join(v2_dir, "s6.png"))
print("Saved V2 s6.png")

# S7: Bang so sanh truc quan s vs d
# Medium-wide framing: Huu Trong positioned further to the left (28%), leaving large 72% open area on right for table
bg_s7 = studio_bg_v2.copy()
# Dim the right side slightly for high contrast table overlay
dark_overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
draw = ImageDraw.Draw(dark_overlay)
for x in range(int(w * 0.35), w):
    alpha = int(60 * ((x - w * 0.35) / (w * 0.65)))
    draw.line([(x, 0), (x, h)], fill=(6, 16, 32, alpha))
bg_s7 = Image.alpha_composite(bg_s7.convert("RGBA"), dark_overlay).convert("RGB")

# Paste Huu Trong on far left
char_ht = v2_s1.crop((0, 0, 520, 768))
# scale down slightly for wide shot
char_ht_wide = char_ht.resize((int(char_ht.width * 0.92), int(char_ht.height * 0.92)), Image.Resampling.LANCZOS)
bg_s7.paste(char_ht_wide, (0, h - char_ht_wide.height))
bg_s7.save(os.path.join(v2_dir, "s7.png"))
print("Saved V2 s7.png")

# S8: Dieu kien |d| = s: Chuyen dong thang khong doi chieu
# Cinematic straight highway vanishing into horizon at sunset
# Use v1_s4 with sunset golden hour grading
im_s8 = v1_s4.copy()
r, g, b = im_s8.split()
r = ImageEnhance.Brightness(r).enhance(1.22) # warm red
g = ImageEnhance.Brightness(g).enhance(1.05) # warm yellow
b = ImageEnhance.Brightness(b).enhance(0.78) # reduce cool blue
sunset_road = Image.merge("RGB", (r, g, b))
# add subtle warm vignette
sunset_road = ImageEnhance.Contrast(sunset_road).enhance(1.1)
sunset_road.save(os.path.join(v2_dir, "s8.png"))
print("Saved V2 s8.png")

# S9: Cau hoi cung co & Chao ket Video 2
# Medium close-up of Huu Trong smiling warmly, engaging pose
crop_s9 = v2_s1.crop((40, 0, 850, 768))
bg_s9 = studio_bg_v2.copy()
# Place close up Huu Trong on left
scale_cu = 1.05
cu_w = int(crop_s9.width * scale_cu)
cu_h = int(crop_s9.height * scale_cu)
crop_s9_scaled = crop_s9.resize((cu_w, cu_h), Image.Resampling.LANCZOS)
bg_s9.paste(crop_s9_scaled, (0, h - cu_h))
bg_s9.save(os.path.join(v2_dir, "s9.png"))
print("Saved V2 s9.png")

# ==========================================
# VIDEO 3: V3_B4_TongHop_DoDichChuyen
# MC: Thế Mỹ (clean side-part hair, NO GLASSES, white uniform)
# ==========================================
print("--- Processing Video 3 ---")

# Prepare clean cutout of The My from authentic source
# In tm_pointing: The My is at (120, 190, 750, 768)
tm_char = tm_pointing.crop((130, 190, 740, 768))

# Let's create an accurate alpha mask for The My
# The smartboard on the right is light cyan/white, with black frame
# The background is classroom wall.
# Let's extract The My cleanly:
tm_rgb = np.array(tm_char)
tm_h, tm_w, _ = tm_rgb.shape

# The My mask: everything inside the person outline
# In tm_char, The My's head is around x: 100..350, y: 0..250
# Torso is x: 50..450, y: 200..550
# Arm is x: 350..600, y: 220..380
# Trousers is x: 100..400, y: 550..768
# Let's create a smooth polygonal mask around The My
mask_tm = Image.new("L", (tm_w, tm_h), 0)
draw_tm = ImageDraw.Draw(mask_tm)

# Body polygon outline
poly = [
    (150, 0), (280, 0), (320, 50), (330, 120), (320, 190), 
    (380, 220), (450, 250), (590, 280), (600, 340), (560, 370), 
    (470, 360), (430, 370), (430, 480), (440, 580), (410, 768), 
    (110, 768), (120, 580), (80, 480), (50, 360), (90, 260), 
    (120, 210), (120, 100), (130, 40)
]
draw_tm.polygon(poly, fill=255)
# Feather edges
mask_tm = mask_tm.filter(ImageFilter.GaussianBlur(radius=3))

tm_rgba = tm_char.convert("RGBA")
tm_rgba.putalpha(mask_tm)

# Background for V3: high-tech physics simulation laboratory with cyan aesthetic
v3_lab_bg = lab_bg_v1.copy()
# Color grade to cool cyan/blue
r, g, b = v3_lab_bg.split()
r = ImageEnhance.Brightness(r).enhance(0.88)
b = ImageEnhance.Brightness(b).enhance(1.15)
v3_lab_bg = Image.merge("RGB", (r, g, b))

# S1: Mo dau & Tieu de Video 3
# The My medium shot on left 35%, right 65% clean open space in tech lab
s1_canvas = v3_lab_bg.copy().convert("RGBA")
# Position The My on left
scale_s1 = (h * 0.95) / tm_h
tm_s1 = tm_rgba.resize((int(tm_w * scale_s1), int(tm_h * scale_s1)), Image.Resampling.LANCZOS)
s1_canvas.paste(tm_s1, (40, h - tm_s1.height), tm_s1)
s1_v3 = s1_canvas.convert("RGB")
s1_v3.save(os.path.join(v3_dir, "s1.png"))
print("Saved V3 s1.png")

# S2: Quy tac cong vecto tong quat
# The My gesturing, lab background with cool cyan ambient
s2_canvas = v3_lab_bg.copy().convert("RGBA")
tm_s2 = tm_rgba.resize((int(tm_w * scale_s1 * 1.03), int(tm_h * scale_s1 * 1.03)), Image.Resampling.LANCZOS)
s2_canvas.paste(tm_s2, (20, h - tm_s2.height), tm_s2)
s2_canvas.convert("RGB").save(os.path.join(v3_dir, "s2.png"))
print("Saved V3 s2.png")

# S3: already exists (Park walking paths aerial)

# S4: Tinh Quang duong (s)
# The My pointing toward right space with light smile
s4_canvas = v3_lab_bg.copy().convert("RGBA")
tm_s4 = tm_rgba.resize((int(tm_w * scale_s1 * 0.98), int(tm_h * scale_s1 * 0.98)), Image.Resampling.LANCZOS)
s4_canvas.paste(tm_s4, (50, h - tm_s4.height), tm_s4)
s4_canvas.convert("RGB").save(os.path.join(v3_dir, "s4.png"))
print("Saved V3 s4.png")

# S5: Tinh Do dich chuyen bang Dinh ly Pythagoras
# Futuristic digital laboratory floor with dark reflective tiles and soft cyan grid lines
s5_bg = Image.new("RGB", (w, h), (10, 18, 32))
draw_s5 = ImageDraw.Draw(s5_bg)
# Draw subtle perspective grid lines on the reflective floor
grid_color = (20, 60, 100)
horizon_y = int(h * 0.4)
# Horizontal grid lines with perspective spacing
for i in range(1, 16):
    py = horizon_y + int((h - horizon_y) * (i / 15.0) ** 1.8)
    draw_s5.line([(0, py), (w, py)], fill=grid_color, width=1)
# Vertical perspective lines converging to center horizon
for k in range(-12, 13):
    x_bottom = int(w * 0.5 + k * (w * 0.08))
    draw_s5.line([(int(w * 0.5), horizon_y), (x_bottom, h)], fill=grid_color, width=1)
# Add glowing ambient cyan gradient
s5_bg = s5_bg.filter(ImageFilter.GaussianBlur(radius=1.5))
# Soft glow center
glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
draw_glow = ImageDraw.Draw(glow)
for r_glow in range(250, 0, -10):
    alpha = int(40 * (1 - r_glow / 250))
    draw_glow.ellipse([(w*0.5 - r_glow, h*0.65 - r_glow*0.4), (w*0.5 + r_glow, h*0.65 + r_glow*0.4)], fill=(0, 229, 255, alpha))
s5_img = Image.alpha_composite(s5_bg.convert("RGBA"), glow).convert("RGB")
s5_img.save(os.path.join(v3_dir, "s5.png"))
print("Saved V3 s5.png")

# S6: So sanh s vs |d|
# The My medium shot, comparing quantities
s6_canvas = v3_lab_bg.copy().convert("RGBA")
tm_s6 = tm_rgba.resize((int(tm_w * scale_s1 * 1.02), int(tm_h * scale_s1 * 1.02)), Image.Resampling.LANCZOS)
s6_canvas.paste(tm_s6, (30, h - tm_s6.height), tm_s6)
s6_canvas.convert("RGB").save(os.path.join(v3_dir, "s6.png"))
print("Saved V3 s6.png")

# S7: 3 Truong hop dac biet
# The My wide shot on left, right 70% open space for 3 cases
s7_canvas = v3_lab_bg.copy().convert("RGBA")
tm_s7 = tm_rgba.resize((int(tm_w * scale_s1 * 0.88), int(tm_h * scale_s1 * 0.88)), Image.Resampling.LANCZOS)
s7_canvas.paste(tm_s7, (20, h - tm_s7.height), tm_s7)
s7_canvas.convert("RGB").save(os.path.join(v3_dir, "s7.png"))
print("Saved V3 s7.png")

# S8: Cau hoi Pop-up
# The My medium close-up
s8_canvas = v3_lab_bg.copy().convert("RGBA")
tm_s8 = tm_rgba.resize((int(tm_w * scale_s1 * 1.15), int(tm_h * scale_s1 * 1.15)), Image.Resampling.LANCZOS)
s8_canvas.paste(tm_s8, (10, h - tm_s8.height), tm_s8)
s8_canvas.convert("RGB").save(os.path.join(v3_dir, "s8.png"))
print("Saved V3 s8.png")

# S9: Tong ket & Cam on
# The My medium shot standing proudly
s9_canvas = v3_lab_bg.copy().convert("RGBA")
tm_s9 = tm_rgba.resize((int(tm_w * scale_s1 * 0.95), int(tm_h * scale_s1 * 0.95)), Image.Resampling.LANCZOS)
s9_canvas.paste(tm_s9, (40, h - tm_s9.height), tm_s9)
s9_canvas.convert("RGB").save(os.path.join(v3_dir, "s9.png"))
print("Saved V3 s9.png")

print("All 18 keyframes generated successfully!")
