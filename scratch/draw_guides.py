import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

audit_dir = Path(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\scratch\flow_frame_audit")
annotated_dir = audit_dir / "annotated"
annotated_dir.mkdir(exist_ok=True)

# Grid lines of interest on 1920x1080
# x = 780 (Standard split left/right)
# x = 960 (Center screen)
# x = 1040 (Shifted safe zone for wide MC)
# x = 1860 (Right margin)

jpg_files = sorted(audit_dir.glob("*.jpg"))

for img_path in jpg_files:
    if img_path.parent == annotated_dir:
        continue
    img = Image.open(img_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    # Draw vertical guide lines
    # x = 780 (Yellow dashed or solid line)
    draw.line([(780, 0), (780, 1080)], fill=(255, 215, 0), width=3)
    # x = 960 (White center line)
    draw.line([(960, 0), (960, 1080)], fill=(255, 255, 255), width=2)
    # x = 1040 (Cyan shifted safe line)
    draw.line([(1040, 0), (1040, 1080)], fill=(0, 255, 255), width=3)
    # x = 1860 (Red right margin)
    draw.line([(1860, 0), (1860, 1080)], fill=(255, 50, 50), width=2)
    
    # Label top
    draw.rectangle([(720, 10), (840, 45)], fill=(0, 0, 0, 180))
    draw.text((730, 15), "x=780", fill=(255, 215, 0))
    
    draw.rectangle([(910, 10), (1010, 45)], fill=(0, 0, 0, 180))
    draw.text((920, 15), "x=960", fill=(255, 255, 255))
    
    draw.rectangle([(990, 55), (1090, 90)], fill=(0, 0, 0, 180))
    draw.text((1000, 60), "x=1040", fill=(0, 255, 255))
    
    draw.rectangle([(1800, 10), (1890, 45)], fill=(0, 0, 0, 180))
    draw.text((1810, 15), "x=1860", fill=(255, 50, 50))
    
    # Save
    out_path = annotated_dir / img_path.name
    img.save(out_path, quality=90)

print(f"Generated {len(jpg_files)} annotated images in {annotated_dir}")
