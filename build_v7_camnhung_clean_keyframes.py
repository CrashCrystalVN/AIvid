import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import numpy as np

WORK_DIR = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid"
KEYFRAMES_DIR = os.path.join(WORK_DIR, "keyframes", "V7_B5_Nhom2_TongHop_VanToc")
os.makedirs(KEYFRAMES_DIR, exist_ok=True)

TARGET_W, TARGET_H = 1376, 768

print("==================================================")
print("BUILDING CLEAN V7 KEYFRAMES (MC CAM NHUNG - ORIGINAL FICTIONAL CHARACTER)")
print("==================================================")

# ------------------------------------------------------------------------------
# 1. PREPARE CINEMATIC AVIATION GALLERY BACKGROUND
# ------------------------------------------------------------------------------
bg_src = os.path.join(WORK_DIR, "usaf_gallery.jpg")
bg_raw = Image.open(bg_src).convert("RGB")
bw, bh = bg_raw.size

target_bh = int(bw * TARGET_H / TARGET_W)
top_crop = int((bh - target_bh) * 0.44)
bg_cropped = bg_raw.crop((0, top_crop, bw, top_crop + target_bh)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)

# Cinematic shallow depth of field: Gaussian blur radius 5.5
bg_blur = bg_cropped.filter(ImageFilter.GaussianBlur(radius=5.5))
bg_blur = ImageEnhance.Brightness(bg_blur).enhance(0.92)
bg_blur = ImageEnhance.Color(bg_blur).enhance(0.96)
bg_blur = ImageEnhance.Contrast(bg_blur).enhance(1.02)

