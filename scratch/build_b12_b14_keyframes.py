import os
import math
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageOps
import numpy as np

WORK_DIR = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid"
DOWNLOADS_DIR = os.path.join(WORK_DIR, "scratch", "downloads")
KEYFRAMES_DIR = os.path.join(WORK_DIR, "keyframes")

B12_DIR = os.path.join(KEYFRAMES_DIR, "B12_ChuyenDongNem")
B14_DIR = os.path.join(KEYFRAMES_DIR, "B14_DinhLuat1Newton")

os.makedirs(B12_DIR, exist_ok=True)
os.makedirs(B14_DIR, exist_ok=True)

TARGET_W, TARGET_H = 1376, 768

print("==================================================")
print("BUILDING 10 CLEAN 16:9 KEYFRAMES FOR B12 & B14")
print("==================================================")

# Load donor assets
cutout_mc = Image.open(os.path.join(WORK_DIR, "test_perfect_s1_cutout.png")).convert("RGBA") # Cô Nhung cutout
full_mc_s1 = Image.open(os.path.join(WORK_DIR, "test_full_s1_perfect.png")).convert("RGB")
smithsonian = Image.open(os.path.join(WORK_DIR, "smithsonian_gallery.jpg")).convert("RGB")
usaf_gallery = Image.open(os.path.join(WORK_DIR, "usaf_gallery.jpg")).convert("RGB")

galileo_ramp = Image.open(os.path.join(DOWNLOADS_DIR, "galileo_ramp.jpg")).convert("RGB")
voyager_model = Image.open(os.path.join(DOWNLOADS_DIR, "voyager_model.png")).convert("RGBA")
voyager_space = Image.open(os.path.join(DOWNLOADS_DIR, "voyager_space.jpg")).convert("RGB")
nebula_hubble = Image.open(os.path.join(DOWNLOADS_DIR, "nebula_hubble.jpg")).convert("RGB")
skateboard = Image.open(os.path.join(DOWNLOADS_DIR, "skateboard.jpg")).convert("RGB")

