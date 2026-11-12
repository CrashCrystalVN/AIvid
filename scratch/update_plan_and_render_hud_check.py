import os
import json
import sys
from PIL import Image

sys.path.append(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid")
import hud_animator

plan_path = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\master_plan_7videos.json"
with open(plan_path, "r", encoding="utf-8") as f:
    plan = json.load(f)

PRES_NHOM1 = "Nhóm 1: Thế Mỹ • ĐP.Hoàng Bách • Văn Hoàng • Thanh Tùng • Gia Nguyên"
BADGE_NHOM1 = "NHÓM 1 - VẬT LÍ 10"
BADGE_NHOM2 = "NHÓM 2 - VẬT LÍ 10"

# Layout config map for all 30 scenes
CONFIGS = {
    # Video 3 (Nhóm 1)
    "V3_S01": {"rect": [1040, 130, 1860, 430], "presenters": PRES_NHOM1, "badge": BADGE_NHOM1},
    "V3_S02": {"rect": [1060, 130, 1860, 870], "solid_card": True},
    "V3_S03": {"rect": [1060, 130, 1860, 870], "solid_card": True},
    "V3_S04": {"rect": [60, 120, 760, 870], "layout": "left_side"}, # Avoids PIP anime girl at bottom-right
    "V3_S05": {"rect": [1050, 130, 1860, 870], "solid_card": True},
    "V3_S06": {"rect": [60, 120, 780, 870], "layout": "left_side"}, # MC on right
    "V3_S07": {"rect": [60, 120, 780, 870], "layout": "left_side", "solid_card": True}, # MC on right
    "V3_S08": {"rect": [1060, 130, 1860, 870]}, # Finger points right
    "V3_S09": {"rect": [60, 120, 660, 870], "layout": "left_side", "presenters": PRES_NHOM1}, # MC in center

    # Video 4 (Nhóm 2)
    "V4_S01": {"rect": [1080, 130, 1860, 360], "presenters": "", "badge": BADGE_NHOM2},
    "V4_S02": {"rect": [1220, 120, 1860, 870]}, # Clear of runner fist
    "V4_S03": {"rect": [1160, 120, 1860, 680]}, # Clear of center motorcycle speedometer
    "V4_S04": {"rect": [1150, 130, 1860, 870]}, # Points right
    "V4_S05": {"rect": [1160, 130, 1860, 870], "solid_card": True}, # Clear table starting at pointing finger
    "V4_S06": {"rect": [1040, 130, 1860, 870]}, # Clear of MC and stopwatch

    # Video 5 (Nhóm 2)
    "V5_S01": {"rect": [1040, 130, 1860, 360], "presenters": "", "badge": BADGE_NHOM2},
    "V5_S02": {"rect": [60, 120, 780, 870], "layout": "left_side"}, # MC on right in train
    "V5_S03": {"rect": [1040, 130, 1860, 870]}, # MC on left
    "V5_S04": {"rect": [60, 120, 780, 870], "layout": "left_side"}, # Speedboats in center/right
    "V5_S05": {"rect": [60, 120, 640, 870], "layout": "left_side"}, # MC in center

    # Video 6 (Nhóm 1)
    "V6_S01": {"rect": [60, 130, 650, 520], "layout": "left_side", "presenters": PRES_NHOM1, "badge": BADGE_NHOM1}, # MC in center
    "V6_S02": {"rect": [60, 120, 760, 570]}, # Cyclist on right, Flow HUD on bottom-left
    "V6_S03": {"rect": [1250, 130, 1860, 870]}, # Leaning cyclist
    "V6_S04": {"rect": [980, 130, 1860, 870]}, # Airport moving walkway
    "V6_S05": {"rect": [960, 520, 1860, 880], "solid_card": True}, # Sits below hovering drone with solid opaque backing

    # Video 7 (Nhóm 1)
    "V7_S01": {"rect": [960, 130, 1860, 430], "presenters": PRES_NHOM1, "badge": BADGE_NHOM1},
    "V7_S02": {"rect": [60, 120, 760, 460]}, # Sits above airplane wing
    "V7_S03": {"rect": [60, 120, 800, 870], "layout": "left_side"}, # Sunset sky on left
    "V7_S04": {"rect": [60, 120, 760, 540]}, # Sits in canyon water above kayaker
    "V7_S05": {"rect": [980, 130, 1860, 870], "presenters": PRES_NHOM1, "badge": BADGE_NHOM1},
}

# Update master_plan_7videos.json
print("Updating master_plan_7videos.json scenes...")
for v in plan["videos"][2:]:
    vid = v["video_id"]
    for s in v["scenes"]:
        sid = s["scene_id"]
        cfg = CONFIGS.get(sid, {})
        hd = s.get("hud_data", {})

        # Apply rect / layout / solid_card
        for k, val in cfg.items():
            hd[k] = val
        s["hud_data"] = hd
        if "layout" in cfg:
            s["hud_layout"] = cfg["layout"]
        if "rect" in cfg:
            s["hud_rect"] = cfg["rect"]

with open(plan_path, "w", encoding="utf-8") as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)

print("master_plan_7videos.json successfully updated with 30 scene layouts!")

# Render preview test frames
check_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\scratch\flow_frame_audit\hud_check"
os.makedirs(check_dir, exist_ok=True)
audit_frames_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\scratch\flow_frame_audit"

print(f"Rendering all 30 preview frames into {check_dir}...")
count = 0
for v in plan["videos"][2:]:
    vid_short = v["video_id"].split("_")[0]
    lesson_title = v.get("title", "Vật lí 10")
    for s in v["scenes"]:
        sid = s["scene_id"]
        s_num = "s" + str(int(sid.split("_")[1][1:]))
        frame_name = f"{vid_short}_{s_num}.jpg"
        frame_path = os.path.join(audit_frames_dir, frame_name)

        if not os.path.exists(frame_path):
            print(f"WARNING: frame not found: {frame_path}")
            continue

        raw_img = Image.open(frame_path).convert("RGB")
        duration = float(s.get("duration_sec", 6.0))
        local_t = duration * 0.8 # Near end so animations, answers & cards are fully revealed

        composited = hud_animator.composite_scene_frame(
            raw_img,
            s,
            local_t=local_t,
            duration=duration,
            total_progress=0.8,
            lesson_title=lesson_title
        )

        out_name = f"{sid}.jpg"
        out_path = os.path.join(check_dir, out_name)
        composited.save(out_path, quality=92)
        count += 1
        print(f"[{count:02d}/30] Rendered {out_name} (rect={s.get('hud_data', {}).get('rect')})")

print("All 30 preview test frames successfully rendered!")