# ------------------------------------------------------------------------------
# 2. HELPER: DRAW ULTRA-DELICATE ANTI-ALIASED ROUND GLASSES (8X SUPERSAMPLING)
# ------------------------------------------------------------------------------
def add_round_glasses(img_rgba, cx1, cy1, cx2, cy2, r_px, pupil_dist):
    w, h = img_rgba.size
    scale = 8
    overlay = Image.new("RGBA", (w * scale, h * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # 8x coordinates
    scx1, scy1 = cx1 * scale, cy1 * scale
    scx2, scy2 = cx2 * scale, cy2 * scale
    sr = r_px * scale
    wire_w = int(1.15 * scale)
    
    frame_color = (68, 54, 46, 235)       # Elegant dark bronze wire
    gold_highlight = (195, 172, 130, 220) # Metallic warm gold sheen
    shadow_color = (35, 28, 22, 90)       # Soft contact shadow
    
    # Contact shadow slightly shifted down-right (1px)
    draw.ellipse([scx1 - sr + int(1*scale), scy1 - sr + int(1*scale), scx1 + sr + int(1*scale), scy1 + sr + int(1*scale)], outline=shadow_color, width=wire_w)
    draw.ellipse([scx2 - sr + int(1*scale), scy2 - sr + int(1*scale), scx2 + sr + int(1*scale), scy2 + sr + int(1*scale)], outline=shadow_color, width=wire_w)
    
    # Main metallic wire rims
    draw.ellipse([scx1 - sr, scy1 - sr, scx1 + sr, scy1 + sr], outline=frame_color, width=wire_w)
    draw.ellipse([scx2 - sr, scy2 - sr, scx2 + sr, scy2 + sr], outline=frame_color, width=wire_w)
    
    # Golden top-light reflection arc (from 215 to 325 degrees)
    draw.arc([scx1 - sr, scy1 - sr, scx1 + sr, scy1 + sr], start=215, end=325, fill=gold_highlight, width=int(0.9 * scale))
    draw.arc([scx2 - sr, scy2 - sr, scx2 + sr, scy2 + sr], start=215, end=325, fill=gold_highlight, width=int(0.9 * scale))
    
    # Elegant arched nose bridge (quadratic Bezier)
    mid_x = (scx1 + sr + scx2 - sr) / 2
    mid_y = min(scy1, scy2) - (3.8 * scale)
    bridge_pts = []
    for t in range(25):
        f = t / 24.0
        bx = (1-f)**2 * (scx1 + sr - 0.5*scale) + 2*(1-f)*f * mid_x + f**2 * (scx2 - sr + 0.5*scale)
        by = (1-f)**2 * (scy1 - 1.0*scale) + 2*(1-f)*f * mid_y + f**2 * (scy2 - 1.0*scale)
        bridge_pts.append((bx, by))
    draw.line(bridge_pts, fill=frame_color, width=wire_w)
    draw.line(bridge_pts, fill=gold_highlight, width=int(0.7 * scale))
    
    # Delicate nose pads
    draw.line([(scx1 + sr - 2*scale, scy1 + 4*scale), (scx1 + sr + 2.5*scale, scy1 + 9*scale)], fill=frame_color, width=int(0.9*scale))
    draw.line([(scx2 - sr + 2*scale, scy2 + 4*scale), (scx2 - sr - 2.5*scale, scy2 + 9*scale)], fill=frame_color, width=int(0.9*scale))
    
    # Temples extending to hairline/ears
    draw.line([(scx1 - sr + 1*scale, scy1 - 1.5*scale), (scx1 - sr - 26*scale, scy1 - 5*scale)], fill=frame_color, width=wire_w)
    draw.line([(scx2 + sr - 1*scale, scy2 - 1.5*scale), (scx2 + sr + 24*scale, scy2 - 5*scale)], fill=frame_color, width=wire_w)
    
    overlay_down = overlay.resize((w, h), Image.Resampling.LANCZOS)
    
    # Subtle anti-reflective coating glare (delicate soft diagonal sheen)
    glare_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d_glare = ImageDraw.Draw(glare_layer)
    d_glare.line([(cx1 - 6, cy1 - 8), (cx1 + 5, cy1 + 5)], fill=(255, 255, 255, 22), width=1)
    d_glare.line([(cx2 - 6, cy2 - 8), (cx2 + 5, cy2 + 5)], fill=(255, 255, 255, 22), width=1)
    
    res = Image.alpha_composite(img_rgba, glare_layer)
    res = Image.alpha_composite(res, overlay_down)
    return res

# ------------------------------------------------------------------------------
# 3. HELPER: APPLY PASTEL MINT CARDIGAN OVER WHITE BLOUSE (ZERO BADGES)
# ------------------------------------------------------------------------------
def apply_pastel_mint_cardigan(cutout_rgba, neck_center_x, v_neck_bottom_y=515):
    cw, ch = cutout_rgba.size
    
    # Inpaint / remove chest pocket badge and sleeve patch
    # Clean white fabric donor from left chest
    patch_clean = cutout_rgba.crop((neck_center_x - 30, 440, neck_center_x + 10, 490))
    cutout_rgba.paste(patch_clean.resize((60, 55)), (neck_center_x + 85, 440))
    sleeve_clean = cutout_rgba.crop((neck_center_x + 120, 480, neck_center_x + 145, 525))
    cutout_rgba.paste(sleeve_clean.resize((28, 45)), (neck_center_x + 180, 480))
    
    # Blouse opening mask: V-neck centered around neck_center_x
    mask_blouse = Image.new("L", (cw, ch), 0)
    d_blouse = ImageDraw.Draw(mask_blouse)
    v_blouse = [
        (neck_center_x - 55, 360),
        (neck_center_x + 50, 360),
        (neck_center_x + 35, 435),
        (neck_center_x + 15, v_neck_bottom_y),
        (neck_center_x - 15, v_neck_bottom_y),
        (neck_center_x - 35, 435),
        (neck_center_x - 55, 360)
    ]
    d_blouse.polygon(v_blouse, fill=255)
    mask_blouse = mask_blouse.filter(ImageFilter.GaussianBlur(radius=3.0))
    
    arr_img = np.array(cutout_rgba).astype(np.float32)
    arr_blouse = np.array(mask_blouse).astype(np.float32) / 255.0
    
    for y in range(365, ch):
        for x in range(cw):
            if arr_img[y, x, 3] > 30:
                r, g, b = arr_img[y, x, 0], arr_img[y, x, 1], arr_img[y, x, 2]
                is_skin = (r > 120) and (r - g > 16) and (r - b > 25)
                b_factor = arr_blouse[y, x]
                cardigan_factor = max(0.0, 1.0 - b_factor)
                
                if not is_skin and cardigan_factor > 0.05:
                    lum = (r * 0.299 + g * 0.587 + b * 0.114) / 255.0
                    # Cheerful soft pastel mint green
                    target_r = lum * 148.0 + 36.0
                    target_g = lum * 208.0 + 38.0
                    target_b = lum * 188.0 + 34.0
                    arr_img[y, x, 0] = arr_img[y, x, 0] * (1.0 - cardigan_factor) + target_r * cardigan_factor
                    arr_img[y, x, 1] = arr_img[y, x, 1] * (1.0 - cardigan_factor) + target_g * cardigan_factor
                    arr_img[y, x, 2] = arr_img[y, x, 2] * (1.0 - cardigan_factor) + target_b * cardigan_factor

    return Image.fromarray(np.clip(arr_img, 0, 255).astype(np.uint8))


# ==============================================================================
# 4. BUILD PRIMARY KEYFRAME s1.png (MC CAM NHUNG - HANDS GENTLY CLASPED)
# ==============================================================================
print("\n--- Generating Primary Keyframe: s1.png ---")
cutout1 = Image.open(os.path.join(WORK_DIR, "cutout_test_s1.png")).convert("RGBA")

# Apply Cardigan (neck centered at x=322)
camnhung_s1 = apply_pastel_mint_cardigan(cutout1, neck_center_x=322, v_neck_bottom_y=515)

# Add Delicate Round Glasses
# Eye positions on cutout1: left eye 340.5, 200.0; right eye 404.5, 204.5; radius 18
camnhung_s1 = add_round_glasses(camnhung_s1, cx1=340.5, cy1=200.0, cx2=404.5, cy2=204.5, r_px=18.0, pupil_dist=64.0)

# Composite onto Blurred Aviation Gallery Background
# Shift slightly left (-40px) to give 65% clean negative space on right
comp_s1 = bg_blur.copy().convert("RGBA")
comp_s1.paste(camnhung_s1, (-40, 0), camnhung_s1)
v7_s1 = comp_s1.convert("RGB")

# Gentle post-processing for studio crispness
v7_s1 = ImageEnhance.Sharpness(v7_s1).enhance(1.04)
v7_s1 = ImageEnhance.Contrast(v7_s1).enhance(1.02)

dst_s1 = os.path.join(KEYFRAMES_DIR, "s1.png")
v7_s1.save(dst_s1, "PNG")
print(f"[SUCCESS] Saved V7 s1.png: {dst_s1} ({v7_s1.size})")


# ==============================================================================
# 5. BUILD ALTERNATIVE BACKUP KEYFRAME s1_alt.png (MC CAM NHUNG - GENTLE WAVE)
# ==============================================================================
print("\n--- Generating Alternative Backup Keyframe: s1_alt.png ---")
cutout9 = Image.open(os.path.join(WORK_DIR, "cutout_test_s9.png")).convert("RGBA")

# Apply Cardigan (neck in s9 centered around x=375)
camnhung_alt = apply_pastel_mint_cardigan(cutout9, neck_center_x=375, v_neck_bottom_y=520)

# Add Delicate Round Glasses for s9
# Eye positions on s9: left eye 368.0, 206.0; right eye 442.0, 210.0; radius 19
camnhung_alt = add_round_glasses(camnhung_alt, cx1=368.0, cy1=206.0, cx2=442.0, cy2=210.0, r_px=19.0, pupil_dist=74.0)

comp_alt = bg_blur.copy().convert("RGBA")
# Shift -90px to place presenter firmly on left 35%, leaving 65% negative space on right
comp_alt.paste(camnhung_alt, (-90, 0), camnhung_alt)
v7_s1_alt = comp_alt.convert("RGB")

v7_s1_alt = ImageEnhance.Sharpness(v7_s1_alt).enhance(1.04)
v7_s1_alt = ImageEnhance.Contrast(v7_s1_alt).enhance(1.02)

dst_s1_alt = os.path.join(KEYFRAMES_DIR, "s1_alt.png")
v7_s1_alt.save(dst_s1_alt, "PNG")
print(f"[SUCCESS] Saved V7 s1_alt.png: {dst_s1_alt} ({v7_s1_alt.size})")


# ==============================================================================
# 6. BUILD OUTRO KEYFRAME s5.png (MC CAM NHUNG - WARM CLOSING APPRECIATION)
# ==============================================================================
print("\n--- Generating Outro Keyframe: s5.png ---")
# Crop-in framing (medium close-up presenter appreciation) for engaging conclusion
# Focus on MC Cam Nhung with warm gratitude
crop_box = (15, 10, int(TARGET_W * 0.94), int(TARGET_H * 0.94))
v7_s5 = v7_s1.crop(crop_box).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
v7_s5 = ImageEnhance.Brightness(v7_s5).enhance(1.03)
v7_s5 = ImageEnhance.Color(v7_s5).enhance(1.02)
v7_s5 = ImageEnhance.Sharpness(v7_s5).enhance(1.06)

dst_s5 = os.path.join(KEYFRAMES_DIR, "s5.png")
v7_s5.save(dst_s5, "PNG")
print(f"[SUCCESS] Saved V7 s5.png: {dst_s5} ({v7_s5.size})")

print("\n==================================================")
print("ALL 3 V7 KEYFRAMES BUILT SUCCESSFULLY!")
print("==================================================")
