import json
import os

plan_path = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\master_plan_7videos.json"

with open(plan_path, "r", encoding="utf-8") as f:
    plan = json.load(f)

for v in plan["videos"]:
    if "V7" in v["video_id"]:
        # Scene 1
        s1 = v["scenes"][0]
        s1["keyframe_prompt"] = (
            "Cinematic medium shot of an original, completely fictional 16-year-old Vietnamese female high school "
            "student presenter (original non-celebrity character) named Cẩm Nhung. She wears delicate thin round "
            "spectacles/glasses, has natural black hair with gentle bangs, and a radiant smart smile, wearing a "
            "stylish pastel-mint green cardigan over a white blouse. She stands on the left 35% of a modern "
            "aerodynamics flight science exhibition gallery with sleek scale aircraft models blurred behind. "
            "Right 65% is clean open negative space. 16:9, 8k, photorealistic, no text, no numbers, no watermarks."
        )
        s1["flow_i2v_prompt"] = (
            "A fictional 16-year-old Vietnamese high school student presenter (original non-celebrity character) "
            "wearing round glasses and a pastel mint cardigan. She smiles warmly, waves gently in greeting, and "
            "speaks with clear expressive voice, gesturing toward the right negative space. Crisp lighting, 4k."
        )
        
        # Scene 5 (Outro)
        s5 = v["scenes"][4]
        s5["keyframe_prompt"] = (
            "Cinematic medium shot of the fictional 16-year-old Vietnamese female student presenter (original "
            "non-celebrity character Cẩm Nhung) with thin round glasses in pastel mint cardigan, smiling radiantly "
            "with hands neatly clasped, giving a warm polite bow of appreciation to the viewer. Modern exhibition "
            "gallery backdrop with soft ambient light. 16:9, 8k, photorealistic, no text, no numbers, no watermarks."
        )
        s5["flow_i2v_prompt"] = (
            "A fictional 16-year-old Vietnamese high school student presenter (original non-celebrity character) "
            "wearing round glasses and a pastel mint cardigan. The presenter smiles warmly, bows with polite gratitude, "
            "and waves cheerfully to conclude the entire series. High quality natural motion."
        )
        print("Updated V7 Scene 1 and Scene 5 prompts in master plan.")

with open(plan_path, "w", encoding="utf-8") as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)

print("[SUCCESS] master_plan_7videos.json updated successfully.")
