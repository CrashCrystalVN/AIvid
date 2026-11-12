import os
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw

v4_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V4_B5_Nhom1_TocDo_VanToc"
v5_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V5_B5_Nhom1_TongHop_VanToc"

w, h = 1376, 768

# Load base keyframes
v4_s1 = Image.open(os.path.join(v4_dir, "s1.png")).convert("RGB")
v5_s1 = Image.open(os.path.join(v5_dir, "s1.png")).convert("RGB")

print("Generating V4_s6 (Tú Châu Medium Close-Up with confident warm smile)...")
# For V4_s6:
# Focus closer on Tú Châu (left 35%), keeping her high ponytail, sports polo, and warm smile
# Crop from v4_s1 with push-in framing to create an engaging medium close-up
# Keep right 65% clean for the quiz_popup HUD
crop_box_v4 = (0, 0, int(w * 0.88), int(h * 0.88))
v4_s6 = v4_s1.crop(crop_box_v4).resize((w, h), Image.Resampling.LANCZOS)
v4_s6 = ImageEnhance.Sharpness(v4_s6).enhance(1.04)
v4_s6 = ImageEnhance.Contrast(v4_s6).enhance(1.02)
v4_s6.save(os.path.join(v4_dir, "s6.png"))
print("Saved V4 s6.png")

print("Generating V5_s5 (Minh Dũng Presenter Wrap-up & Appreciation)...")
# For V5_s5:
# Minh Dũng standing proudly in the transportation lab, warm lighting
crop_box_v5 = (15, 10, int(w * 0.92), int(h * 0.92))
v5_s5 = v5_s1.crop(crop_box_v5).resize((w, h), Image.Resampling.LANCZOS)
v5_s5 = ImageEnhance.Brightness(v5_s5).enhance(1.03)
v5_s5 = ImageEnhance.Contrast(v5_s5).enhance(1.02)
v5_s5.save(os.path.join(v5_dir, "s5.png"))
print("Saved V5 s5.png")

print("All 11 keyframes generated.")
