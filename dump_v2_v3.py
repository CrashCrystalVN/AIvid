import json

with open('C:/Users/vuasu/.gemini/antigravity/scratch/AIvid/master_plan_7videos.json', 'r', encoding='utf-8') as f:
    plan = json.load(f)

with open('C:/Users/vuasu/.gemini/antigravity/scratch/AIvid/v2_v3_scenes.txt', 'w', encoding='utf-8') as out:
    for v in plan['videos']:
        vid = v.get('video_id') or v.get('id')
        if vid in ['V2_B4_DoDichChuyen_QuangDuong', 'V3_B4_TongHop_DoDichChuyen']:
            out.write(f"=== {vid} (Speaker: {v.get('speaker', 'N/A')}) ===\n")
            for s in v.get('scenes', []):
                idx = s.get('scene_idx')
                title = s.get('title')
                speaker = s.get('speaker')
                has_mc = s.get('has_mc')
                prompt = s.get('keyframe_prompt')
                hud = s.get('hud_type')
                out.write(f"Scene {idx}: {title} | MC: {speaker} | has_mc: {has_mc} | hud: {hud}\n")
                out.write(f"  Prompt: {prompt}\n\n")

print("Dumped v2_v3_scenes.txt successfully.")
