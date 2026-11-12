import os
import json
from PIL import Image
import hud_animator

work_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid"
plan_path = os.path.join(work_dir, "master_plan_7videos.json")

with open(plan_path, "r", encoding="utf-8") as f:
    plan = json.load(f)

v4 = plan["videos"][3]
v5 = plan["videos"][4]

preview_dir = os.path.join(work_dir, "preview_huds", "b5_nhom1_samples")
os.makedirs(preview_dir, exist_ok=True)

test_targets = [
    (v4, "V4_B5_Nhom1_TocDo_VanToc", 1, "s1.png"),
    (v4, "V4_B5_Nhom1_TocDo_VanToc", 5, "s5.png"),
    (v5, "V5_B5_Nhom1_TongHop_VanToc", 1, "s1.png"),
    (v5, "V5_B5_Nhom1_TongHop_VanToc", 3, "s3.png")
]

for v, vid_dir, sc_idx, img_name in test_targets:
    sc = v["scenes"][sc_idx - 1]
    img_path = os.path.join(work_dir, "keyframes", vid_dir, img_name)
    bg = Image.open(img_path).convert("RGB")
    dur = sc.get("audio_duration", 10.0)
    
    comp = hud_animator.composite_scene_frame(
        bg_frame=bg,
        scene_data=sc,
        local_t=min(5.0, dur * 0.7),
        duration=dur,
        total_progress=sc_idx / len(v["scenes"]),
        lesson_title=v.get("title", "")
    )
    
    out_p = os.path.join(preview_dir, f"preview_{vid_dir}_{sc_idx}.jpg")
    comp.save(out_p, quality=92)
    print(f"Generated preview HUD: {out_p}")

print("All sample preview HUDs generated successfully!")
