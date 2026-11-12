import json
import os

WORK_DIR = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid"
PLAN_FILE = os.path.join(WORK_DIR, "master_plan_7videos.json")

BROLL_PROMPTS = {
    # Video 1
    "V1_S01": "Extreme close-up macro pan across a high-precision brass compass and drafting ruler on a sleek dark desk, glowing digital coordinates reflecting softly on polished metal, 16:9 cinematic 8k, photorealistic.",
    "V1_S02": "Extreme low-angle close-up of car tires spinning through a bustling city intersection pavement, asphalt texture, reflections of traffic lights in rain puddles, 16:9 8k cinematic.",
    "V1_S03": "Over-the-shoulder close-up of the Vietnamese male student MC tilting his head in curiosity with an intrigued thoughtful smile, warm studio backlight, 16:9 8k.",
    "V1_S04": "Macro cinematic shot of a glowing digital speedometer and GPS compass on a futuristic vehicle dashboard, numbers shifting smoothly, 16:9 8k.",
    "V1_S05": "Aerial top-down 90-degree drone shot slowly rotating over a four-way intersection, traffic moving in orthogonal directions along clean road markings, 16:9 8k.",
    "V1_S06": "Cinematic close-up of an analog pocket stopwatch clicking into motion with crisp mechanical gear reflections, shallow depth of field, 16:9.",
    "V1_S07": "Cinematic wide tracking shot of a sleek modern high-speed train seen from across a vast open landscape, appearing as a miniature point moving swiftly along the horizon, 16:9 8k.",
    "V1_S08": "Close-up reaction shot of the student MC with an engaging questioning gaze, raising one eyebrow with a friendly inquisitive expression, 16:9.",
    "V1_S09": "Medium tracking shot of the male student MC giving a respectful closing bow and confident warm smile, studio lights dimming gracefully behind him, 16:9.",

    # Video 2
    "V2_S01": "Cinematic close-up of student MC adjusting his glasses thoughtfully before stepping into frame with enthusiasm, soft blue studio lighting, 16:9.",
    "V2_S02": "Dynamic low-angle tracking shot of a modern car's front bumper and glowing LED headlights turning sharply North at a street crossing, 16:9 8k.",
    "V2_S03": "Close-up profile of the student MC gesturing with focused intensity, eyes bright, right hand sweeping gracefully horizontally, warm rim lighting, 16:9.",
    "V2_S04": "Tilt-shift miniature bird's-eye view of winding city roads between building blocks, with glowing golden trail lights simulating multiple routes, 16:9 8k.",
    "V2_S05": "Macro tracking shot of an odometer and bicycle wheel spinning along a winding gravel path, measuring curved path distance, 16:9.",
    "V2_S06": "Macro high-speed tracking shot of a surveyor's laser beam shooting straight across an open field, creating a crisp red line connecting two posts, 16:9.",
    "V2_S07": "Slow slider shot across the high-tech studio showing the MC standing beside a glowing dual-column comparative glass screen, 16:9.",
    "V2_S08": "Cinematic smooth tracking shot alongside a car driving strictly straight down a desert highway disappearing into the vanishing point at sunrise, 16:9.",
    "V2_S09": "Warm close-up of the student MC tapping his temple playfully and smiling, encouraging the viewers to think about the question, 16:9.",

    # Video 3
    "V3_S01": "Slow dramatic pull-back wide shot of the modern science laboratory, ambient blue LED accents glowing softly along the walls, 16:9.",
    "V3_S02": "Close-up of student MC's hands gracefully demonstrating vector tail-to-tip addition with open palms in the air, soft rim lighting, 16:9.",
    "V3_S03": "Aerial drone shot tracking a courier scooter driving 4 km straight East along a wide avenue, then making a crisp 90-degree left turn heading North, 16:9.",
    "V3_S04": "Top-down macro shot of a pencil drawing an 8 km segmented route along a grid notebook with neat numerical steps, 16:9.",
    "V3_S05": "Macro shot of a glowing digital drafting compass opening precisely to form the hypotenuse of a right-angled triangle on glass, 16:9.",
    "V3_S06": "Split-perspective shot contrasting a long winding path with a direct straight arrow across a futuristic geometric terrain, 16:9.",
    "V3_S07": "Close-up of three magnetic compass needles mounted on a brushed metal instrument, snapping into parallel, opposite, and perpendicular orientations, 16:9.",
    "V3_S08": "Engaging close-up of the student MC with an enthusiastic, encouraging smile, pointing gently towards the viewer, 16:9.",
    "V3_S09": "Wide cinematic dolly shot of the Vietnamese student MC in white uniform standing proudly in the center of the illuminated studio, giving a full friendly bow and wave, 16:9.",

    # Video 4
    "V4_S01": "Cinematic slow pan across the female student MC standing poised and confident in a bright, futuristic physics studio, soft warm lighting, 16:9.",
    "V4_S02": "Extreme slow-motion low-angle close-up of a track athlete's spikes exploding off starting blocks, dust kicking up in golden sunlight, 16:9 8k.",
    "V4_S03": "Macro cinematic view of a motorcycle digital speedometer rapidly accelerating from 0 to 60 km/h with glowing numbers reflecting in rider's visor, 16:9.",
    "V4_S04": "Close-up of female student MC raising her hand to indicate a specific forward heading, expressive eyes and articulate delivery, 16:9.",
    "V4_S05": "Medium two-shot perspective of the female student presenting beside a large illuminated dual-color comparison display, 16:9.",
    "V4_S06": "Warm close-up of the female student MC smiling with a welcoming head tilt, holding a marker pen, asking the audience to choose, 16:9.",

    # Video 5
    "V5_S01": "Establishing wide shot of the futuristic physics lab with glowing holographic vectors floating above a demonstration table, 16:9.",
    "V5_S02": "Cinematic tracking shot inside a modern high-speed passenger train aisle, looking at a person walking forward while scenic mountains blur outside the windows, 16:9.",
    "V5_S03": "Close-up of female student MC's hands joining two glowing holographic vectors tip-to-tail, confident professional smile, 16:9.",
    "V5_S04": "High-angle drone shot of a white speed motorboat cutting diagonally across a wide sparkling river, white foam wake trailing against blue water, 16:9 8k.",
    "V5_S05": "Wide closing shot of the female student MC smiling warmly with hands clasped politely, studio lights gently fading, 16:9.",

    # Video 6
    "V6_S01": "Dynamic tracking shot of male tech-enthusiast student MC in casual school blazer standing next to high-tech digital gear, 16:9.",
    "V6_S02": "FPV drone close pursuit shot flying just 2 meters behind a racing cyclist sprinting on smooth coastal tarmac, speedometer HUD overlay effect, 16:9.",
    "V6_S03": "Ultra-low-angle slow-motion shot of a road bicycle tire leaning hard into a hairpin curve, rubber gripping wet pavement with water spray, 16:9.",
    "V6_S04": "Eye-level side-tracking shot of travelers walking briskly forward on an airport moving walkway with blurred luggage concourse in background, 16:9.",
    "V6_S05": "Medium shot of male student MC pointing forward with an energetic high-tech gesture, inviting viewer to solve the riddle, 16:9.",

    # Video 7
    "V7_S01": "Dramatic wide shot of a flight navigation room with large screens displaying real-time global wind maps and flight paths, 16:9.",
    "V7_S02": "Exterior cinematic shot of a commercial airliner jet flying through dramatic sunset storm clouds, jet engines roaring with visible vapor trails, 16:9 8k.",
    "V7_S03": "Telephoto runway tracking shot of an airliner executing a crosswind crab landing, airplane nose angled sideways while landing gear touches down smoothly, 16:9 8k.",
    "V7_S04": "Close water-level action shot of a bright yellow kayak paddle slicing into foaming river rapids, splashing crystal-clear water drops in slow motion, 16:9 8k.",
    "V7_S05": "Grand finale wide shot: both student MCs (male and female) standing side by side in the magnificent physics studio, bowing with warm smiles and applause, 16:9 8k."
}

