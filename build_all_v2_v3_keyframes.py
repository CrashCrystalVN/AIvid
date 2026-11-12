import os
import math
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import numpy as np

v2_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V2_B4_DoDichChuyen_QuangDuong"
v3_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V3_B4_TongHop_DoDichChuyen"
os.makedirs(v2_dir, exist_ok=True)
os.makedirs(v3_dir, exist_ok=True)

# 1. Base assets
v2_s1 = Image.open(os.path.join(v2_dir, "s1.png")).convert("RGB")
v2_s2 = Image.open(os.path.join(v2_dir, "s2.png")).convert("RGB")
v3_s3 = Image.open(os.path.join(v3_dir, "s3.png")).convert("RGB")
v1_s1 = Image.open(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V1_B4_ViTri_HeQuyChieu\s1.png").convert("RGB")
v1_s4 = Image.open(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V1_B4_ViTri_HeQuyChieu\s4.png").convert("RGB")
v1_s7 = Image.open(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V1_B4_ViTri_HeQuyChieu\s7.png").convert("RGB")
v1_s8 = Image.open(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V1_B4_ViTri_HeQuyChieu\s8.png").convert("RGB")

w, h = 1376, 768

# Extract clean studio background from v2_s1 (right part has no person)
# In v2_s1, person is roughly x: 0 to 520, y: 0 to 768.
# The right part x: 500 to 1376 is a pure modern studio.
studio_bg_v2 = v2_s1.crop((480, 0, 1376, 768)).resize((w, h), Image.Resampling.LANCZOS)
studio_bg_v1 = v1_s1.crop((450, 0, 1376, 768)).resize((w, h), Image.Resampling.LANCZOS)

# Extract Huu Trong character from v2_s1
# Huu Trong box: (120, 60, 520, 768)
huu_trong_crop = v2_s1.crop((120, 60, 510, 768))

print("Huu Trong crop size:", huu_trong_crop.size)
print("Base assets ready.")
