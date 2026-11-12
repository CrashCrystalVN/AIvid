import json

with open(r'C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\master_plan_7videos.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for vid in data['videos'][3:5]:
    print('===', vid['video_id'], '===')
    for sc in vid['scenes']:
        print(f"[{sc['scene_id']}] HUD: {sc.get('hud_type')} | Title: {sc.get('title')}")
