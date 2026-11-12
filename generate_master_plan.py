import json
import os

plan = {
    "project_name": "Google Flow Hybrid Full Animation - Physics Grade 10",
    "style_reference": "Cô Nhung Cute / Hologram HUD Cyan Glow / Clean Keyframe + Python HUD Engine",
    "budget_summary": {
        "max_flow_credits": 1000,
        "cost_per_veo_fast_clip": 20,
        "max_possible_clips": 50,
        "allocated_clips": 48,
        "allocated_credits": 960,
        "reserve_clips": 2,
        "reserve_credits": 40
    },
    "curriculum_scope": [
        "Bài 4: Độ dịch chuyển và quãng đường đi được (Kết nối tri thức)",
        "Bài 5: Tốc độ và vận tốc (Kết nối tri thức)"
    ],
    "videos": [
        # =========================================================================
        # VIDEO 1: BÀI 4 - PHẦN 1
        # =========================================================================
        {
            "video_id": "V1_B4_ViTri_HeQuyChieu",
            "title": "Bài 4 (Phần 1): Vị trí của vật & Hệ quy chiếu",
            "lesson": "Bài 4: Độ dịch chuyển và quãng đường đi được",
            "part": 1,
            "group_assignment": "Anh Thư, Hữu Trọng, Thế Mỹ",
            "theme": "Thực tế giao thông ngã tư, hệ tọa độ địa lí Oxy, vật mốc & chất điểm",
            "mc_character": {
                "name": "Anh Thư",
                "gender": "female",
                "age": 16,
                "role": "Lead Presenter - Friendly, energetic Vietnamese high school student",
                "appearance_prompt_en": "A 16-year-old Vietnamese female high school student with smooth black hair tied in an elegant high ponytail, warm bright smile, clear skin, wearing a crisp modern white school uniform shirt with navy blue collar piping and embroidered school crest. Expressive friendly eyes and articulate presenter posture."
            },
            "clip_count": 9,
            "total_estimated_duration_sec": 65.0,
            "scenes": [
                {
                    "scene_idx": 1,
                    "scene_id": "V1_S01",
                    "title": "Mở đầu & Tiêu đề bài học",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Cinematic medium shot of a 16-year-old Vietnamese female high school student with black ponytail hair and a friendly warm smile, wearing a crisp white high school uniform shirt with navy collar trim. She stands on the left side of a sleek, bright high-tech physics classroom studio with soft ambient lighting. The right 60% of the frame is completely clean, uncluttered open space with gentle bokeh background, perfect for floating holographic graphics. 16:9 aspect ratio, 8k, photorealistic, no text, no numbers, no symbols.",
                    "flow_i2v_prompt": "The Vietnamese female student smiles warmly, waves gently with her right hand in greeting, and speaks naturally with expressive lip movement. Tripod medium camera shot, gentle studio lighting, realistic human micro-expressions, clean background remains static, 4k.",
                    "hud_type": "title_banner",
                    "hud_data": {
                        "banner_title": "BÀI 4: ĐỘ DỊCH CHUYỂN & QUÃNG ĐƯỜNG",
                        "badge": "VẬT LÍ 10 - KNTT",
                        "subtitle": "Phần 1: Vị trí của vật & Hệ quy chiếu",
                        "presenters": "Nhóm: Anh Thư • Hữu Trọng • Thế Mỹ",
                        "theme_color": "cyan_glow"
                    },
                    "speaker": "Anh Thư",
                    "voiceover_text": "Chào mừng thầy cô và các bạn! Hôm nay, nhóm mình xin đồng hành cùng các bạn khám phá Bài 4: Vị trí của vật và Hệ quy chiếu trong môn Vật lí 10.",
                    "subtitles": [
                        {"start": 0.0, "end": 3.2, "text": "Chào mừng thầy cô và các bạn!"},
                        {"start": 3.2, "end": 7.0, "text": "Hôm nay, nhóm mình xin khám phá Bài 4: Vị trí của vật và Hệ quy chiếu."}
                    ]
                },
                {
                    "scene_idx": 2,
                    "scene_id": "V1_S02",
                    "title": "Tình huống thực tế: Ô tô qua ngã tư",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic aerial top-down 90-degree drone shot of a modern clean urban four-way intersection with smooth asphalt roads, crosswalk markings, and surrounding lush green trees. A bright red sedan car is paused precisely at the center junction point. Surrounding lanes are clean. Ample open asphalt road space left, right, top, and bottom for overlay graphics. Crisp daylight, 8k resolution, 16:9 aspect ratio, absolutely no text, no letters, no HUD.",
                    "flow_i2v_prompt": "Smooth aerial drone hover shot. The red car accelerates gently straight forward northward through the intersection at a realistic city speed. Trees sway gently in the breeze. Static clean camera perspective, fluid realistic vehicle motion, photorealistic 4k.",
                    "hud_type": "speed_gauge",
                    "hud_data": {
                        "gauge_title": "THÔNG SỐ XE Ô TÔ",
                        "speed": "v = 36 km/h (10 m/s)",
                        "time": "t = 10 s",
                        "distance": "s = 100 m",
                        "origin_marker": "Gốc O (Tâm ngã tư)"
                    },
                    "speaker": "Anh Thư",
                    "voiceover_text": "Hãy bắt đầu với một câu hỏi thực tế: Một chiếc ô tô chạy qua ngã tư O với tốc độ đều 36 km/h. Sau đúng 10 giây, xe đi được quãng đường 100 mét.",
                    "subtitles": [
                        {"start": 0.0, "end": 3.8, "text": "Một chiếc ô tô chạy qua ngã tư O với tốc độ đều 36 km/h."},
                        {"start": 3.8, "end": 7.5, "text": "Sau đúng 10 giây, xe đi được quãng đường 100 mét."}
                    ]
                },
                {
                    "scene_idx": 3,
                    "scene_id": "V1_S03",
                    "title": "Mâu thuẫn nhận thức: Ô tô đang ở đâu?",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Medium shot of the same Vietnamese female high school student with ponytail in crisp white uniform, standing on the left side of the modern classroom. She has an inquisitive, questioning expression with slightly raised eyebrows and open hand gesture. The right side of the screen is empty clean studio space with subtle blue ambient lighting. Photorealistic, 8k, 16:9 aspect ratio, no text, no graphics.",
                    "flow_i2v_prompt": "The female student tilts her head slightly in thought, speaking engagingly with natural mouth movements, gesturing toward the empty space on her right as if presenting an intriguing puzzle to the audience. Realistic eye blinks and subtle shoulder movements, 4k.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "box_1": {"title": "Dữ kiện đã biết", "content": "Quãng đường s = 100 m"},
                        "box_2": {"title": "Câu hỏi đặt ra", "content": "Ô tô đang ở đâu trên bản đồ?", "status": "warning"},
                        "dilemma": "Chỉ biết quãng đường s => CHƯA ĐỦ để xác định vị trí!"
                    },
                    "speaker": "Anh Thư",
                    "voiceover_text": "Câu hỏi đặt ra là: Liệu chỉ biết quãng đường 100 mét, chúng mình có thể chỉ ra chính xác ô tô đang ở vị trí nào không? Chắc chắn là chưa thể!",
                    "subtitles": [
                        {"start": 0.0, "end": 4.0, "text": "Liệu chỉ biết quãng đường 100 m, ta có xác định được ô tô ở đâu?"},
                        {"start": 4.0, "end": 7.0, "text": "Chắc chắn là chưa thể, vì ta chưa biết hướng đi!"}
                    ]
                },
                {
                    "scene_idx": 4,
                    "scene_id": "V1_S04",
                    "title": "Vật mốc & Hệ tọa độ 1 chiều (Ox)",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic street-level perspective of a long straight modern city avenue with smooth asphalt road and sidewalks lined with neat trees and modern lampposts on a sunny day. Clean negative space across the middle road surface and upper sky for vector graphics. Sharp depth of field, 16:9, photorealistic, no text, no symbols.",
                    "flow_i2v_prompt": "Subtle forward camera dolly along the straight avenue. Distant leaves flutter gently. Clear, stable road surface perfect for overlaid coordinate axis. High quality 4k render.",
                    "hud_type": "animated_axes",
                    "hud_data": {
                        "axis_mode": "1D_Ox",
                        "origin_label": "Gốc O (Cột đèn / Ngã tư)",
                        "axis_direction": "Trục Ox trùng hướng đường đi",
                        "coordinate_point": "x = +100 m",
                        "scale": "Mỗi vạch = 20 m"
                    },
                    "speaker": "Anh Thư",
                    "voiceover_text": "Nếu ô tô chỉ chạy thẳng trên một con đường thẳng, ta chỉ cần chọn một vật mốc O và trục Ox trùng với đường đi; vị trí xe sẽ được xác định bởi tọa độ x.",
                    "subtitles": [
                        {"start": 0.0, "end": 3.8, "text": "Nếu ô tô chỉ chạy thẳng trên một con đường thẳng,"},
                        {"start": 3.8, "end": 7.5, "text": "ta chỉ cần chọn vật mốc O và trục Ox; vị trí xe xác định bởi tọa độ x."}
                    ]
                },
                {
                    "scene_idx": 5,
                    "scene_id": "V1_S05",
                    "title": "Hệ tọa độ địa lí 2 chiều Oxy (Đông - Tây - Nam - Bắc)",
                    "duration_sec": 8.0,
                    "keyframe_prompt": "Medium shot of the Vietnamese female student in white uniform standing on the left side of the high-tech classroom, smiling confidently and pointing her right index finger toward the right open space. Bright, clean minimalist classroom environment with a hint of tech glass. Crisp studio lighting, 16:9, 8k, no text, no numbers, no diagrams.",
                    "flow_i2v_prompt": "The student speaks articulately, her right arm extending smoothly to trace an imaginary vertical and horizontal axis in the air to her right. Natural eye contact with camera, fluid arm motion, realistic facial animation.",
                    "hud_type": "animated_axes",
                    "hud_data": {
                        "axis_mode": "2D_Geographic_Oxy",
                        "x_axis": "Ox: Hướng Tây - Đông",
                        "y_axis": "Oy: Hướng Nam - Bắc",
                        "point_A": "Điểm A (20 m, 45° Đông - Bắc)",
                        "vector_OA": "Vectơ OA vẽ sáng từ O đến A"
                    },
                    "speaker": "Anh Thư",
                    "voiceover_text": "Nhưng khi xe có thể rẽ nhiều hướng, ta cần Hệ tọa độ địa lí Oxy: Trục Ox theo hướng Tây – Đông và trục Oy theo hướng Nam – Bắc, gắn chặt với vật mốc.",
                    "subtitles": [
                        {"start": 0.0, "end": 4.0, "text": "Khi xe có thể rẽ nhiều hướng, ta cần Hệ tọa độ địa lí Oxy:"},
                        {"start": 4.0, "end": 8.0, "text": "Trục Ox hướng Tây – Đông và trục Oy hướng Nam – Bắc gắn với vật mốc."}
                    ]
                },
                {
                    "scene_idx": 6,
                    "scene_id": "V1_S06",
                    "title": "Khái niệm Hệ quy chiếu hoàn chỉnh",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Medium wide shot of the Vietnamese female student standing elegantly in the high-tech classroom laboratory, with modern sleek laboratory benches in the background. The upper half and right side of the frame are softly lit empty spaces with dark blue atmospheric gradient. 16:9, 8k, photorealistic, no text, no letters.",
                    "flow_i2v_prompt": "The presenter nods encouragingly and gestures with both hands in a counting motion, speaking clearly with synchronized mouth animation. Cinematic studio lighting, subtle camera zoom-in.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "HỆ QUY CHIẾU HOÀN CHỈNH",
                        "elements": [
                            "1. Hệ tọa độ gắn với vật mốc",
                            "2. Mốc thời gian (t0 = 0)",
                            "3. Đồng hồ đo thời gian"
                        ],
                        "formula": "HỆ QUY CHIẾU = HỆ TỌA ĐỘ + MỐC THỜI GIAN & ĐỒNG HỒ"
                    },
                    "speaker": "Anh Thư",
                    "voiceover_text": "Để mô tả trọn vẹn chuyển động, các bạn nhớ công thức vàng: Hệ quy chiếu bao gồm Hệ tọa độ gắn với vật mốc, kết hợp cùng mốc thời gian và đồng hồ đo.",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Để mô tả trọn vẹn chuyển động, các bạn nhớ công thức vàng:"},
                        {"start": 3.7, "end": 7.5, "text": "Hệ quy chiếu = Hệ tọa độ gắn vật mốc + Mốc thời gian & Đồng hồ đo."}
                    ]
                },
                {
                    "scene_idx": 7,
                    "scene_id": "V1_S07",
                    "title": "Khái niệm Chất điểm",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Cinematic ultra-wide landscape shot of an expansive modern highway spanning across rolling green hills under a bright clear sky. In the vast distance, a tiny red car travels along the road. Vast negative sky and landscape space for holographic scaling graphics. 16:9 aspect ratio, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "Cinematic slow aerial drone glide following the tiny car moving along the massive highway. Realistic atmospheric haze and natural light, stable smooth cinematic movement.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "KHÁI NIỆM CHẤT ĐIỂM",
                        "condition": "Kích thước của vật << Chiều dài quãng đường",
                        "example": "Ô tô (4 m) << Quãng đường (100 m - 10 km)",
                        "rule": "Bỏ qua kích thước hình dạng, coi vật là một điểm mang khối lượng!"
                    },
                    "speaker": "Anh Thư",
                    "voiceover_text": "Khi kích thước của vật rất nhỏ so với quãng đường di chuyển — ví dụ chiếc ô tô 4 mét chạy hàng trăm mét — ta hoàn toàn có thể coi nó là một chất điểm!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.5, "text": "Khi kích thước của vật rất nhỏ so với quãng đường đi được,"},
                        {"start": 3.5, "end": 7.0, "text": "ta hoàn toàn có thể coi vật là một chất điểm!"}
                    ]
                },
                {
                    "scene_idx": 8,
                    "scene_id": "V1_S08",
                    "title": "Câu hỏi tương tác Pop-up",
                    "duration_sec": 6.5,
                    "keyframe_prompt": "Medium close-up of the Vietnamese female student in white school uniform, looking directly at the camera with an engaging, friendly smile and a quizzical expression, tilting head slightly. The right half of the frame has clean dark slate background with gentle bokeh. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student smiles warmly, blinks naturally, raises an inviting hand toward the right side, and speaks cheerfully. Fluid breathing motion and engaging presence.",
                    "hud_type": "quiz_popup",
                    "hud_data": {
                        "question": "Khi nào một vật chuyển động được coi là CHẤT ĐIỂM?",
                        "options": [
                            "A. Khi khối lượng của vật rất nhỏ",
                            "B. Khi kích thước của vật rất nhỏ so với quãng đường đi",
                            "C. Khi vật chuyển động rất nhanh"
                        ],
                        "correct_answer": "B",
                        "hint": "Quy tắc: Kích thước vật << Chiều dài đường đi."
                    },
                    "speaker": "Anh Thư",
                    "voiceover_text": "Bây giờ, mời các bạn cùng thử tài với câu hỏi tương tác: Trong trường hợp nào thì một vật chuyển động được coi là một chất điểm?",
                    "subtitles": [
                        {"start": 0.0, "end": 3.2, "text": "Mời các bạn cùng thử tài với câu hỏi tương tác:"},
                        {"start": 3.2, "end": 6.5, "text": "Trong trường hợp nào thì vật chuyển động được coi là chất điểm?"}
                    ]
                },
                {
                    "scene_idx": 9,
                    "scene_id": "V1_S09",
                    "title": "Tổng kết & Chào kết Video 1",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Medium shot of the Vietnamese female student standing center-left in the modern classroom, smiling brightly with a warm gesture of gratitude, hands neatly clasped. Clean modern classroom aesthetics, soft warm lighting, 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student speaks enthusiastically, nods respectfully, and gives a cheerful hand wave to the camera. Warm studio atmosphere, natural smooth movement.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "TỔNG KẾT BÀI 4 (PHẦN 1)",
                        "recap": [
                            "✓ Vị trí cần: Vật mốc + Hệ tọa độ Oxy",
                            "✓ Hệ quy chiếu = Hệ tọa độ + Mốc thời gian & Đồng hồ",
                            "✓ Chất điểm khi kích thước << quãng đường"
                        ],
                        "next_teaser": "Đón xem Video 2: Phân biệt Quãng đường & Độ dịch chuyển!"
                    },
                    "speaker": "Anh Thư",
                    "voiceover_text": "Vậy là chúng ta đã nắm chắc cách xác định vị trí và thiết lập hệ quy chiếu rồi! Hẹn gặp lại thầy cô và các bạn ở Video 2 với khái niệm Độ dịch chuyển nhé!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.5, "text": "Vậy là chúng ta đã nắm chắc vị trí và hệ quy chiếu rồi!"},
                        {"start": 3.5, "end": 7.0, "text": "Hẹn gặp lại các bạn ở Video 2 với khái niệm Độ dịch chuyển nhé!"}
                    ]
                }
            ]
        },

        # =========================================================================
        # VIDEO 2: BÀI 4 - PHẦN 2
        # =========================================================================
        {
            "video_id": "V2_B4_DoDichChuyen_QuangDuong",
            "title": "Bài 4 (Phần 2): Độ dịch chuyển & Phân biệt Quãng đường",
            "lesson": "Bài 4: Độ dịch chuyển và quãng đường đi được",
            "part": 2,
            "group_assignment": "Anh Thư, Hữu Trọng, Thế Mỹ",
            "theme": "Mô hình siêu thị - bưu điện, vectơ độ dịch chuyển d, so sánh s và d, điều kiện |d| = s",
            "mc_character": {
                "name": "Hữu Trọng",
                "gender": "male",
                "age": 16,
                "role": "Lead Presenter - Smart, articulate Vietnamese male high school student",
                "appearance_prompt_en": "A 16-year-old Vietnamese male high school student with short neat black hair, black-rimmed spectacles, warm confident smile, wearing a crisp white high school uniform shirt with navy blue collar trim and button placket. Intellectual, articulate and energetic demeanor."
            },
            "clip_count": 9,
            "total_estimated_duration_sec": 66.5,
            "scenes": [
                {
                    "scene_idx": 1,
                    "scene_id": "V2_S01",
                    "title": "Mở đầu & Tiêu đề Video 2",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Cinematic medium shot of a 16-year-old Vietnamese male high school student with neat short black hair and black-rimmed glasses, warm confident smile, wearing a crisp white school uniform shirt with navy blue trim. He stands on the left of an open modern bright science studio. The right 65% is clean open space with soft architectural blur. 16:9, 8k, photorealistic, no text, no symbols.",
                    "flow_i2v_prompt": "The male student smiles, nods in greeting, and speaks naturally with expressive gestures. Clear natural mouth movement, realistic posture adjustment, smooth 4k cinematic presentation.",
                    "hud_type": "title_banner",
                    "hud_data": {
                        "banner_title": "BÀI 4: ĐỘ DỊCH CHUYỂN & QUÃNG ĐƯỜNG",
                        "badge": "VẬT LÍ 10 - KNTT",
                        "subtitle": "Phần 2: Phân biệt Quãng đường (s) và Độ dịch chuyển (d)",
                        "presenters": "Nhóm: Hữu Trọng • Anh Thư • Thế Mỹ",
                        "theme_color": "cyan_glow"
                    },
                    "speaker": "Hữu Trọng",
                    "voiceover_text": "Chào các bạn! Trong phần 2 của Bài 4, nhóm mình sẽ cùng các bạn làm rõ một trong những khái niệm nền tảng dễ nhầm lẫn nhất: Quãng đường và Độ dịch chuyển!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.3, "text": "Chào các bạn! Trong phần 2 của Bài 4,"},
                        {"start": 3.3, "end": 7.0, "text": "nhóm mình sẽ phân biệt rõ Quãng đường và Độ dịch chuyển!"}
                    ]
                },
                {
                    "scene_idx": 2,
                    "scene_id": "V2_S02",
                    "title": "Quay lại ngã tư: Xác định rõ hướng Bắc",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Aerial top-down view of the urban four-way intersection. Origin point at center junction. Crisp asphalt road surface, pedestrian crosswalks, surrounding modern city buildings and sidewalks. Large clear asphalt surface ready for vector graphics overlay. 16:9, 8k, photorealistic, no text, no numbers.",
                    "flow_i2v_prompt": "Smooth high-angle drone shot. The red car smoothly moves north along the central lane, coming to a steady stop at point B. Clean realistic urban vehicle motion, 4k.",
                    "hud_type": "animated_vector_road",
                    "hud_data": {
                        "origin": "Gốc O (Ngã tư)",
                        "destination": "Điểm B (Hướng Bắc)",
                        "vector_d": "Vectơ d_OB: 100 m hướng Bắc",
                        "highlight": "Biết cả ĐỘ DÀI (100 m) và HƯỚNG (Bắc) => Xác định chính xác vị trí!"
                    },
                    "speaker": "Hữu Trọng",
                    "voiceover_text": "Quay lại ví dụ ngã tư ban nãy: Nếu bây giờ mình nói rõ xe chạy 100 mét về hướng Bắc, các bạn sẽ chỉ ra ngay vị trí của xe tại điểm B trên bản đồ!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.8, "text": "Nếu bây giờ ta nói rõ: xe chạy 100 mét về hướng Bắc,"},
                        {"start": 3.8, "end": 7.5, "text": "các bạn sẽ chỉ ra ngay vị trí xe tại điểm B trên bản đồ!"}
                    ]
                },
                {
                    "scene_idx": 3,
                    "scene_id": "V2_S03",
                    "title": "Định nghĩa Độ dịch chuyển (Đại lượng Vectơ)",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Medium shot of the Vietnamese male student with glasses in white uniform standing on the left side of the science studio, right hand open in a demonstrative gesture pointing horizontally. Crisp soft lighting, negative space across the right two-thirds. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student speaks articulately, his right hand moving smoothly in a straight line from left to right as if tracing a glowing arrow. Natural facial animation and confident posture.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "ĐỘ DỊCH CHUYỂN (d)",
                        "symbol": "Vectơ d (có mũi tên)",
                        "definition": "Đại lượng vectơ cho biết ĐỘ DÀI và HƯỚNG thay đổi vị trí của vật",
                        "vector_elements": "Gốc tại vị trí đầu • Ngọn tại vị trí cuối • Độ dài tỉ lệ khoảng cách"
                    },
                    "speaker": "Hữu Trọng",
                    "voiceover_text": "Đại lượng vừa cho biết độ dài, vừa cho biết hướng thay đổi vị trí đó chính là Độ dịch chuyển, ký hiệu là vectơ d có dấu mũi tên trên đầu!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.8, "text": "Đại lượng vừa cho biết độ dài, vừa cho biết hướng thay đổi vị trí"},
                        {"start": 3.8, "end": 7.5, "text": "chính là Độ dịch chuyển, ký hiệu là vectơ d!"}
                    ]
                },
                {
                    "scene_idx": 4,
                    "scene_id": "V2_S04",
                    "title": "Mô hình 3 tuyến đường: Siêu thị A đến Bưu điện B",
                    "duration_sec": 8.0,
                    "keyframe_prompt": "Cinematic high-angle bird's-eye view of a modern European-style city district with two distinct landmarks: a modern glass supermarket building on the left and an iconic post office building with clock tower on the right, separated by green city squares and asphalt streets. 16:9, 8k, photorealistic, no text, no labels.",
                    "flow_i2v_prompt": "Slow gentle cinematic zoom-in towards the city area between the supermarket and the post office. Light traffic and pedestrians moving naturally. Perfect clean base for path overlays.",
                    "hud_type": "animated_vector_road",
                    "hud_data": {
                        "start_point": "Siêu thị A",
                        "end_point": "Bưu điện B",
                        "paths": [
                            {"id": "path1", "label": "Đường 1: Xe máy (s1 = 1200 m)", "type": "curve_orange"},
                            {"id": "path2", "label": "Đường 2: Đi bộ (s2 = 800 m)", "type": "straight_blue"},
                            {"id": "path3", "label": "Đường 3: Ô tô (s3 = 1500 m)", "type": "curve_green"}
                        ],
                        "vector_d": "Vectơ d chung: Mũi tên thẳng A -> B (|d| = 800 m)"
                    },
                    "speaker": "Hữu Trọng",
                    "voiceover_text": "Quan sát 3 người cùng đi từ Siêu thị A đến Bưu điện B: Người đi xe máy theo đường vòng, người đi bộ đi đường thẳng xuyên công viên, và người lái ô tô đi đường tránh.",
                    "subtitles": [
                        {"start": 0.0, "end": 4.0, "text": "Quan sát 3 người cùng đi từ Siêu thị A đến Bưu điện B:"},
                        {"start": 4.0, "end": 8.0, "text": "Đường 1 đi xe máy, đường 2 đi bộ, và đường 3 đi ô tô theo lộ trình khác nhau."}
                    ]
                },
                {
                    "scene_idx": 5,
                    "scene_id": "V2_S05",
                    "title": "Bản chất Quãng đường (s)",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Medium shot of the Vietnamese male student in glasses, speaking with an expressive explanatory hand gesture, standing on the left side of the modern studio. Right side empty with modern dark navy backdrop. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The presenter traces curving paths with his finger in the air, speaking clearly with lively facial expressions and head nods. Natural lighting and fluid movement.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "QUÃNG ĐƯỜNG ĐI ĐƯỢC (s)",
                        "nature": "Đại lượng vô hướng, luôn dương (s > 0)",
                        "definition": "Độ dài toàn bộ quỹ đạo thực tế vật đã vạch ra",
                        "comparison": "s1 ≠ s2 ≠ s3 (Phụ thuộc vào lộ trình mỗi người)"
                    },
                    "speaker": "Hữu Trọng",
                    "voiceover_text": "Quãng đường s là độ dài thực tế của đường đi. Ba người chọn ba lộ trình khác nhau nên quãng đường của họ chắc chắn khác nhau: s1 khác s2 và khác s3!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.6, "text": "Quãng đường s là độ dài thực tế của đường đi."},
                        {"start": 3.6, "end": 7.0, "text": "Ba người đi ba đường khác nhau nên s1 ≠ s2 ≠ s3!"}
                    ]
                },
                {
                    "scene_idx": 6,
                    "scene_id": "V2_S06",
                    "title": "Bản chất Độ dịch chuyển (d)",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Medium shot of the Vietnamese male student with glasses in white uniform, smiling broadly and pointing both index fingers decisively forward-right. Clean bright high-tech background, ample open area on the right. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student delivers a key takeaway, pointing firmly to the right, nodding with certainty, speaking with upbeat energetic cadence. High quality human motion.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "ĐỘ DỊCH CHUYỂN (d)",
                        "core_fact": "Chỉ quan tâm VỊ TRÍ ĐẦU (A) và VỊ TRÍ CUỐI (B)",
                        "result": "d1 = d2 = d3 = Vectơ AB",
                        "conclusion": "Độ dịch chuyển của cả 3 người là HOÀN TOÀN NHƯ NHAU!"
                    },
                    "speaker": "Hữu Trọng",
                    "voiceover_text": "Thế nhưng độ dịch chuyển d chỉ quan tâm đúng điểm đầu là siêu thị A và điểm cuối là bưu điện B. Vì cùng đi từ A đến B, độ dịch chuyển của cả ba người là như nhau!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.8, "text": "Độ dịch chuyển d chỉ quan tâm điểm đầu A và điểm cuối B."},
                        {"start": 3.8, "end": 7.5, "text": "Cùng đi từ A đến B nên độ dịch chuyển của cả ba người là hoàn toàn như nhau!"}
                    ]
                },
                {
                    "scene_idx": 7,
                    "scene_id": "V2_S07",
                    "title": "Bảng so sánh trực quan s vs d",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Medium wide shot of the Vietnamese male student standing respectfully to the far left of the modern studio, gesturing with an open palm toward the large open central and right space. Elegant dark navy tech background with subtle vertical light beams. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The presenter stands poised, gesturing sequentially from top to bottom as each row of the virtual comparison table illuminates. Natural breathing and friendly demeanor.",
                    "hud_type": "comparison_table",
                    "hud_data": {
                        "columns": ["Tiêu chí", "Quãng đường (s)", "Độ dịch chuyển (d)"],
                        "rows": [
                            ["Bản chất", "Đại lượng vô hướng", "Đại lượng vectơ (có hướng)"],
                            ["Dấu giá trị", "Luôn không âm (s ≥ 0)", "Có thể dương, âm hoặc bằng 0"],
                            ["Quỹ đạo", "Phụ thuộc hình dạng đường đi", "Chỉ phụ thuộc điểm đầu & cuối"]
                        ]
                    },
                    "speaker": "Hữu Trọng",
                    "voiceover_text": "Bảng so sánh này giúp các bạn nhớ ngay: Quãng đường là đại lượng vô hướng luôn dương và phụ thuộc quỹ đạo; còn độ dịch chuyển là đại lượng vectơ có thể âm, dương hoặc bằng 0!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Quãng đường là vô hướng luôn dương và phụ thuộc quỹ đạo;"},
                        {"start": 3.7, "end": 7.5, "text": "còn độ dịch chuyển là vectơ, có thể âm, dương hoặc bằng không!"}
                    ]
                },
                {
                    "scene_idx": 8,
                    "scene_id": "V2_S08",
                    "title": "Điều kiện cốt lõi: Khi nào |d| = s?",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic straight highway vanishing toward the horizon at sunset. A lone white sedan drives smoothly along a single lane. Large open sky and roadside space for formula callouts. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "Smooth tracking shot behind the car cruising straight forward along the road. Clean stable motion, sunset glow reflecting on road surface.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "QUY TẮC CỐT LÕI: KHI NÀO |d| = s?",
                        "condition": "Chuyển động THẲNG và KHÔNG ĐỔI CHIỀU",
                        "counter_case_1": "Đổi chiều / đường cong: |d| < s",
                        "counter_case_2": "Đi vòng khép kín về chỗ cũ: d = 0 dù s > 0"
                    },
                    "speaker": "Hữu Trọng",
                    "voiceover_text": "Một quy tắc vàng để làm bài thi: Độ lớn độ dịch chuyển chỉ bằng quãng đường khi và chỉ khi vật chuyển động thẳng và tuyệt đối không đổi chiều!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.5, "text": "Độ lớn độ dịch chuyển chỉ bằng quãng đường khi và chỉ khi"},
                        {"start": 3.5, "end": 7.5, "text": "vật chuyển động thẳng và tuyệt đối không đổi chiều!"}
                    ]
                },
                {
                    "scene_idx": 9,
                    "scene_id": "V2_S09",
                    "title": "Câu hỏi củng cố & Chào kết Video 2",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Medium close-up of the Vietnamese male student with glasses in white uniform, smiling warmly, holding up one finger playfully, posing a thought-provoking question. Soft blurred modern studio background. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student smiles, asks the quiz question with natural pauses, tilts head slightly waiting for the viewer's answer, then gives a friendly thumbs up and nod.",
                    "hud_type": "quiz_popup",
                    "hud_data": {
                        "question": "Bạn chạy 1 vòng sân vận động 400 m rồi về vạch xuất phát. Độ dịch chuyển d bằng bao nhiêu?",
                        "options": [
                            "A. d = 400 m",
                            "B. d = 0 m",
                            "C. d = 200 m"
                        ],
                        "correct_answer": "B",
                        "explanation": "Vị trí đầu trùng vị trí cuối nên vectơ d = 0 m dù s = 400 m."
                    },
                    "speaker": "Hữu Trọng",
                    "voiceover_text": "Thử tài nhanh: Nếu bạn chạy một vòng sân vận động 400 mét rồi về đúng vạch xuất phát, độ dịch chuyển bằng bao nhiêu? Chính là bằng không mét! Hẹn gặp lại các bạn ở Video 3!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.6, "text": "Chạy một vòng sân 400 m về chỗ cũ, độ dịch chuyển bằng bao nhiêu?"},
                        {"start": 3.6, "end": 7.0, "text": "Chính là 0 mét! Hẹn gặp lại các bạn ở Video 3!"}
                    ]
                }
            ]
        },

        # =========================================================================
        # VIDEO 3: BÀI 4 - PHẦN 3
        # =========================================================================
        {
            "video_id": "V3_B4_TongHop_DoDichChuyen",
            "title": "Bài 4 (Phần 3): Tổng hợp Độ dịch chuyển",
            "lesson": "Bài 4: Độ dịch chuyển và quãng đường đi được",
            "part": 3,
            "group_assignment": "Anh Thư, Hữu Trọng, Thế Mỹ",
            "theme": "Cộng vectơ độ dịch chuyển, ví dụ tam giác vuông Pitago (4km Đông + 4km Bắc), 3 trường hợp góc",
            "mc_character": {
                "name": "Thế Mỹ",
                "gender": "male",
                "age": 16,
                "role": "Lead Presenter - Dynamic, confident Vietnamese male high school student",
                "appearance_prompt_en": "A 16-year-old Vietnamese male high school student with clean modern side-part black hair, confident and enthusiastic expression, wearing a crisp white high school uniform shirt with neat buttoned collar. Sharp presenter posture, lively hand gestures and charismatic voice."
            },
            "clip_count": 9,
            "total_estimated_duration_sec": 65.5,
            "scenes": [
                {
                    "scene_idx": 1,
                    "scene_id": "V3_S01",
                    "title": "Mở đầu & Tiêu đề Video 3",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Cinematic medium shot of a 16-year-old Vietnamese male high school student with clean modern side-part black hair and a confident, enthusiastic expression, wearing a crisp white high school uniform shirt. He stands on the left of a high-tech physics simulation laboratory with sleek glass equipment in soft background blur. The right 65% is clean open space. 16:9, 8k, photorealistic, no text, no symbols.",
                    "flow_i2v_prompt": "The male student steps forward slightly with a friendly smile, extends an inviting hand gesture toward the audience, and introduces the video topic with animated, natural speech. High fidelity facial animation, 4k.",
                    "hud_type": "title_banner",
                    "hud_data": {
                        "banner_title": "BÀI 4: ĐỘ DỊCH CHUYỂN & QUÃNG ĐƯỜNG",
                        "badge": "VẬT LÍ 10 - KNTT",
                        "subtitle": "Phần 3: Tổng hợp Độ dịch chuyển bằng phương pháp Vectơ",
                        "presenters": "Nhóm: Thế Mỹ • Anh Thư • Hữu Trọng",
                        "theme_color": "cyan_glow"
                    },
                    "speaker": "Thế Mỹ",
                    "voiceover_text": "Chào mừng thầy cô và các bạn đến với phần 3 của Bài 4! Khi một vật di chuyển qua nhiều chặng liên tiếp, làm sao tính được độ dịch chuyển chung cuộc? Cùng nhóm mình tìm hiểu nhé!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.4, "text": "Chào mừng thầy cô và các bạn đến với phần 3 của Bài 4!"},
                        {"start": 3.4, "end": 7.0, "text": "Khi vật đi qua nhiều chặng, làm sao tính được độ dịch chuyển chung cuộc?"}
                    ]
                },
                {
                    "scene_idx": 2,
                    "scene_id": "V3_S02",
                    "title": "Quy tắc cộng vectơ tổng quát",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Medium shot of the Vietnamese male student standing on the left side of the lab, gesturing with both hands outward to frame a virtual graphic area on his right. Soft studio lighting with cool cyan rim light, 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student speaks with clear diction and confidence, his hands gesturing to connect two conceptual points in space. Subtle eye blinks, natural shoulder breathing.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "QUY TẮC CỘNG VECTƠ TỔNG HỢP",
                        "formula": "Vectơ d = Vectơ d1 + Vectơ d2",
                        "rule": "Độ dịch chuyển tổng hợp là vectơ nối từ điểm xuất phát đầu tiên đến điểm kết thúc cuối cùng"
                    },
                    "speaker": "Thế Mỹ",
                    "voiceover_text": "Trong Vật lí, nếu vật thực hiện liên tiếp các độ dịch chuyển d1 và d2, thì độ dịch chuyển tổng hợp d được tính bằng quy tắc cộng vectơ: vectơ d bằng vectơ d1 cộng vectơ d2!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.5, "text": "Khi vật thực hiện liên tiếp các độ dịch chuyển d1 và d2,"},
                        {"start": 3.5, "end": 7.0, "text": "độ dịch chuyển tổng hợp là vectơ d = d1 + d2!"}
                    ]
                },
                {
                    "scene_idx": 3,
                    "scene_id": "V3_S03",
                    "title": "Ví dụ thực tế: Đi 4 km Đông rồi 4 km Bắc",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Aerial high-angle bird's-eye view of a modern landscaped city park with square walking paths, green lawns, and rectangular flowerbeds. Crisp sunlight, clear pathways. Completely clean open landscape free of text or labels. 16:9, 8k, photorealistic.",
                    "flow_i2v_prompt": "Smooth aerial camera hover over the park. Subtle breeze moving treetop foliage. Stable ground plane, ideal for overlaying animated vector paths.",
                    "hud_type": "animated_vector_road",
                    "hud_data": {
                        "origin_A": "Điểm xuất phát A",
                        "segment_1": "A -> B: d1 = 4 km (Hướng Đông)",
                        "segment_2": "B -> C: d2 = 4 km (Hướng Bắc, góc 90°)",
                        "vector_d": "Vectơ d = Vectơ AC (Đường chéo)"
                    },
                    "speaker": "Thế Mỹ",
                    "voiceover_text": "Hãy xét ví dụ này: Một bạn học sinh đi từ điểm A sang B 4 km về hướng Đông, sau đó rẽ vuông góc từ B lên C 4 km về hướng Bắc.",
                    "subtitles": [
                        {"start": 0.0, "end": 3.6, "text": "Một bạn học sinh đi từ A sang B 4 km về hướng Đông,"},
                        {"start": 3.6, "end": 7.5, "text": "sau đó rẽ vuông góc từ B lên C 4 km về hướng Bắc."}
                    ]
                },
                {
                    "scene_idx": 4,
                    "scene_id": "V3_S04",
                    "title": "Tính Quãng đường (s)",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Medium shot of the Vietnamese male student in white uniform, pointing toward the right space with a light smile, explaining a simple math concept. High-tech lab backdrop with subtle cyan glow. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student raises two fingers to indicate addition, speaking energetically with expressive eyes and friendly smile. Natural motion.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "step": "BƯỚC 1: TÍNH QUÃNG ĐƯỜNG (s)",
                        "calculation": "s = s1 + s2 = 4 km + 4 km = 8 km",
                        "note": "Quãng đường là tổng đại số chiều dài các đoạn đường thực tế"
                    },
                    "speaker": "Thế Mỹ",
                    "voiceover_text": "Về quãng đường, bạn ấy đã bước đi thực tế 4 km rồi thêm 4 km nữa, tổng cộng quãng đường s bằng 8 km. Quá đơn giản phải không nào?",
                    "subtitles": [
                        {"start": 0.0, "end": 3.5, "text": "Về quãng đường: s = 4 km + 4 km = 8 km."},
                        {"start": 3.5, "end": 7.0, "text": "Quãng đường là tổng chiều dài thực tế đã bước đi."}
                    ]
                },
                {
                    "scene_idx": 5,
                    "scene_id": "V3_S05",
                    "title": "Tính Độ dịch chuyển (d) bằng Định lý Pythagoras",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic high-angle view of a sleek futuristic digital laboratory floor with dark reflective tiles and soft grid lines. Deep blue and slate atmosphere, ample clear central space for a glowing 3D holographic triangle. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "Slow smooth pedestal camera move up. The reflective floor catches subtle neon reflections. High-tech educational laboratory setting.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "step": "BƯỚC 2: TÍNH ĐỘ DỊCH CHUYỂN (d)",
                        "method": "Áp dụng định lý Pythagoras cho tam giác vuông ABC:",
                        "formula": "d = √(d1² + d2²) = √(4² + 4²) = √32 ≈ 5,66 km",
                        "direction": "Hướng Đông - Bắc (Góc 45°)"
                    },
                    "speaker": "Thế Mỹ",
                    "voiceover_text": "Nhưng độ dịch chuyển tổng hợp lại là đường chéo nối thẳng từ A đến C. Vì hai chặng vuông góc, ta dùng định lý Pitago: d bằng căn của 4 bình cộng 4 bình, ra khoảng 5,7 km theo hướng Đông - Bắc!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Độ dịch chuyển tổng hợp là đường chéo nối thẳng A đến C."},
                        {"start": 3.7, "end": 7.5, "text": "Áp dụng Pitago: d = √(4² + 4²) ≈ 5,7 km theo hướng Đông - Bắc!"}
                    ]
                },
                {
                    "scene_idx": 6,
                    "scene_id": "V3_S06",
                    "title": "So sánh s (8 km) vs |d| (5,7 km)",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Medium shot of the Vietnamese male student in white uniform, holding his palms apart to compare two quantities, standing in the modern science lab. Right side open space with soft cyan lighting. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student looks between camera and the virtual numbers, nodding meaningfully, emphasizing the physical difference between distance and displacement with animated hand gestures.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "SO SÁNH KẾT QUẢ",
                        "distance": "Quãng đường: s = 8 km",
                        "displacement": "Độ lớn độ dịch chuyển: |d| ≈ 5,7 km",
                        "rule": "|d| < s do đường đi bị gãy khúc đổi hướng!"
                    },
                    "speaker": "Thế Mỹ",
                    "voiceover_text": "Rõ ràng quãng đường 8 km lớn hơn hẳn độ lớn độ dịch chuyển 5,7 km. Một lần nữa chứng minh: cứ đổi hướng là độ dịch chuyển sẽ nhỏ hơn quãng đường!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.5, "text": "Quãng đường 8 km lớn hơn hẳn độ dịch chuyển 5,7 km."},
                        {"start": 3.5, "end": 7.0, "text": "Cứ đổi hướng thì độ dịch chuyển luôn nhỏ hơn quãng đường!"}
                    ]
                },
                {
                    "scene_idx": 7,
                    "scene_id": "V3_S07",
                    "title": "3 Trường hợp tổng hợp vectơ đặc biệt",
                    "duration_sec": 8.0,
                    "keyframe_prompt": "Medium wide shot of the Vietnamese male student standing on the left side of the spacious tech studio, hands gesturing across three vertical imaginary zones on his right. Modern ambient blue lighting. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The presenter sweeps his hand smoothly across three vertical segments, speaking clearly with structured pedagogical pacing.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "3 TRƯỜNG HỢP VECTƠ ĐẶC BIỆT",
                        "case_1": "1. Cùng phương, cùng chiều: d = d1 + d2",
                        "case_2": "2. Cùng phương, ngược chiều: d = |d1 - d2|",
                        "case_3": "3. Vuông góc nhau: d = √(d1² + d2²)"
                    },
                    "speaker": "Thế Mỹ",
                    "voiceover_text": "Để làm bài nhanh, các bạn chỉ cần nhớ: cùng chiều thì cộng, ngược chiều thì lấy hiệu trị tuyệt đối, còn vuông góc nhau thì dùng ngay định lý Pitago!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.8, "text": "Cùng chiều thì cộng (d = d1 + d2), ngược chiều thì trừ (d = |d1 - d2|),"},
                        {"start": 3.8, "end": 8.0, "text": "còn vuông góc nhau thì dùng ngay Pitago: d = √(d1² + d2²)!"}
                    ]
                },
                {
                    "scene_idx": 8,
                    "scene_id": "V3_S08",
                    "title": "Câu hỏi tương tác Pop-up Bài 4",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Medium close-up of the Vietnamese male student in white uniform, smiling warmly, holding up a finger as he poses a brain teaser. Soft tech lab background. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student speaks playfully to the camera, gestures toward the quiz card popping up, smiles waiting for the answer.",
                    "hud_type": "quiz_popup",
                    "hud_data": {
                        "question": "Hai độ dịch chuyển d1 = 3 m và d2 = 4 m vuông góc nhau. Độ dịch chuyển tổng hợp bằng?",
                        "options": [
                            "A. 7 m",
                            "B. 1 m",
                            "C. 5 m"
                        ],
                        "correct_answer": "C",
                        "explanation": "d = √(3² + 4²) = √25 = 5 m (bộ ba Pitago kinh điển)."
                    },
                    "speaker": "Thế Mỹ",
                    "voiceover_text": "Câu hỏi nhanh cho các bạn: Nếu d1 bằng 3 mét và d2 bằng 4 mét vuông góc nhau, độ dịch chuyển tổng hợp là bao nhiêu? Rất nhanh, chính là 5 mét!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.4, "text": "Nếu d1 = 3 m và d2 = 4 m vuông góc nhau, độ dịch chuyển d bằng bao nhiêu?"},
                        {"start": 3.4, "end": 7.0, "text": "Chính là 5 mét theo bộ ba số Pitago 3-4-5!"}
                    ]
                },
                {
                    "scene_idx": 9,
                    "scene_id": "V3_S09",
                    "title": "Tổng kết toàn bộ Bài 4 & Lời cảm ơn",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Medium shot of the Vietnamese male student in white uniform standing proudly in the modern physics lab, smiling warmly with a polite bow and wave. Bright, encouraging studio lighting, 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student bows respectfully with hands together, smiles broadly, and waves goodbye to the camera. Warm closing animation.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "HOÀN THÀNH BÀI 4 - ĐỘ DỊCH CHUYỂN",
                        "recap": [
                            "✓ Phần 1: Vị trí & Hệ quy chiếu",
                            "✓ Phần 2: Phân biệt Quãng đường (s) & Độ dịch chuyển (d)",
                            "✓ Phần 3: Tổng hợp vectơ độ dịch chuyển"
                        ],
                        "presenters": "Nhóm thực hiện: Anh Thư • Hữu Trọng • Thế Mỹ",
                        "thanks": "Cảm ơn thầy cô và các bạn đã theo dõi!"
                    },
                    "speaker": "Thế Mỹ",
                    "voiceover_text": "Như vậy nhóm mình đã đồng hành trọn vẹn cùng các bạn qua 3 phần của Bài 4. Cảm ơn thầy cô và các bạn đã chú ý lắng nghe bài thuyết trình của nhóm mình!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.8, "text": "Như vậy nhóm mình đã đi trọn vẹn 3 phần của Bài 4."},
                        {"start": 3.8, "end": 7.5, "text": "Cảm ơn thầy cô và các bạn đã theo dõi bài thuyết trình!"}
                    ]
                }
            ]
        },

        # =========================================================================
        # VIDEO 4: BÀI 5 - NHÓM 1 - PHẦN 1
        # =========================================================================
        {
            "video_id": "V4_B5_Nhom1_TocDo_VanToc",
            "title": "Bài 5 (Nhóm 1 - Phần 1): Tốc độ & Vận tốc",
            "lesson": "Bài 5: Tốc độ và vận tốc",
            "part": 1,
            "group_assignment": "Nhóm 1 (Tú Châu, Minh Dũng, Bảo Hân)",
            "idea_theme": "Đường đua điền kinh 100m, đồng hồ tốc kế xe máy, phân biệt đại lượng vô hướng vs vectơ",
            "mc_character": {
                "name": "Tú Châu",
                "gender": "female",
                "age": 16,
                "role": "Lead Presenter (Nhóm 1) - Sporty, energetic Vietnamese female high school student",
                "appearance_prompt_en": "A 16-year-old Vietnamese female high school student with an athletic build and neat high ponytail tied with a subtle royal-blue ribbon, radiant bright smile, wearing a modern royal-blue collared school sports polo shirt with white side stripes. Energetic, lively and articulate."
            },
            "clip_count": 6,
            "total_estimated_duration_sec": 44.5,
            "scenes": [
                {
                    "scene_idx": 1,
                    "scene_id": "V4_S01",
                    "title": "Mở đầu & Tiêu đề Bài 5 Nhóm 1",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Cinematic medium shot of a 16-year-old Vietnamese female high school student with athletic posture and neat high ponytail tied with a subtle blue ribbon, bright friendly smile, wearing a modern royal-blue collared school sports polo shirt. She stands on the left of an indoor athletic science studio overlooking an Olympic running track. Ample clean negative space on the right 60%. 16:9, 8k, photorealistic, no text, no logos.",
                    "flow_i2v_prompt": "The female student smiles energetically, gestures warmly toward the camera, speaking with vibrant cadence. The sports stadium background remains soft and steady, 4k.",
                    "hud_type": "title_banner",
                    "hud_data": {
                        "banner_title": "BÀI 5: TỐC ĐỘ VÀ VẬN TỐC",
                        "badge": "NHÓM 1 - VẬT LÍ 10",
                        "subtitle": "Phần 1: Phân biệt Tốc độ và Vận tốc",
                        "presenters": "Nhóm 1: Tú Châu • Minh Dũng • Bảo Hân",
                        "theme_color": "cyan_glow"
                    },
                    "speaker": "Tú Châu",
                    "voiceover_text": "Chào thầy cô và các bạn! Nhóm 1 xin chào mừng mọi người đến với Bài 5: Tốc độ và Vận tốc – hai khái niệm tưởng giống mà lại khác biệt hoàn toàn!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.3, "text": "Chào thầy cô và các bạn! Nhóm 1 xin chào mừng mọi người"},
                        {"start": 3.3, "end": 7.0, "text": "đến với Bài 5: Tốc độ và Vận tốc trong môn Vật lí 10!"}
                    ]
                },
                {
                    "scene_idx": 2,
                    "scene_id": "V4_S02",
                    "title": "Vận động viên 100m: Tốc độ trung bình",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic side-angle tracking shot of an athletic sprinter in dynamic motion sprinting along a crimson running track under bright stadium floodlights. Crisp motion blur in background, sharp focus on the runner. Clean upper sky and open track lanes for holographic speedometer and timer. 16:9, 8k, photorealistic, no text, no numbers.",
                    "flow_i2v_prompt": "Dynamic slow-motion tracking shot gliding smoothly alongside the sprinter as they power toward the finish line. Athletic vigor, stadium breeze, cinematic 4k.",
                    "hud_type": "speed_gauge",
                    "hud_data": {
                        "distance": "s = 100 m",
                        "time": "t = 9,98 s",
                        "formula": "TỐC ĐỘ TRUNG BÌNH: v = s / t",
                        "result": "v = 100 / 9,98 ≈ 10,02 m/s (36,1 km/h)"
                    },
                    "speaker": "Tú Châu",
                    "voiceover_text": "Khi quan sát vận động viên điền kinh chạy 100 mét trong 9,98 giây, ta tính được tốc độ trung bình: lấy quãng đường chia thời gian, đạt xấp xỉ 10 mét trên giây!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.8, "text": "Vận động viên điền kinh chạy 100 m trong 9,98 giây:"},
                        {"start": 3.8, "end": 7.5, "text": "Tốc độ trung bình v = s / t ≈ 10 m/s (36 km/h)!"}
                    ]
                },
                {
                    "scene_idx": 3,
                    "scene_id": "V4_S03",
                    "title": "Đồng hồ xe máy: Tốc độ tức thời",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic close-up perspective from behind motorcycle handlebars riding smoothly along a twilight asphalt city boulevard. The circular mechanical speedometer dial is in center-left foreground. The upper right has soft blurred city bokeh with vast negative space for digital gauge overlays. 16:9, 8k, photorealistic, no pre-rendered numbers on dial.",
                    "flow_i2v_prompt": "Smooth driving camera movement as motorcycle glides along the street. Street lamps pass by rhythmically. Stable handlebar view, ideal for overlaying animated speedometer gauge needle and digital readouts.",
                    "hud_type": "speed_gauge",
                    "hud_data": {
                        "mode": "TỐC ĐỘ TỨC THỜI",
                        "speedometer": "Kim chỉ: 50 km/h",
                        "definition": "Đo độ nhanh chậm tại đúng thời điểm quan sát",
                        "device": "Tốc kế xe máy / ô tô"
                    },
                    "speaker": "Tú Châu",
                    "voiceover_text": "Còn con số nhảy liên tục trên đồng hồ xe máy lúc chúng mình đang chạy xe chính là Tốc độ tức thời – cho biết mức độ nhanh chậm tại đúng thời điểm đó.",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Con số hiện trên đồng hồ xe máy khi đang di chuyển"},
                        {"start": 3.7, "end": 7.5, "text": "chính là Tốc độ tức thời tại thời điểm đó!"}
                    ]
                },
                {
                    "scene_idx": 4,
                    "scene_id": "V4_S04",
                    "title": "Tại sao cần Vận tốc? Hướng chuyển động",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Medium shot of the Vietnamese female student in sports polo, speaking expressively with hand gestures indicating two opposite directions, standing on the left side of the athletic studio. Right side dark slate background with subtle cyan lighting. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student gestures with left and right hands pointing opposite ways, speaking with lively engaging expressions, explaining the dilemma of direction.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "issue": "HẠN CHẾ CỦA TỐC ĐỘ",
                        "description": "Tốc độ chỉ đo nhanh hay chậm, KHÔNG CHO BIẾT HƯỚNG!",
                        "solution": "Khái niệm VẬN TỐC (Velocity)",
                        "formula": "Vectơ v = Vectơ d / t"
                    },
                    "speaker": "Tú Châu",
                    "voiceover_text": "Tuy nhiên, tốc độ không cho biết vật đang lao về hướng nào. Vì thế, chúng ta cần khái niệm Vận tốc: Vận tốc trung bình bằng độ dịch chuyển chia cho thời gian!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.6, "text": "Tốc độ không cho biết vật đang lao về hướng nào."},
                        {"start": 3.6, "end": 7.5, "text": "Vì thế, ta cần Vận tốc: vectơ v = vectơ d / t!"}
                    ]
                },
                {
                    "scene_idx": 5,
                    "scene_id": "V4_S05",
                    "title": "Bảng so sánh 2 cột: Tốc độ vs Vận tốc",
                    "duration_sec": 8.0,
                    "keyframe_prompt": "Medium wide shot of the Vietnamese female student in blue sports polo standing on the far left, gesturing toward the center-right presentation area. Studio atmosphere with blue lighting accents. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The student stands poised, gesturing cleanly to each row of the virtual comparison table as it lights up. Realistic subtle breathing and blinking.",
                    "hud_type": "comparison_table",
                    "hud_data": {
                        "columns": ["Đặc điểm", "Tốc độ (Speed)", "Vận tốc (Velocity)"],
                        "rows": [
                            ["Công thức", "v = s / t", "v = d / t (vectơ)"],
                            ["Bản chất", "Đại lượng vô hướng (v ≥ 0)", "Đại lượng vectơ (có hướng)"],
                            ["Dấu", "Luôn không âm", "Có thể âm, dương hoặc bằng 0"]
                        ]
                    },
                    "speaker": "Tú Châu",
                    "voiceover_text": "Nhìn vào bảng phân biệt: Tốc độ bằng quãng đường chia thời gian, là vô hướng luôn dương. Còn vận tốc bằng độ dịch chuyển chia thời gian, là đại lượng vectơ có cả hướng và độ lớn!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.8, "text": "Tốc độ v = s/t là vô hướng, không bao giờ âm;"},
                        {"start": 3.8, "end": 8.0, "text": "còn vận tốc v = d/t mang tính vectơ, có thể âm, dương hoặc bằng 0!"}
                    ]
                },
                {
                    "scene_idx": 6,
                    "scene_id": "V4_S06",
                    "title": "Câu hỏi tương tác & Chào kết Video 4",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Medium close-up of the Vietnamese female student in sports polo, smiling warmly and confidently, holding an athletic digital stopwatch in her hand, looking into the lens. Soft blurred gym studio background. 16:9, 8k, photorealistic, no text on stopwatch.",
                    "flow_i2v_prompt": "The student raises the stopwatch slightly, clicks it cheerfully, smiles at the camera, and poses the quiz challenge with inviting hand motions.",
                    "hud_type": "quiz_popup",
                    "hud_data": {
                        "question": "Khi nào độ lớn của vận tốc bằng tốc độ?",
                        "options": [
                            "A. Khi vật chuyển động tròn đều",
                            "B. Khi vật chuyển động thẳng không đổi hướng",
                            "C. Khi vật chuyển động lùi"
                        ],
                        "correct_answer": "B",
                        "explanation": "Khi thẳng không đổi hướng thì |d| = s nên |v| = v_tocdo."
                    },
                    "speaker": "Tú Châu",
                    "voiceover_text": "Câu hỏi cho các bạn: Khi nào độ lớn vận tốc bằng tốc độ? Chính là khi vật chuyển động thẳng không đổi hướng! Cùng đón xem Video 5 tiếp theo nhé!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.5, "text": "Khi nào độ lớn vận tốc bằng đúng tốc độ?"},
                        {"start": 3.5, "end": 7.0, "text": "Khi chuyển động thẳng không đổi hướng! Hẹn gặp lại ở Video 5!"}
                    ]
                }
            ]
        },

        # =========================================================================
        # VIDEO 5: BÀI 5 - NHÓM 1 - PHẦN 2
        # =========================================================================
        {
            "video_id": "V5_B5_Nhom1_TongHop_VanToc",
            "title": "Bài 5 (Nhóm 1 - Phần 2): Tổng hợp Vận tốc & Công thức cộng",
            "lesson": "Bài 5: Tốc độ và vận tốc",
            "part": 2,
            "group_assignment": "Nhóm 1 (Tú Châu, Minh Dũng, Bảo Hân)",
            "idea_theme": "Hành khách trên tàu hỏa chạy, ca nô qua sông nước chảy xiết, quy ước 1-2-3",
            "mc_character": {
                "name": "Minh Dũng",
                "gender": "male",
                "age": 16,
                "role": "Lead Presenter (Nhóm 1) - Energetic, charismatic Vietnamese male high school student",
                "appearance_prompt_en": "A 16-year-old Vietnamese male high school student with athletic build, modern short fade haircut, confident friendly smile, wearing a dark navy blue collared team polo shirt with white trim. Dynamic presenter with expressive gestures."
            },
            "clip_count": 5,
            "total_estimated_duration_sec": 38.0,
            "scenes": [
                {
                    "scene_idx": 1,
                    "scene_id": "V5_S01",
                    "title": "Mở đầu & Tiêu đề Bài 5 Nhóm 1 (Phần 2)",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic medium shot of a 16-year-old Vietnamese male high school student with neat short fade haircut, confident friendly smile, wearing a navy blue collared school polo shirt. He stands on the left of a transportation science laboratory with sleek model tracks and displays in the soft background. The right 65% is clean open space. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The male student speaks with enthusiasm, gesturing smoothly toward the empty space on his right. Natural head movements, eye contact with camera, 4k cinematic presentation.",
                    "hud_type": "title_banner",
                    "hud_data": {
                        "banner_title": "BÀI 5: TỐC ĐỘ VÀ VẬN TỐC",
                        "badge": "NHÓM 1 - VẬT LÍ 10",
                        "subtitle": "Phần 2: Công thức cộng vận tốc & Tổng hợp vận tốc",
                        "presenters": "Nhóm 1: Minh Dũng • Tú Châu • Bảo Hân",
                        "theme_color": "cyan_glow"
                    },
                    "speaker": "Minh Dũng",
                    "voiceover_text": "Chào các bạn! Đã bao giờ bạn tự hỏi: Khi bạn bước đi trên một toa tàu đang chạy, thì vận tốc thực sự của bạn đối với người đứng bên đường là bao nhiêu?",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Khi bạn bước đi trên một toa tàu đang chạy,"},
                        {"start": 3.7, "end": 7.5, "text": "vận tốc thực sự của bạn với người đứng bên đường là bao nhiêu?"}
                    ]
                },
                {
                    "scene_idx": 2,
                    "scene_id": "V5_S02",
                    "title": "Mô hình Tàu hỏa: Quy ước 3 vật thể (1 - 2 - 3)",
                    "duration_sec": 8.0,
                    "keyframe_prompt": "Cinematic side-profile shot of a sleek modern passenger train cruising smoothly along railway tracks through open green fields. Clear open sky above the train and spacious foreground for floating holographic diagrams. 16:9, 8k, photorealistic, no letters or numbers on train.",
                    "flow_i2v_prompt": "Smooth tracking camera pacing alongside the moving passenger train. Wheels roll realistically, distant countryside shifts with subtle parallax. Stable frame for vector overlays.",
                    "hud_type": "animated_vector_road",
                    "hud_data": {
                        "object_1": "(1) Người hành khách (Vật chuyển động)",
                        "object_2": "(2) Toa tàu hỏa (Hệ quy chiếu chuyển động)",
                        "object_3": "(3) Mặt đường ray (Hệ quy chiếu đứng yên)",
                        "vectors": [
                            "v12: Vận tốc tương đối (Người / Tàu)",
                            "v23: Vận tốc kéo theo (Tàu / Đất)",
                            "v13: Vận tốc tuyệt đối (Người / Đất)"
                        ]
                    },
                    "speaker": "Minh Dũng",
                    "voiceover_text": "Để giải bài toán này, nhóm mình chia sẻ mẹo đánh số cực chuẩn: Số 1 là người chuyển động, số 2 là toa tàu đang chạy, và số 3 là mặt đất đứng yên.",
                    "subtitles": [
                        {"start": 0.0, "end": 4.0, "text": "Quy ước cực dễ nhớ: Số 1 là bạn (vật chuyển động),"},
                        {"start": 4.0, "end": 8.0, "text": "số 2 là toa tàu (HQC chuyển động), và số 3 là mặt đất (HQC đứng yên)."}
                    ]
                },
                {
                    "scene_idx": 3,
                    "scene_id": "V5_S03",
                    "title": "Công thức cộng vận tốc tổng quát",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Medium shot of the Vietnamese male student in navy polo, hands framing a central formula space with conviction. Modern lab interior with ambient blue glow. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The presenter explains the formula with animated hand gestures, nodding to emphasize the vector sum rule, fluid mouth movement and posture.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "formula": "Vectơ v_1,3 = Vectơ v_1,2 + Vectơ v_2,3",
                        "case_same": "Cùng chiều tàu: v_1,3 = v_1,2 + v_2,3 (Cộng dồn vận tốc)",
                        "case_opposite": "Ngược chiều tàu: v_1,3 = |v_1,2 - v_2,3| (Trừ bớt vận tốc)"
                    },
                    "speaker": "Minh Dũng",
                    "voiceover_text": "Công thức cộng vận tốc phát biểu: Vận tốc tuyệt đối v13 bằng vectơ v12 cộng vectơ v23! Đi cùng chiều thì cộng dồn, đi ngược chiều thì lấy hiệu trừ bớt.",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Công thức cộng vận tốc: Vectơ v_1,3 = Vectơ v_1,2 + Vectơ v_2,3."},
                        {"start": 3.7, "end": 7.5, "text": "Đi cùng chiều thì cộng dồn, ngược chiều thì lấy hiệu trừ bớt!"}
                    ]
                },
                {
                    "scene_idx": 4,
                    "scene_id": "V5_S04",
                    "title": "Mô hình Ca nô vượt sông vuông góc (Pitago)",
                    "duration_sec": 8.0,
                    "keyframe_prompt": "Cinematic high-angle drone shot looking down at a wide scenic river with rippling turquoise water between two lush green riverbanks. A small white motorboat moves across the water. Clear expansive water surface perfect for vector arrows. 16:9, 8k, photorealistic, no text, no symbols.",
                    "flow_i2v_prompt": "Smooth aerial drone hover shot over the river. The small boat moves diagonally across the flowing water, water ripples trail behind it. Natural flowing water dynamics.",
                    "hud_type": "animated_vector_road",
                    "hud_data": {
                        "bank": "Bờ sông (Vật 3)",
                        "current": "Nước chảy ngang (v23 = 3 m/s)",
                        "boat_speed": "Mũi thuyền thẳng qua sông (v12 = 4 m/s)",
                        "result_vector": "Thuyền trôi chéo v13",
                        "pythagoras": "v_1,3 = √(v_1,2² + v_2,3²) = √(4² + 3²) = 5 m/s"
                    },
                    "speaker": "Minh Dũng",
                    "voiceover_text": "Còn khi ca nô qua sông có dòng nước chảy xiết: Mũi thuyền hướng vuông góc nhưng nước đẩy ngang, ta dùng Pitago tính được vận tốc tuyệt đối bằng 5 mét trên giây!",
                    "subtitles": [
                        {"start": 0.0, "end": 4.0, "text": "Khi ca nô qua sông bị nước đẩy vuông góc bờ:"},
                        {"start": 4.0, "end": 8.0, "text": "Áp dụng Pitago: v_1,3 = √(4² + 3²) = 5 m/s theo hướng chéo!"}
                    ]
                },
                {
                    "scene_idx": 5,
                    "scene_id": "V5_S05",
                    "title": "Tổng kết Nhóm 1 & Chào kết thúc",
                    "duration_sec": 7.0,
                    "keyframe_prompt": "Medium shot of the Vietnamese male student in navy polo standing smiling warmly, hand raised in an appreciative salute gesture to the audience. Bright modern studio background, 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The presenter smiles warmly, bows slightly with hands together, and waves to conclude the presentation. Natural friendly human motion.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "TỔNG KẾT BÀI 5 - NHÓM 1",
                        "key_points": [
                            "✓ Tốc độ v = s/t (Vô hướng, nhanh chậm)",
                            "✓ Vận tốc v = d/t (Vectơ, có hướng)",
                            "✓ v_1,3 = v_1,2 + v_2,3 (Quy ước 1-2-3)"
                        ],
                        "team": "Nhóm 1: Tú Châu • Minh Dũng • Bảo Hân",
                        "thanks": "Cảm ơn thầy cô và các bạn đã lắng nghe!"
                    },
                    "speaker": "Minh Dũng",
                    "voiceover_text": "Chỉ cần nhớ mẹo đánh số 1-2-3 và quy tắc hình học, mọi bài toán cộng vận tốc đều cực kỳ dễ dàng! Cảm ơn thầy cô và các bạn đã theo dõi video của Nhóm 1!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.5, "text": "Nắm vững mẹo 1-2-3, bài toán cộng vận tốc sẽ cực kỳ dễ dàng!"},
                        {"start": 3.5, "end": 7.0, "text": "Cảm ơn thầy cô và các bạn đã theo dõi video của Nhóm 1!"}
                    ]
                }
            ]
        },

        # =========================================================================
        # VIDEO 6: BÀI 5 - NHÓM 2 - PHẦN 1
        # =========================================================================
        {
            "video_id": "V6_B5_Nhom2_TocDo_VanToc",
            "title": "Bài 5 (Nhóm 2 - Phần 1): Tốc độ & Vận tốc (Góc nhìn Công nghệ)",
            "lesson": "Bài 5: Tốc độ và vận tốc",
            "part": 1,
            "group_assignment": "Nhóm 2 (Hoàng Nam, Cẩm Nhung, Bảo Yến)",
            "idea_theme": "Flycam/Drone công nghệ cao ghi hình xe đạp đua gắn GPS, băng chuyền sân bay vận tốc âm dương",
            "mc_character": {
                "name": "Hoàng Nam",
                "gender": "male",
                "age": 16,
                "role": "Lead Presenter (Nhóm 2) - Tech-savvy, modern Vietnamese male student",
                "appearance_prompt_en": "A 16-year-old tech-savvy Vietnamese male high school student with modern stylish glasses, neat haircut, wearing a sleek graphite-grey zip-up tech jacket over a crisp white tee. Modern, confident, tech-enthusiast demeanor."
            },
            "clip_count": 5,
            "total_estimated_duration_sec": 38.0,
            "scenes": [
                {
                    "scene_idx": 1,
                    "scene_id": "V6_S01",
                    "title": "Mở đầu & Tiêu đề Bài 5 Nhóm 2",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic medium shot of a 16-year-old tech-savvy Vietnamese male high school student with stylish modern glasses, wearing a sleek graphite-grey zip-up tech jacket over a plain white t-shirt. He stands on the left of a high-tech drone robotics innovation laboratory with carbon fiber drone frames blurred in the background. Right 65% is clean open negative space. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The tech student speaks with crisp enthusiasm, holding a sleek compact drone controller, nodding and smiling warmly to the camera. High tech ambiance, 4k.",
                    "hud_type": "title_banner",
                    "hud_data": {
                        "banner_title": "BÀI 5: TỐC ĐỘ VÀ VẬN TỐC",
                        "badge": "NHÓM 2 - GÓC NHÌN HIỆN ĐẠI",
                        "subtitle": "Phần 1: Định vị GPS, Tốc kế số & Vectơ Vận tốc",
                        "presenters": "Nhóm 2: Hoàng Nam • Cẩm Nhung • Bảo Yến",
                        "theme_color": "cyan_glow"
                    },
                    "speaker": "Hoàng Nam",
                    "voiceover_text": "Chào mừng thầy cô và các bạn đến với góc nhìn công nghệ của Nhóm 2! Hôm nay tụi mình sẽ khám phá Tốc độ và Vận tốc qua thiết bị GPS và thiết bị bay flycam!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Chào mừng thầy cô và các bạn đến với góc nhìn công nghệ của Nhóm 2!"},
                        {"start": 3.7, "end": 7.5, "text": "Hôm nay tụi mình khám phá Tốc độ và Vận tốc qua flycam và GPS!"}
                    ]
                },
                {
                    "scene_idx": 2,
                    "scene_id": "V6_S02",
                    "title": "Drone bám đuổi xe đạp đua: Tốc kế GPS",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic high-angle drone tracking shot of a cyclist in aerodynamic cycling gear riding a sleek modern road bike along a scenic coastal asphalt road beside turquoise ocean waters. Expansive road and ocean space for holographic GPS telemetry graphics. 16:9, 8k, photorealistic, no text, no telemetry pre-rendered.",
                    "flow_i2v_prompt": "Smooth aerial drone tracking moving forward alongside the cyclist. Wheels spin, sea breeze ruffles jersey, smooth cinematic flight motion. Ideal for overlaying futuristic GPS HUD overlays.",
                    "hud_type": "speed_gauge",
                    "hud_data": {
                        "device": "GPS TELEMETRY ONBOARD",
                        "speed": "v_gps = 42,5 km/h",
                        "cadence": "Cadence: 90 rpm",
                        "sampling": "Tần số lấy mẫu: 10 Hz (0,1 s / lần)",
                        "formula": "v_instant = Δs / Δt"
                    },
                    "speaker": "Hoàng Nam",
                    "voiceover_text": "Quan sát từ flycam: Chiếc xe đạp gắn đồng hồ GPS liên tục tính toán tốc độ tức thời 42,5 km/h bằng cách đo quãng đường siêu nhỏ chia cho từng 0,1 giây.",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Đồng hồ GPS trên xe đạp liên tục đo tốc độ tức thời 42,5 km/h"},
                        {"start": 3.7, "end": 7.5, "text": "bằng cách chia quãng đường siêu nhỏ cho từng 0,1 giây!"}
                    ]
                },
                {
                    "scene_idx": 3,
                    "scene_id": "V6_S03",
                    "title": "Xe đạp ôm cua: Tốc độ giữ nguyên nhưng Vận tốc đổi!",
                    "duration_sec": 8.0,
                    "keyframe_prompt": "High-angle view of an asphalt mountain road curving in a graceful S-curve bend. The cyclist leans smoothly into the curve. Vast clean road surface for vector trajectory arrows. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "Cinematic drone shot tracking the bicycle carving through the curve at steady pace. Realistic leaning physics, smooth camera path.",
                    "hud_type": "animated_vector_road",
                    "hud_data": {
                        "curve_status": "XE ĐẠP ĐANG ÔM CUA TRÒN",
                        "speed_value": "Tốc độ: v = 30 km/h (KHÔNG ĐỔI)",
                        "vector_direction": "Hướng vectơ tiếp tuyến: ĐỔI LIÊN TỤC",
                        "conclusion": "VẬN TỐC THAY ĐỔI vì hướng thay đổi, dù tốc độ giữ nguyên!"
                    },
                    "speaker": "Hoàng Nam",
                    "voiceover_text": "Điểm thú vị là: Khi xe đạp ôm cua với tốc độ đều 30 km/h, tốc độ của xe không đổi, nhưng vận tốc lại liên tục thay đổi! Vì sao? Vì hướng vectơ vận tốc đã bị đổi!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.8, "text": "Khi xe đạp ôm cua với tốc độ không đổi 30 km/h,"},
                        {"start": 3.8, "end": 8.0, "text": "tốc độ giữ nguyên nhưng vận tốc thay đổi vì hướng liên tục đổi!"}
                    ]
                },
                {
                    "scene_idx": 4,
                    "scene_id": "V6_S04",
                    "title": "Băng chuyền sân bay: Vận tốc âm vs dương",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic interior shot of a brightly lit modern airport terminal concourse with a long flat moving walkway belt and polished floors. Soft ambient indoor lighting, clean negative space across upper ceiling and walkway for directional coordinate vectors. 16:9, 8k, photorealistic, no signage text, no airport logos.",
                    "flow_i2v_prompt": "Smooth slow tracking shot alongside the moving walkway gliding steadily. Reflections on polished airport floor, smooth mechanical motion.",
                    "hud_type": "animated_axes",
                    "hud_data": {
                        "axis": "Trục Ox theo hướng băng chuyền (+)",
                        "person_forward": "Người đi xuôi chiều: v1 = +1,5 m/s (dương)",
                        "person_backward": "Người quay đầu đi ngược: v2 = -0,5 m/s (âm)",
                        "speed_note": "Tốc độ cả hai người đều là số dương!"
                    },
                    "speaker": "Hoàng Nam",
                    "voiceover_text": "Trên băng chuyền sân bay: Chọn chiều dương là chiều băng chuyền chạy, người đi xuôi có vận tốc dương, người đi ngược có vận tốc âm, nhưng tốc độ của họ thì luôn dương!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Trên băng chuyền sân bay: người đi xuôi có vận tốc dương (+),"},
                        {"start": 3.7, "end": 7.5, "text": "người đi ngược có vận tốc âm (-), nhưng tốc độ thì luôn dương!"}
                    ]
                },
                {
                    "scene_idx": 5,
                    "scene_id": "V6_S05",
                    "title": "Câu hỏi tương tác công nghệ & Kết thúc Video 6",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Medium shot of the tech-savvy Vietnamese male student in grey jacket, holding a sleek digital tablet, looking up at the camera with an engaging smile. Innovation lab backdrop with soft bokeh. 16:9, 8k, photorealistic, no text on tablet.",
                    "flow_i2v_prompt": "The student taps the tablet screen lightly, looks into the lens, smiles and asks the interactive question with inviting tone.",
                    "hud_type": "quiz_popup",
                    "hud_data": {
                        "question": "Một flycam bay vòng tròn đều với tốc độ 10 m/s. Vận tốc của nó có đổi không?",
                        "options": [
                            "A. Không đổi vì tốc độ đều 10 m/s",
                            "B. Có đổi vì hướng chuyển động liên tục thay đổi",
                            "C. Vận tốc luôn bằng 0"
                        ],
                        "correct_answer": "B",
                        "explanation": "Vận tốc là vectơ, chỉ cần đổi hướng là vận tốc đã thay đổi."
                    },
                    "speaker": "Hoàng Nam",
                    "voiceover_text": "Câu hỏi nhanh cho các bạn: Khi flycam bay một vòng tròn đều với tốc độ 10 m/s, vận tốc của nó có thay đổi không? Đáp án là có, vì hướng bay liên tục đổi! Đón xem Video 7 nhé!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Flycam bay vòng tròn đều tốc độ 10 m/s, vận tốc có đổi không?"},
                        {"start": 3.7, "end": 7.5, "text": "Có thay đổi vì hướng liên tục đổi! Đón xem Video 7 cùng Nhóm 2 nhé!"}
                    ]
                }
            ]
        },

        # =========================================================================
        # VIDEO 7: BÀI 5 - NHÓM 2 - PHẦN 2
        # =========================================================================
        {
            "video_id": "V7_B5_Nhom2_TongHop_VanToc",
            "title": "Bài 5 (Nhóm 2 - Phần 2): Tổng hợp Vận tốc (Hàng không & Kayak)",
            "lesson": "Bài 5: Tốc độ và vận tốc",
            "part": 2,
            "group_assignment": "Nhóm 2 (Hoàng Nam, Cẩm Nhung, Bảo Yến)",
            "idea_theme": "Máy bay xuôi gió và ngược gió bão, gió thổi tạt ngang, thuyền kayak vượt sóng thác",
            "mc_character": {
                "name": "Cẩm Nhung",
                "gender": "female",
                "age": 16,
                "role": "Lead Presenter (Nhóm 2) - Charismatic, elegant Vietnamese female student",
                "appearance_prompt_en": "A 16-year-old Vietnamese female high school student with shoulder-length soft wavy black hair, radiant smart smile, wearing a stylish pastel-mint green cardigan over a white collared blouse. Articulate, charming and enthusiastic presenter style."
            },
            "clip_count": 5,
            "total_estimated_duration_sec": 38.0,
            "scenes": [
                {
                    "scene_idx": 1,
                    "scene_id": "V7_S01",
                    "title": "Mở đầu & Tiêu đề Bài 5 Nhóm 2 (Phần 2)",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic medium shot of a 16-year-old Vietnamese female high school student with shoulder-length soft wavy hair and a radiant smart smile, wearing a stylish pastel-mint green cardigan over a white blouse. She stands on the left of an aerodynamics and flight science gallery with sleek scale aircraft models blurred behind. Right 65% is clean open space. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The female presenter smiles warmly, waves gently in greeting, and speaks with clear expressive voice, gesturing toward the right negative space. Crisp lighting, 4k.",
                    "hud_type": "title_banner",
                    "hud_data": {
                        "banner_title": "BÀI 5: TỔNG HỢP VẬN TỐC (HÀNG KHÔNG & SÓNG NƯỚC)",
                        "badge": "NHÓM 2 - VẬT LÍ 10",
                        "subtitle": "Phần 2: Ứng dụng Khí động học, Máy bay & Thuyền Kayak",
                        "presenters": "Nhóm 2: Cẩm Nhung • Hoàng Nam • Bảo Yến",
                        "theme_color": "cyan_glow"
                    },
                    "speaker": "Cẩm Nhung",
                    "voiceover_text": "Chào các bạn! Trong phần cuối này, Nhóm 2 sẽ đưa các bạn bay lên bầu trời và lướt sóng để xem các phi công và vận động viên kayak ứng dụng công thức cộng vận tốc ra sao nhé!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Chào các bạn! Trong phần cuối này, Nhóm 2 sẽ đưa các bạn"},
                        {"start": 3.7, "end": 7.5, "text": "khám phá công thức cộng vận tốc trên máy bay và thuyền kayak!"}
                    ]
                },
                {
                    "scene_idx": 2,
                    "scene_id": "V7_S02",
                    "title": "Máy bay xuôi gió & ngược gió bão",
                    "duration_sec": 8.0,
                    "keyframe_prompt": "Cinematic aerial shot of a modern passenger jet airliner cruising steadily at high altitude above a vast field of sunlit white cumulus clouds under a deep blue sky. Ample sky space around the aircraft for wind vectors and speed telemetry. 16:9, 8k, photorealistic, no airline logos, no letters.",
                    "flow_i2v_prompt": "Slow majestic aerial tracking of the airplane cruising through the sky. Subtle wing condensation, clouds drift slowly below. Stable cinematic composition.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "system": "HỆ THỐNG: (1) Máy bay • (2) Không khí • (3) Mặt đất",
                        "tailwind": "Xuôi gió: v_1,3 = v_maybay + v_gio = 800 + 100 = 900 km/h (Bay nhanh hơn)",
                        "headwind": "Ngược gió: v_1,3 = v_maybay - v_gio = 800 - 100 = 700 km/h (Bay chậm hơn)"
                    },
                    "speaker": "Cẩm Nhung",
                    "voiceover_text": "Khi máy bay bay ở độ cao 10.000 mét, gió xuôi chiều 100 km/h sẽ cộng dồn giúp máy bay đạt vận tốc 900 km/h đối với mặt đất, tiết kiệm cả giờ bay và nhiên liệu!",
                    "subtitles": [
                        {"start": 0.0, "end": 4.0, "text": "Khi bay gặp gió xuôi chiều 100 km/h, vận tốc cộng dồn đạt 900 km/h,"},
                        {"start": 4.0, "end": 8.0, "text": "giúp máy bay tiết kiệm cả giờ bay và hàng ngàn lít nhiên liệu!"}
                    ]
                },
                {
                    "scene_idx": 3,
                    "scene_id": "V7_S03",
                    "title": "Gió thổi tạt ngang: Tam giác vectơ hướng bay",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "High-angle aerial shot from behind a modern aircraft flying through high-altitude misty skies. Vast open sky and misty cloudscape for overlaying vector triangle diagrams. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "Gentle cinematic tracking behind the aircraft. The plane banks subtly to compensate for wind drift. Smooth photorealistic atmospheric flight.",
                    "hud_type": "animated_vector_road",
                    "hud_data": {
                        "vector_v12": "v12: Hướng mũi máy bay",
                        "vector_v23": "v23: Gió thổi tạt ngang vuông góc",
                        "vector_v13": "v13: Đường bay thực tế nối đến sân bay",
                        "action": "Phi công phải bẻ mũi máy bay nghiêng góc θ để bù gió trôi!"
                    },
                    "speaker": "Cẩm Nhung",
                    "voiceover_text": "Còn khi gió thổi tạt ngang vuông góc đường bay, vận tốc thực tế bị trôi chéo theo tam giác vuông. Các phi công buộc phải bẻ mũi máy bay nghiêng một góc để bù gió!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Khi gió thổi tạt ngang, vận tốc thực tế bị trôi chéo."},
                        {"start": 3.7, "end": 7.5, "text": "Phi công phải bẻ mũi máy bay nghiêng một góc để bù gió trôi!"}
                    ]
                },
                {
                    "scene_idx": 4,
                    "scene_id": "V7_S04",
                    "title": "Thuyền Kayak chèo trên sông: 3 Trường hợp tổng kết",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Cinematic aerial drone shot of an athletic person paddling a sleek modern kayak on an emerald river winding through a lush pine forest canyon. Pristine clear water ripples, clean surface for vector annotations. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "Smooth aerial drone tracking moving alongside the kayak as the paddle strokes cut through the glistening water. Natural water dynamics, cinematic outdoor light.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "kayak_rule": "3 QUY TẮC CỘNG VẬN TỐC KHI CHÈO THUYỀN",
                        "case_downstream": "Xuôi dòng: v_thực = v_thuyền + v_dòng",
                        "case_upstream": "Ngược dòng: v_thực = |v_thuyền - v_dòng|",
                        "case_across": "Chèo ngang dòng: v_thực = √(v_thuyền² + v_dòng²)"
                    },
                    "speaker": "Cẩm Nhung",
                    "voiceover_text": "Tương tự với thuyền kayak: Chèo xuôi dòng nước đẩy thì nhanh hơn, chèo ngược dòng thì tốn sức hơn, và muốn sang bờ bên kia vuông góc thì phải chèo chếch lên thượng nguồn!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Chèo kayak xuôi dòng thì nhanh hơn, ngược dòng tốn sức hơn,"},
                        {"start": 3.7, "end": 7.5, "text": "muốn sang bờ vuông góc thì phải chèo chếch lên thượng nguồn!"}
                    ]
                },
                {
                    "scene_idx": 5,
                    "scene_id": "V7_S05",
                    "title": "Lời cảm ơn & Tổng kết toàn bộ 7 video của cả 2 Nhóm",
                    "duration_sec": 7.5,
                    "keyframe_prompt": "Medium shot of the Vietnamese female student in mint cardigan, smiling radiantly, hands neatly clasped, giving a warm bow of appreciation to the viewer. Modern exhibition gallery backdrop with soft ambient light. 16:9, 8k, photorealistic, no text.",
                    "flow_i2v_prompt": "The presenter smiles warmly, bows with polite gratitude, and waves cheerfully to conclude the entire series. High quality natural motion.",
                    "hud_type": "hud_boxes",
                    "hud_data": {
                        "title": "HOÀN THÀNH CHUỖI 7 VIDEO VẬT LÍ 10",
                        "summary": "7 Video Hoạt họa Google Flow Hybrid (Full Animation)",
                        "teams": "Nhóm 1 & Nhóm 2 - Bài 4 & Bài 5",
                        "thanks": "Trân trọng cảm ơn quý thầy cô và các bạn đã đồng hành!"
                    },
                    "speaker": "Cẩm Nhung",
                    "voiceover_text": "Đó là toàn bộ bí quyết làm chủ công thức cộng vận tốc! Nhóm 2 xin trân trọng cảm ơn quý thầy cô và các bạn đã lắng nghe và ủng hộ cả chuỗi video Vật lí 10 của tụi mình!",
                    "subtitles": [
                        {"start": 0.0, "end": 3.7, "text": "Đó là bí quyết làm chủ công thức cộng vận tốc!"},
                        {"start": 3.7, "end": 7.5, "text": "Nhóm 2 trân trọng cảm ơn quý thầy cô và các bạn đã đồng hành!"}
                    ]
                }
            ]
        }
    ]
}

out_path = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\master_plan_7videos.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)

print(f"Generated {out_path} successfully!")
print(f"Total videos: {len(plan['videos'])}")
total_clips = sum(v['clip_count'] for v in plan['videos'])
print(f"Total clips: {total_clips}")
print(f"Total credits: {total_clips * 20}")