def update_plan():
    with open(PLAN_FILE, "r", encoding="utf-8") as f:
        plan = json.load(f)

    # 1. Update budget_summary for 2 Pro Accounts (2,000 cr)
    plan["budget_summary"] = {
        "total_pro_accounts": 2,
        "credits_per_account": 1000,
        "total_flow_credits": 2000,
        "cost_per_veo_fast_clip": 20,
        "max_total_clips": 100,
        "allocated_main_clips": 48,
        "allocated_main_credits": 960,
        "reserve_broll_reroll_credits": 1040,
        "account_1": {
            "account_name": "Account 1 (Bài 4)",
            "assigned_lesson": "Bài 4: Độ dịch chuyển và quãng đường đi được",
            "video_ids": ["V1_B4_ViTri_HeQuyChieu", "V2_B4_DoDichChuyen_QuangDuong", "V3_B4_TongHop_DoDichChuyen"],
            "total_credits": 1000,
            "main_clips": 27,
            "main_credits": 540,
            "reserve_broll_reroll_credits": 460
        },
        "account_2": {
            "account_name": "Account 2 (Bài 5)",
            "assigned_lesson": "Bài 5: Tốc độ và vận tốc (Nhóm 1 & Nhóm 2)",
            "video_ids": ["V4_B5_Nhom1_TocDo_VanToc", "V5_B5_Nhom1_TongHop_VanToc", "V6_B5_Nhom2_TocDo_VanToc", "V7_B5_Nhom2_TongHop_VanToc"],
            "total_credits": 1000,
            "main_clips": 21,
            "main_credits": 420,
            "reserve_broll_reroll_credits": 580
        }
    }

    # 2. Update videos with account_target, account_allocation and scene broll_prompt
    for v in plan["videos"]:
        vid = v["video_id"]
        if vid in ["V1_B4_ViTri_HeQuyChieu", "V2_B4_DoDichChuyen_QuangDuong", "V3_B4_TongHop_DoDichChuyen"]:
            v["account_target"] = "Account 1 (Bài 4)"
            v["account_id"] = "acc_1"
            v["account_cap_credits"] = 1000
            v["account_lesson"] = "Bài 4: Độ dịch chuyển và quãng đường đi được"
        else:
            v["account_target"] = "Account 2 (Bài 5)"
            v["account_id"] = "acc_2"
            v["account_cap_credits"] = 1000
            v["account_lesson"] = "Bài 5: Tốc độ và vận tốc"

        for s in v.get("scenes", []):
            s_id = s.get("scene_id")
            if s_id in BROLL_PROMPTS:
                s["broll_prompt"] = BROLL_PROMPTS[s_id]
            else:
                s["broll_prompt"] = f"Close-up insert angle of {s.get('title', '')}, crisp 8k photorealistic cinematic lighting, 16:9, no text."

    with open(PLAN_FILE, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] master_plan_7videos.json updated to 2,000 credits & dual accounts!")

if __name__ == "__main__":
    update_plan()
