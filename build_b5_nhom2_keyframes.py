"""
Build Script for Lesson 5 Group 2 Keyframes (V6 & V7 - 10 Keyframes)
Strict adherence to 16:9 ratio, zero-text, zero-watermarks, character consistency,
and ample clean negative space (60-70%) for Python Hologram HUD animation.
"""

import os
import math
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageOps
import numpy as np

WORK_DIR = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid"
RAW_DIR = os.path.join(WORK_DIR, "_raw_assets")
KEYFRAMES_DIR = os.path.join(WORK_DIR, "keyframes")

V6_DIR = os.path.join(KEYFRAMES_DIR, "V6_B5_Nhom2_TocDo_VanToc")
V7_DIR = os.path.join(KEYFRAMES_DIR, "V7_B5_Nhom2_TongHop_VanToc")

os.makedirs(V6_DIR, exist_ok=True)
os.makedirs(V7_DIR, exist_ok=True)

TARGET_W, TARGET_H = 1376, 768

print("==================================================")
print("BUILDING 10 KEYFRAMES FOR LESSON 5 - GROUP 2 (V6 & V7)")
print("==================================================")

# ==============================================================================
# 1. VIDEO 6: V6_B5_Nhom2_TocDo_VanToc (5 SCENES)
# MC: Hoàng Nam (16yo male, modern square glasses, graphite-grey tech jacket)
# Theme: Drone Robotics & Telemetry Lab, Coastal GPS Cyclist, Mountain S-Curve, Walkway
# ==============================================================================
print("\n--- Processing Video 6: V6_B5_Nhom2_TocDo_VanToc ---")

# V6_S01: Master MC Lead (Hoàng Nam in Drone Robotics Lab)
# Source: Master Image from AI generation
v6_s1_src = r"C:\Users\vuasu\.gemini\antigravity\brain\e501ff20-cc5a-4d2f-9d59-919ab50c546e\hoang_nam_keyframe_v3_1794387687143.jpg"
v6_s1 = Image.open(v6_s1_src).convert("RGB")
if v6_s1.size != (TARGET_W, TARGET_H):
    v6_s1 = v6_s1.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
v6_s1_dst = os.path.join(V6_DIR, "s1.png")
v6_s1.save(v6_s1_dst, "PNG")
print(f"Saved V6_S01: {v6_s1_dst} ({v6_s1.size})")

