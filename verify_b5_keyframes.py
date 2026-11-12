import os
from PIL import Image

v4_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V4_B5_Nhom1_TocDo_VanToc"
v5_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\keyframes\V5_B5_Nhom1_TongHop_VanToc"

v4_scenes = ["s1.png", "s2.png", "s3.png", "s4.png", "s5.png", "s6.png"]
v5_scenes = ["s1.png", "s2.png", "s3.png", "s4.png", "s5.png"]

print("=== VERIFYING V4 KEYFRAMES ===")
for s in v4_scenes:
    p = os.path.join(v4_dir, s)
    assert os.path.exists(p), f"Missing {p}"
    im = Image.open(p)
    size_kb = os.path.getsize(p) / 1024
    print(f"V4 {s}: {im.size} | {im.mode} | {size_kb:.1f} KB - OK")

print("\n=== VERIFYING V5 KEYFRAMES ===")
for s in v5_scenes:
    p = os.path.join(v5_dir, s)
    assert os.path.exists(p), f"Missing {p}"
    im = Image.open(p)
    size_kb = os.path.getsize(p) / 1024
    print(f"V5 {s}: {im.size} | {im.mode} | {size_kb:.1f} KB - OK")

print("\nTotal 11/11 keyframes verified successfully!")
