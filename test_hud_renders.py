import os
import json
from PIL import Image
import hud_animator

work_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid"
plan_path = os.path.join(work_dir, "master_plan_7videos.json")

with open(plan_path, "r", encoding="utf-8") as f:
    plan = json.load(f)

v1 = plan["videos"][0]
scenes = v1["scenes"]
lesson_title = v1.get("title", "")

preview_test_dir = os.path.join(work_dir, "output_videos", "previews_v1", "test_fixed_hud")
os.makedirs(preview_test_dir, exist_ok=True)

print("Testing HUD rendering on raw frames with composite_scene_frame...")
for s in scenes:
    idx = s["scene_idx"]
    raw_frame_path = os.path.join(work_dir, "output_videos", "previews_v1", "raw_mc", f"raw_s{idx}_5s.jpg")
    if not os.path.exists(raw_frame_path):
        print(f"Missing raw frame for s{idx}")
        continue
    
    bg = Image.open(raw_frame_path).convert("RGB")
    dur = s.get("audio_duration", 9.96)
    
    # Test at local_t = 6.0s (HUD fully revealed)
    comp = hud_animator.composite_scene_frame(
        bg_frame=bg,
        scene_data=s,
        local_t=6.0,
        duration=dur,
        total_progress=idx / len(scenes),
        lesson_title=lesson_title
    )
    
    out_path = os.path.join(preview_test_dir, f"test_s{idx}.jpg")
    comp.save(out_path, quality=92)
    print(f"Rendered s{idx} to {out_path}")