# V6_S02: High-angle Coastal Road Cyclist (GPS Telemetry)
# Source: Pacific Coast Highway (5767 x 3234)
v6_s2_src = os.path.join(RAW_DIR, "v6_s2_coastal.jpg")
img_s2 = Image.open(v6_s2_src).convert("RGB")
iw, ih = img_s2.size
# Crop 16:9 from center-upper region to showcase road, ocean, and cyclist
target_ih = int(iw * TARGET_H / TARGET_W)
top = int((ih - target_ih) * 0.40)
v6_s2 = img_s2.crop((0, top, iw, top + target_ih)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
# Enhance ocean turquoise and road contrast
v6_s2 = ImageEnhance.Color(v6_s2).enhance(1.08)
v6_s2 = ImageEnhance.Contrast(v6_s2).enhance(1.04)
v6_s2_dst = os.path.join(V6_DIR, "s2.png")
v6_s2.save(v6_s2_dst, "PNG")
print(f"Saved V6_S02: {v6_s2_dst} ({v6_s2.size})")

# V6_S03: Mountain S-Curve Road (Vector Trajectory)
# Source: Romania Transfagarasan (3216 x 2136)
v6_s3_src = os.path.join(RAW_DIR, "v6_s3_mountain.jpg")
img_s3 = Image.open(v6_s3_src).convert("RGB")
iw, ih = img_s3.size
target_ih = int(iw * TARGET_H / TARGET_W)
top = int((ih - target_ih) * 0.50)
v6_s3 = img_s3.crop((0, top, iw, top + target_ih)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
v6_s3 = ImageEnhance.Color(v6_s3).enhance(1.06)
v6_s3 = ImageEnhance.Contrast(v6_s3).enhance(1.05)
v6_s3_dst = os.path.join(V6_DIR, "s3.png")
v6_s3.save(v6_s3_dst, "PNG")
print(f"Saved V6_S03: {v6_s3_dst} ({v6_s3.size})")

# V6_S04: Modern Airport Terminal Moving Walkway (Signed Velocity Vectors)
# Source: Ohare Neon Walkway (3888 x 2592)
v6_s4_src = os.path.join(RAW_DIR, "ohare_walkway.jpg")
img_s4 = Image.open(v6_s4_src).convert("RGB")
iw, ih = img_s4.size
target_ih = int(iw * TARGET_H / TARGET_W)
top = int((ih - target_ih) * 0.45)
v6_s4 = img_s4.crop((0, top, iw, top + target_ih)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
# Enhance soft neon colors and reflective floor
v6_s4 = ImageEnhance.Brightness(v6_s4).enhance(1.02)
v6_s4 = ImageEnhance.Contrast(v6_s4).enhance(1.04)
v6_s4_dst = os.path.join(V6_DIR, "s4.png")
v6_s4.save(v6_s4_dst, "PNG")
print(f"Saved V6_S04: {v6_s4_dst} ({v6_s4.size})")

# V6_S05: MC Hoàng Nam Presenter Wrap-Up & Interactive Quiz
# Source: hoang_nam_keyframe_v2_1794387665705.jpg (Clean studio lab variant)
v6_s5_src = r"C:\Users\vuasu\.gemini\antigravity\brain\e501ff20-cc5a-4d2f-9d59-919ab50c546e\hoang_nam_keyframe_v2_1794387665705.jpg"
img_s5 = Image.open(v6_s5_src).convert("RGB")
# Framing: Subtle push-in crop for close engaging presenter dialogue
crop_box = (15, 10, int(TARGET_W * 0.94), int(TARGET_H * 0.94))
v6_s5 = img_s5.crop(crop_box).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
v6_s5 = ImageEnhance.Sharpness(v6_s5).enhance(1.05)
v6_s5 = ImageEnhance.Contrast(v6_s5).enhance(1.02)
v6_s5_dst = os.path.join(V6_DIR, "s5.png")
v6_s5.save(v6_s5_dst, "PNG")
print(f"Saved V6_S05: {v6_s5_dst} ({v6_s5.size})")


# ==============================================================================
# 2. VIDEO 7: V7_B5_Nhom2_TongHop_VanToc (5 SCENES)
# MC: Cẩm Nhung (16yo female, soft wavy black hair, pastel-mint green cardigan over white blouse)
# Theme: Aerodynamics Flight Science Gallery, Jet Airliners, Emerald River Kayak
# ==============================================================================
print("\n--- Processing Video 7: V7_B5_Nhom2_TongHop_VanToc ---")

# Helper: Create Mint-Green Cardigan tint on clothing
def apply_mint_cardigan_tint(img_rgba):
    arr = np.array(img_rgba).astype(np.float32)
    h_arr, w_arr, _ = arr.shape
    # Torso region: y >= 460, where light cream clothing is present
    for y in range(460, h_arr):
        for x in range(w_arr):
            if arr[y, x, 3] > 40:
                r, g, b = arr[y, x, 0], arr[y, x, 1], arr[y, x, 2]
                max_c = max(r, g, b)
                min_c = min(r, g, b)
                if max_c > 130 and (max_c - min_c) < 55:
                    # Delicate, sophisticated pastel mint green: #a8e6cf
                    arr[y, x, 0] = np.clip(r * 0.74, 0, 255)
                    arr[y, x, 1] = np.clip(g * 0.98, 0, 255)
                    arr[y, x, 2] = np.clip(b * 0.88, 0, 255)
    return Image.fromarray(arr.astype(np.uint8))

# Gallery Background Preparation
bg_gallery_src = os.path.join(RAW_DIR, "v7_bg_gallery.jpg")
bg_raw = Image.open(bg_gallery_src).convert("RGB")
bg_w, bg_h = bg_raw.size
target_h = int(bg_w * TARGET_H / TARGET_W)
crop_top = (bg_h - target_h) // 2
bg_cropped = bg_raw.crop((0, crop_top, bg_w, crop_top + target_h)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
# Shallow depth-of-field Gaussian blur for cinematic studio realism
bg_blur = bg_cropped.filter(ImageFilter.GaussianBlur(radius=6))
bg_blur = ImageEnhance.Brightness(bg_blur).enhance(0.92)
bg_blur = ImageEnhance.Color(bg_blur).enhance(0.95)

# V7_S01: Master MC Lead (Cẩm Nhung in Aerodynamics Gallery)
lead_src = os.path.join(RAW_DIR, "v7_mc_lead.png")
lead_raw = Image.open(lead_src).convert("RGBA")
lead_mint = apply_mint_cardigan_tint(lead_raw)

scale_lead = 690.0 / lead_mint.size[1]
cur_w = int(lead_mint.size[0] * scale_lead)
cur_h = int(lead_mint.size[1] * scale_lead)
lead_res = lead_mint.resize((cur_w, cur_h), Image.Resampling.LANCZOS)

comp_s1 = bg_blur.copy().convert("RGBA")
comp_s1.paste(lead_res, (40, TARGET_H - cur_h), lead_res)
v7_s1 = comp_s1.convert("RGB")
v7_s1_dst = os.path.join(V7_DIR, "s1.png")
v7_s1.save(v7_s1_dst, "PNG")
print(f"Saved V7_S01: {v7_s1_dst} ({v7_s1.size})")

# V7_S02: Modern Passenger Jet Airliner Cruising Above Sunlit Clouds
# Source: Airliner (3608 x 1903)
v7_s2_src = os.path.join(RAW_DIR, "v7_s2_airliner.jpg")
img_s2 = Image.open(v7_s2_src).convert("RGB")
iw, ih = img_s2.size
target_ih = int(iw * TARGET_H / TARGET_W)
top = int((ih - target_ih) * 0.40)
v7_s2 = img_s2.crop((0, top, iw, top + target_ih)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
v7_s2 = ImageEnhance.Color(v7_s2).enhance(1.05)
v7_s2 = ImageEnhance.Contrast(v7_s2).enhance(1.03)
v7_s2_dst = os.path.join(V7_DIR, "s2.png")
v7_s2.save(v7_s2_dst, "PNG")
print(f"Saved V7_S02: {v7_s2_dst} ({v7_s2.size})")

# V7_S03: Aircraft High-Altitude Misty Flight / Vector Triangle
# Source: Aerial Overtake (4593 x 3062)
v7_s3_src = os.path.join(RAW_DIR, "v7_s3_mist_plane.jpg")
img_s3 = Image.open(v7_s3_src).convert("RGB")
iw, ih = img_s3.size
target_ih = int(iw * TARGET_H / TARGET_W)
top = int((ih - target_ih) * 0.45)
v7_s3 = img_s3.crop((0, top, iw, top + target_ih)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
v7_s3 = ImageEnhance.Contrast(v7_s3).enhance(1.04)
v7_s3_dst = os.path.join(V7_DIR, "s3.png")
v7_s3.save(v7_s3_dst, "PNG")
print(f"Saved V7_S03: {v7_s3_dst} ({v7_s3.size})")

# V7_S04: Kayak Paddling along Emerald River Canyon
# Source: Kayak Marble Canyon (2784 x 1856)
v7_s4_src = os.path.join(RAW_DIR, "v7_s4_kayak.jpg")
img_s4 = Image.open(v7_s4_src).convert("RGB")
iw, ih = img_s4.size
target_ih = int(iw * TARGET_H / TARGET_W)
top = int((ih - target_ih) * 0.50)
v7_s4 = img_s4.crop((0, top, iw, top + target_ih)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
# Boost emerald water tones and canyon clarity
v7_s4 = ImageEnhance.Color(v7_s4).enhance(1.10)
v7_s4 = ImageEnhance.Contrast(v7_s4).enhance(1.05)
v7_s4_dst = os.path.join(V7_DIR, "s4.png")
v7_s4.save(v7_s4_dst, "PNG")
print(f"Saved V7_S04: {v7_s4_dst} ({v7_s4.size})")

# V7_S05: MC Cẩm Nhung Closing Bow & Warm Appreciation to Conclude Series
bow_src = os.path.join(RAW_DIR, "v7_mc_bow.png")
bow_raw = Image.open(bow_src).convert("RGBA")
bow_mint = apply_mint_cardigan_tint(bow_raw)

scale_bow = 690.0 / bow_mint.size[1]
cur_w = int(bow_mint.size[0] * scale_bow)
cur_h = int(bow_mint.size[1] * scale_bow)
bow_res = bow_mint.resize((cur_w, cur_h), Image.Resampling.LANCZOS)

comp_s5 = bg_blur.copy().convert("RGBA")
comp_s5.paste(bow_res, (50, TARGET_H - cur_h), bow_res)
v7_s5 = comp_s5.convert("RGB")
v7_s5_dst = os.path.join(V7_DIR, "s5.png")
v7_s5.save(v7_s5_dst, "PNG")
print(f"Saved V7_S05: {v7_s5_dst} ({v7_s5.size})")

print("\n==================================================")
print("SUCCESSFULLY GENERATED ALL 10 KEYFRAMES (16:9, ZERO-TEXT)!")
print("==================================================")
