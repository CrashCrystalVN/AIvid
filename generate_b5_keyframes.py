"""
Script for Generating 21 Keyframes for Lesson 5 (Videos 4, 5, 6, 7)
Configured with strict prompt engineering for 16:9 clean negative space, zero-text, and character consistency.
"""

import os
import json

TARGET_KEYFRAMES = {
    "V4_B5_Nhom1_TocDo_VanToc": {
        "mc": "Tú Châu (16yo, athletic build, high ponytail + royal blue ribbon, royal blue sports polo with white stripes)",
        "theme": "Athletic Science Studio / Olympic Track (Cyan/Blue Theme)",
        "scenes": [
            {
                "id": "s1",
                "role": "MC Lead",
                "prompt": "Cinematic medium shot of a 16-year-old Vietnamese female high school student (Tú Châu) with athletic posture and neat high ponytail tied with a subtle royal-blue ribbon, bright friendly smile, wearing a modern royal-blue collared school sports polo shirt with white side stripes. She stands on the left 35% of an indoor athletic science studio overlooking an Olympic running track in the background. Ample clean negative space on the right 65% with soft ambient sports studio lighting. 16:9, 8k, photorealistic, no text, no logos."
            },
            {
                "id": "s2",
                "role": "Action",
                "prompt": "Cinematic side-angle tracking shot of an athletic sprinter in dynamic motion sprinting along a crimson running track under bright stadium floodlights. Crisp motion blur in background, sharp focus on the runner. Clean upper sky and open track lanes for holographic speedometer and timer. 16:9, 8k, photorealistic, no text, no numbers."
            },
            {
                "id": "s3",
                "role": "Subject",
                "prompt": "Cinematic close-up perspective from behind motorcycle handlebars riding smoothly along a twilight asphalt city boulevard. The circular mechanical speedometer dial is in center-left foreground. The upper right has soft blurred city bokeh with vast negative space for digital gauge overlays. 16:9, 8k, photorealistic, no pre-rendered numbers on dial."
            },
            {
                "id": "s4",
                "role": "MC Presenter",
                "prompt": "Medium shot of the Vietnamese female student in sports polo, speaking expressively with hand gestures indicating two opposite directions, standing on the left side (35%) of the athletic studio. Right side dark slate background with subtle cyan lighting. 16:9, 8k, photorealistic, no text."
            },
            {
                "id": "s5",
                "role": "MC Presenter",
                "prompt": "Medium wide shot of the Vietnamese female student in blue sports polo standing on the far left, gesturing toward the center-right presentation area. Studio atmosphere with blue lighting accents. 16:9, 8k, photorealistic, no text."
            },
            {
                "id": "s6",
                "role": "MC Presenter",
                "prompt": "Medium close-up of the Vietnamese female student in sports polo, smiling warmly and confidently, holding an athletic digital stopwatch in her hand, looking into the lens. Soft blurred gym studio background. 16:9, 8k, photorealistic, no text on stopwatch."
            }
        ]
    },
    "V5_B5_Nhom1_TongHop_VanToc": {
        "mc": "Minh Dũng (16yo, short fade haircut, confident smile, dark navy blue collared polo with white trim)",
        "theme": "Transportation Science Lab / Train & River (Navy & Deep Blue Theme)",
        "scenes": [
            {
                "id": "s1",
                "role": "MC Lead",
                "prompt": "Cinematic medium shot of a 16-year-old Vietnamese male high school student (Minh Dũng) with athletic build, modern neat short fade haircut, confident friendly smile, wearing a dark navy blue collared school team polo shirt with crisp white trim. He stands on the left 35% of a modern transportation science laboratory with sleek scale model train tracks and displays softly blurred in the background. Ample clean negative space on the right 65%. 16:9, 8k, photorealistic, no text."
            },
            {
                "id": "s2",
                "role": "Object",
                "prompt": "Cinematic side-profile shot of a sleek modern passenger train cruising smoothly along railway tracks through open green fields. Clear open sky above the train and spacious foreground for floating holographic diagrams. 16:9, 8k, photorealistic, no letters or numbers on train."
            },
            {
                "id": "s3",
                "role": "MC Presenter",
                "prompt": "Medium shot of the Vietnamese male student in navy polo, hands framing a central formula space with conviction. Modern lab interior with ambient blue glow. 16:9, 8k, photorealistic, no text."
            },
            {
                "id": "s4",
                "role": "Action",
                "prompt": "Cinematic high-angle drone shot looking down at a wide scenic river with rippling turquoise water between two lush green riverbanks. A small white motorboat moves across the water. Clear expansive water surface perfect for vector arrows. 16:9, 8k, photorealistic, no text, no symbols."
            },
            {
                "id": "s5",
                "role": "MC Presenter",
                "prompt": "Medium shot of the Vietnamese male student in navy polo standing smiling warmly, hand raised in an appreciative salute gesture to the audience. Bright modern studio background, 16:9, 8k, photorealistic, no text."
            }
        ]
    },
    "V6_B5_Nhom2_TocDo_VanToc": {
        "mc": "Hoàng Nam (16yo, tech glasses, graphite-grey tech jacket over white shirt)",
        "theme": "Drone Robotics & Innovation Lab / Coast & Airport (Slate & Cool Teal Theme)",
        "scenes": [
            {
                "id": "s1",
                "role": "MC Lead",
                "prompt": "Cinematic medium shot of a 16-year-old tech-savvy Vietnamese male high school student (Hoàng Nam) with stylish modern square spectacles/glasses, wearing a sleek graphite-grey zip-up tech jacket over a plain white crewneck t-shirt. He stands on the left 35% of a high-tech drone robotics and telemetry innovation laboratory with carbon fiber drone frames blurred in the background. Right 65% is clean open negative space. 16:9, 8k, photorealistic, no text."
            },
            {
                "id": "s2",
                "role": "Action",
                "prompt": "Cinematic high-angle drone tracking shot of a cyclist in aerodynamic cycling gear riding a sleek modern road bike along a scenic coastal asphalt road beside turquoise ocean waters. Expansive road and ocean space for holographic GPS telemetry graphics. 16:9, 8k, photorealistic, no text, no telemetry pre-rendered."
            },
            {
                "id": "s3",
                "role": "Action",
                "prompt": "High-angle view of an asphalt mountain road curving in a graceful S-curve bend. The cyclist leans smoothly into the curve. Vast clean road surface for vector trajectory arrows. 16:9, 8k, photorealistic, no text."
            },
            {
                "id": "s4",
                "role": "Environment",
                "prompt": "Cinematic interior shot of a brightly lit modern airport terminal concourse with a long flat moving walkway belt and polished floors. Soft ambient indoor lighting, clean negative space across upper ceiling and walkway for directional coordinate vectors. 16:9, 8k, photorealistic, no signage text, no airport logos."
            },
            {
                "id": "s5",
                "role": "MC Presenter",
                "prompt": "Medium shot of the tech-savvy Vietnamese male student in grey jacket, holding a sleek digital tablet, looking up at the camera with an engaging smile. Innovation lab backdrop with soft bokeh. 16:9, 8k, photorealistic, no text on tablet."
            }
        ]
    },
    "V7_B5_Nhom2_TongHop_VanToc": {
        "mc": "Cẩm Nhung (16yo, soft wavy black hair, pastel-mint green cardigan over white blouse)",
        "theme": "Aviation Science Gallery / Flight & Kayak River (Mint Green & Atmospheric Sky Theme)",
        "scenes": [
            {
                "id": "s1",
                "role": "MC Lead",
                "prompt": "Cinematic medium shot of a 16-year-old Vietnamese female high school student (Cẩm Nhung) with shoulder-length soft wavy black hair and a radiant smart smile, wearing a stylish pastel-mint green cardigan over a neat white collared blouse. She stands on the left 35% of an aerodynamics and flight science gallery with sleek scale aircraft models blurred behind. Right 65% is clean open space. 16:9, 8k, photorealistic, no text."
            },
            {
                "id": "s2",
                "role": "Action",
                "prompt": "Cinematic aerial shot of a modern passenger jet airliner cruising steadily at high altitude above a vast field of sunlit white cumulus clouds under a deep blue sky. Ample sky space around the aircraft for wind vectors and speed telemetry. 16:9, 8k, photorealistic, no airline logos, no letters."
            },
            {
                "id": "s3",
                "role": "Action",
                "prompt": "High-angle aerial shot from behind a modern aircraft flying through high-altitude misty skies. Vast open sky and misty cloudscape for overlaying vector triangle diagrams. 16:9, 8k, photorealistic, no text."
            },
            {
                "id": "s4",
                "role": "Action",
                "prompt": "Cinematic aerial drone shot of an athletic person paddling a sleek modern kayak on an emerald river winding through a lush pine forest canyon. Pristine clear water ripples, clean surface for vector annotations. 16:9, 8k, photorealistic, no text."
            },
            {
                "id": "s5",
                "role": "MC Presenter",
                "prompt": "Medium shot of the Vietnamese female student in mint cardigan, smiling radiantly, hands neatly clasped, giving a warm bow of appreciation to the viewer. Modern exhibition gallery backdrop with soft ambient light. 16:9, 8k, photorealistic, no text."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Loaded {sum(len(v['scenes']) for v in TARGET_KEYFRAMES.values())} keyframe definitions across {len(TARGET_KEYFRAMES)} videos.")