# Helper function: Crop and resize to 16:9 (1376x768)
def crop_16_9(img, focus_x=0.5, focus_y=0.5):
    iw, ih = img.size
    target_ih = int(iw * TARGET_H / TARGET_W)
    if target_ih <= ih:
        top = int((ih - target_ih) * focus_y)
        return img.crop((0, top, iw, top + target_ih)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    else:
        target_iw = int(ih * TARGET_W / TARGET_H)
        left = int((iw - target_iw) * focus_x)
        return img.crop((left, 0, left + target_iw, ih)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)

# Helper: Create dark vignette/negative space gradient on right side
def apply_right_negative_space(base_img, start_pct=0.35, max_darkness=0.75, tint_color=(8, 14, 28)):
    w, h = base_img.size
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    start_x = int(w * start_pct)
    for x in range(start_x, w):
        ratio = (x - start_x) / (w - start_x)
        # Smooth ease in curve
        alpha = int(255 * max_darkness * (ratio ** 1.3))
        d.line([(x, 0), (x, h)], fill=(tint_color[0], tint_color[1], tint_color[2], alpha))
    return Image.alpha_composite(base_img.convert("RGBA"), overlay).convert("RGB")

# ==============================================================================
# BÀI 12: CHUYỂN ĐỘNG NÉM (5 CẢNH)
# ==============================================================================
print("\n--- Generating Bài 12 Keyframes ---")

# B12_S1: Intro - Hiện tượng ném bóng thể thao trong đời sống (MC Cô Nhung)
# Background: High-tech mechanics sports lab, MC on left, right 65% clean space
bg_s1 = crop_16_9(usaf_gallery, focus_x=0.3, focus_y=0.45).filter(ImageFilter.GaussianBlur(radius=6.0))
bg_s1 = ImageEnhance.Brightness(bg_s1).enhance(0.85)
bg_s1 = apply_right_negative_space(bg_s1, start_pct=0.32, max_darkness=0.82, tint_color=(5, 12, 24))
# Composite MC
b12_s1 = Image.alpha_composite(bg_s1.convert("RGBA"), cutout_mc).convert("RGB")
b12_s1.save(os.path.join(B12_DIR, "s1.png"), "PNG")
print("Saved B12_S1 (Intro): s1.png")

# B12_S2: Thí nghiệm ném ngang 2 viên bi A và B rơi tự do vs ném ngang
# High-tech physics laboratory workbench with mechanical launch rig on left
bg_s2 = crop_16_9(smithsonian, focus_x=0.2, focus_y=0.55).filter(ImageFilter.GaussianBlur(radius=3.5))
bg_s2 = ImageEnhance.Brightness(bg_s2).enhance(0.90)
bg_s2 = ImageEnhance.Contrast(bg_s2).enhance(1.08)
bg_s2 = apply_right_negative_space(bg_s2, start_pct=0.38, max_darkness=0.78, tint_color=(7, 15, 30))
# Add subtle metallic spheres on a sleek launch platform at left (x=240, y=280)
draw_s2 = ImageDraw.Draw(bg_s2)
# Rig stand (subtle mechanics)
draw_s2.rounded_rectangle([180, 270, 320, 282], radius=4, fill=(50, 65, 85), outline=(90, 120, 160))
draw_s2.rectangle([245, 282, 255, 620], fill=(40, 50, 68))
# Sphere A (chrome / steel ball)
draw_s2.ellipse([200, 235, 236, 271], fill=(180, 205, 225), outline=(220, 240, 255))
# Sphere B (chrome / steel ball)
draw_s2.ellipse([265, 235, 301, 271], fill=(180, 205, 225), outline=(220, 240, 255))
# Floor base
draw_s2.rectangle([140, 620, 360, 635], fill=(30, 42, 58))
b12_s2 = bg_s2.filter(ImageFilter.SMOOTH_MORE)
b12_s2.save(os.path.join(B12_DIR, "s2.png"), "PNG")
print("Saved B12_S2 (Thí nghiệm bi A & B): s2.png")

# B12_S3: Phân tích & công thức ném ngang (Oy rơi tự do, Ox thẳng đều)
# Sleek dark tech physics lab, MC Cô Nhung on left, 70% negative space on right
bg_s3 = crop_16_9(usaf_gallery, focus_x=0.6, focus_y=0.4).filter(ImageFilter.GaussianBlur(radius=8.0))
bg_s3 = ImageEnhance.Brightness(bg_s3).enhance(0.78)
bg_s3 = apply_right_negative_space(bg_s3, start_pct=0.30, max_darkness=0.88, tint_color=(4, 10, 22))
b12_s3 = Image.alpha_composite(bg_s3.convert("RGBA"), cutout_mc).convert("RGB")
b12_s3.save(os.path.join(B12_DIR, "s3.png"), "PNG")
print("Saved B12_S3 (Phân tích ném ngang): s3.png")

# B12_S4: Chuyển động ném xiên & quỹ đạo Parabol
# Launcher angled upwards on left, wide twilight/cyan sky on right (70% negative space)
bg_s4 = crop_16_9(smithsonian, focus_x=0.4, focus_y=0.3).filter(ImageFilter.GaussianBlur(radius=4.5))
bg_s4 = ImageEnhance.Color(bg_s4).enhance(0.85)
bg_s4 = ImageEnhance.Brightness(bg_s4).enhance(0.82)
# Gradient sky transition
overlay_s4 = Image.new("RGBA", (TARGET_W, TARGET_H), (0, 0, 0, 0))
d_s4 = ImageDraw.Draw(overlay_s4)
for y in range(TARGET_H):
    alpha = int(180 * (1.0 - y / TARGET_H))
    d_s4.line([(0, y), (TARGET_W, y)], fill=(6, 16, 36, alpha))
bg_s4 = Image.alpha_composite(bg_s4.convert("RGBA"), overlay_s4).convert("RGB")
bg_s4 = apply_right_negative_space(bg_s4, start_pct=0.35, max_darkness=0.75, tint_color=(5, 14, 28))
# Launcher barrel angled 45 degrees at bottom-left
d_s4_draw = ImageDraw.Draw(bg_s4)
# Turret mount
d_s4_draw.ellipse([140, 520, 260, 640], fill=(45, 58, 76), outline=(80, 110, 145))
# Angled barrel
d_s4_draw.polygon([(185, 545), (280, 450), (298, 468), (203, 563)], fill=(70, 90, 115), outline=(120, 155, 195))
b12_s4 = bg_s4.filter(ImageFilter.SMOOTH_MORE)
b12_s4.save(os.path.join(B12_DIR, "s4.png"), "PNG")
print("Saved B12_S4 (Ném xiên & Parabol): s4.png")

# B12_S5: Công thức tầm cao H, tầm xa L, góc cực đại 45 độ & Tổng kết
# MC Cô Nhung smiling on left, warm ambient lighting, 65% clean space on right
bg_s5 = crop_16_9(usaf_gallery, focus_x=0.25, focus_y=0.4).filter(ImageFilter.GaussianBlur(radius=5.5))
bg_s5 = ImageEnhance.Brightness(bg_s5).enhance(0.88)
bg_s5 = ImageEnhance.Color(bg_s5).enhance(1.05)
bg_s5 = apply_right_negative_space(bg_s5, start_pct=0.33, max_darkness=0.82, tint_color=(6, 12, 26))
b12_s5 = Image.alpha_composite(bg_s5.convert("RGBA"), cutout_mc).convert("RGB")
b12_s5.save(os.path.join(B12_DIR, "s5.png"), "PNG")
print("Saved B12_S5 (Tổng kết công thức): s5.png")

# ==============================================================================
# BÀI 14: ĐỊNH LUẬT 1 NEWTON (5 CẢNH)
# ==============================================================================
print("\n--- Generating Bài 14 Keyframes ---")

# B14_S1: Intro - Lịch sử & Đặt vấn đề: Quan niệm Aristotle vs Thí nghiệm máng nghiêng Galilei
# Authentic Galileo inclined plane from Museo Galileo Florence cropped 16:9 on left, negative space on right
ramp_cropped = crop_16_9(galileo_ramp, focus_x=0.18, focus_y=0.55)
ramp_blur = ramp_cropped.filter(ImageFilter.GaussianBlur(radius=1.5))
ramp_blur = ImageEnhance.Contrast(ramp_blur).enhance(1.10)
ramp_blur = ImageEnhance.Color(ramp_blur).enhance(1.05)
b14_s1 = apply_right_negative_space(ramp_blur, start_pct=0.38, max_darkness=0.84, tint_color=(12, 10, 16))
b14_s1.save(os.path.join(B14_DIR, "s1.png"), "PNG")
print("Saved B14_S1 (Máng nghiêng Galilei): s1.png")

# B14_S2: Nội dung Định luật 1 Newton (1687) - Hợp lực = 0
# MC Cô Nhung on left, deep cobalt / dark navy background, 70% negative space on right
bg_b14_s2 = crop_16_9(smithsonian, focus_x=0.7, focus_y=0.5).filter(ImageFilter.GaussianBlur(radius=7.5))
bg_b14_s2 = ImageEnhance.Brightness(bg_b14_s2).enhance(0.76)
bg_b14_s2 = ImageEnhance.Color(bg_b14_s2).enhance(0.9)
# Deep cobalt blue tone
r, g, b = bg_b14_s2.split()
b = ImageEnhance.Brightness(b).enhance(1.18)
r = ImageEnhance.Brightness(r).enhance(0.85)
bg_b14_s2 = Image.merge("RGB", (r, g, b))
bg_b14_s2 = apply_right_negative_space(bg_b14_s2, start_pct=0.32, max_darkness=0.85, tint_color=(4, 8, 24))
b14_s2 = Image.alpha_composite(bg_b14_s2.convert("RGBA"), cutout_mc).convert("RGB")
b14_s2.save(os.path.join(B14_DIR, "s2.png"), "PNG")
print("Saved B14_S2 (Định luật 1 Newton): s2.png")

# B14_S3: Minh họa 2 ví dụ SGK: Quả cầu treo dây (P + T = 0) và Người trượt ván
# Hanging pendulum on left + smooth frictionless track, clean upper/right space
skate_cropped = crop_16_9(skateboard, focus_x=0.25, focus_y=0.5).filter(ImageFilter.GaussianBlur(radius=3.0))
skate_cropped = ImageEnhance.Brightness(skate_cropped).enhance(0.80)
skate_cropped = ImageEnhance.Contrast(skate_cropped).enhance(1.06)
# Left side: add suspension apparatus for hanging sphere
d_s3 = ImageDraw.Draw(skate_cropped)
# Stand bar
d_s3.rectangle([120, 60, 280, 75], fill=(45, 55, 70), outline=(80, 100, 130))
d_s3.rectangle([135, 75, 145, 450], fill=(40, 50, 65))
# Hanging wire
d_s3.line([(240, 75), (240, 310)], fill=(180, 195, 215), width=2)
# Spherical bob
d_s3.ellipse([220, 310, 260, 350], fill=(190, 210, 230), outline=(230, 245, 255))
b14_s3 = apply_right_negative_space(skate_cropped, start_pct=0.40, max_darkness=0.80, tint_color=(6, 14, 28))
b14_s3.save(os.path.join(B14_DIR, "s3.png"), "PNG")
print("Saved B14_S3 (Quả cầu treo & ván trượt): s3.png")

# B14_S4: Khái niệm Quán tính & Tàu không gian Voyager trong vũ trụ
# Deep space nebula background with NASA Voyager spacecraft on left, infinite starfield on right
nebula_bg = crop_16_9(nebula_hubble, focus_x=0.5, focus_y=0.5)
nebula_bg = ImageEnhance.Brightness(nebula_bg).enhance(0.70)
# Composite Voyager spacecraft on left side (scaled down to fit 400x350 at x=120, y=180)
vw, vh = voyager_model.size
scale_v = 420.0 / max(vw, vh)
voyager_scaled = voyager_model.resize((int(vw * scale_v), int(vh * scale_v)), Image.Resampling.LANCZOS)
nebula_bg.paste(voyager_scaled, (100, 170), voyager_scaled)
b14_s4 = apply_right_negative_space(nebula_bg, start_pct=0.45, max_darkness=0.82, tint_color=(2, 4, 12))
b14_s4.save(os.path.join(B14_DIR, "s4.png"), "PNG")
print("Saved B14_S4 (Tàu Voyager & Quán tính): s4.png")

# B14_S5: Trắc nghiệm củng cố (v = 3 m/s) & Tổng kết
# MC Cô Nhung smiling encouragingly on left, high-tech education studio, 70% negative space on right
bg_b14_s5 = crop_16_9(usaf_gallery, focus_x=0.5, focus_y=0.45).filter(ImageFilter.GaussianBlur(radius=6.0))
bg_b14_s5 = ImageEnhance.Brightness(bg_b14_s5).enhance(0.85)
bg_b14_s5 = ImageEnhance.Color(bg_b14_s5).enhance(1.06)
bg_b14_s5 = apply_right_negative_space(bg_b14_s5, start_pct=0.32, max_darkness=0.84, tint_color=(6, 12, 25))
b14_s5 = Image.alpha_composite(bg_b14_s5.convert("RGBA"), cutout_mc).convert("RGB")
b14_s5.save(os.path.join(B14_DIR, "s5.png"), "PNG")
print("Saved B14_S5 (Trắc nghiệm củng cố): s5.png")

print("\nALL 10 KEYFRAMES GENERATED SUCCESSFULLY!")
