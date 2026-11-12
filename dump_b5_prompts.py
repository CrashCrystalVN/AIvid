import json

with open(r'C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\master_plan_7videos.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

videos_list = data.get('videos', [])
target_ids = ['V4_B5_Nhom1_TocDo_VanToc', 'V5_B5_Nhom1_TongHop_VanToc', 'V6_B5_Nhom2_TocDo_VanToc', 'V7_B5_Nhom2_TongHop_VanToc']

summary = {}
for v in videos_list:
    vid = v.get('video_id') or v.get('id')
    if vid in target_ids:
        summary[vid] = {
            'title': v.get('title'),
            'mc_character': v.get('mc_character'),
            'scenes': []
        }
        for idx, s in enumerate(v.get('scenes', []), 1):
            summary[vid]['scenes'].append({
                'scene_idx': idx,
                'scene_id': s.get('scene_id', f's{idx}'),
                'title': s.get('title'),
                'speaker': s.get('speaker'),
                'keyframe_prompt': s.get('keyframe_prompt')
            })

print(json.dumps(summary, ensure_ascii=False, indent=2))
