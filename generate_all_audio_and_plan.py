import os
import json
import asyncio
import subprocess
import re
import wave
import numpy as np
import edge_tts
import imageio_ffmpeg

WORK_DIR = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid"
PLAN_FILE = os.path.join(WORK_DIR, "master_plan_7videos.json")

# Enhanced voiceovers for all 48 scenes
# Standard pedagogical content for Bài 4 & Bài 5 Physics Grade 10 (KNTT)
VOICEOVERS = {
    # -------------------------------------------------------------
    # VIDEO 1: Bài 4 - Phần 1 (Anh Thư - female - vi-VN-HoaiMyNeural)
    # -------------------------------------------------------------
    "V1_B4_ViTri_HeQuyChieu": {
        1: "Chào mừng thầy cô và các bạn! Hôm nay, nhóm mình xin đồng hành cùng các bạn khám phá Bài 4: Vị trí của vật và Hệ quy chiếu trong môn Vật lí 10.",
        2: "Hãy bắt đầu với một câu hỏi thực tế: Một chiếc ô tô chạy qua ngã tư O với tốc độ đều 36 km trên giờ. Sau đúng 10 giây, xe đi được quãng đường 100 mét.",
        3: "Câu hỏi đặt ra là: Liệu chỉ biết quãng đường 100 mét, chúng mình có thể chỉ ra chính xác ô tô đang ở vị trí nào không? Chắc chắn là chưa thể!",
        4: "Nếu ô tô chỉ chạy thẳng trên một con đường thẳng, ta chỉ cần chọn một vật mốc O và trục Ox trùng với đường đi, vị trí xe sẽ được xác định bởi tọa độ x.",
        5: "Nhưng khi xe có thể rẽ nhiều hướng, ta cần Hệ tọa độ địa lí Oxy: Trục Ox theo hướng Tây, Đông và trục Oy theo hướng Nam, Bắc, gắn chặt với vật mốc.",
        6: "Để mô tả trọn vẹn chuyển động, các bạn nhớ công thức vàng: Hệ quy chiếu bao gồm Hệ tọa độ gắn với vật mốc, kết hợp cùng mốc thời gian và đồng hồ đo.",
        7: "Khi kích thước của vật rất nhỏ so với quãng đường di chuyển, ví dụ chiếc ô tô 4 mét chạy hàng trăm mét, ta hoàn toàn có thể coi nó là một chất điểm!",
        8: "Bây giờ, mời các bạn cùng thử tài với một câu hỏi tương tác thú vị: Trong trường hợp thực tế nào thì một vật chuyển động được coi là một chất điểm? Hãy suy nghĩ thật kỹ nhé!",
        9: "Vậy là chúng ta đã nắm chắc cách xác định vị trí và thiết lập hệ quy chiếu rồi! Hẹn gặp lại thầy cô và các bạn ở Video 2 với khái niệm Độ dịch chuyển nhé!"
    },
    # -------------------------------------------------------------
    # VIDEO 2: Bài 4 - Phần 2 (Hữu Trọng - male - vi-VN-NamMinhNeural)
    # -------------------------------------------------------------
    "V2_B4_DoDichChuyen_QuangDuong": {
        1: "Chào các bạn! Trong phần 2 của Bài 4, nhóm mình sẽ cùng các bạn làm rõ một trong những khái niệm nền tảng dễ nhầm lẫn nhất: Quãng đường và Độ dịch chuyển!",
        2: "Quay lại ví dụ ngã tư ban nãy: Nếu bây giờ mình nói rõ xe chạy 100 mét về hướng Bắc, các bạn sẽ chỉ ra ngay vị trí của xe tại điểm B trên bản đồ!",
        3: "Đại lượng vừa cho biết độ dài, vừa cho biết hướng thay đổi vị trí đó chính là Độ dịch chuyển, ký hiệu là vectơ d có dấu mũi tên trên đầu!",
        4: "Quan sát 3 người cùng đi từ Siêu thị A đến Bưu điện B: Người đi xe máy theo đường vòng, người đi bộ đi đường thẳng xuyên công viên, và người lái ô tô đi đường tránh.",
        5: "Quãng đường s là độ dài thực tế của đường đi. Ba người chọn ba lộ trình khác nhau nên quãng đường của họ chắc chắn khác nhau: s một khác s hai và khác s ba!",
        6: "Thế nhưng độ dịch chuyển d chỉ quan tâm đúng điểm đầu là siêu thị A và điểm cuối là bưu điện B. Vì cùng đi từ A đến B, độ dịch chuyển của cả ba người là như nhau!",
        7: "Bảng so sánh này giúp các bạn nhớ ngay: Quãng đường là đại lượng vô hướng luôn dương và phụ thuộc quỹ đạo; còn độ dịch chuyển là đại lượng vectơ có thể âm, dương hoặc bằng 0!",
        8: "Một quy tắc vàng cần khắc sâu khi làm bài thi: Độ lớn của độ dịch chuyển chỉ bằng quãng đường đi được khi và chỉ khi vật chuyển động thẳng và tuyệt đối không đổi chiều!",
        9: "Thử tài nhanh: Nếu bạn chạy một vòng sân vận động 400 mét rồi về đúng vạch xuất phát, độ dịch chuyển bằng bao nhiêu? Chính là bằng không mét! Hẹn gặp lại các bạn ở Video 3!"
    },
    # -------------------------------------------------------------
    # VIDEO 3: Bài 4 - Phần 3 (Thế Mỹ - male - vi-VN-NamMinhNeural)
    # -------------------------------------------------------------
    "V3_B4_TongHop_DoDichChuyen": {
        1: "Chào mừng thầy cô và các bạn đến với phần 3 của Bài 4! Khi một vật di chuyển qua nhiều chặng liên tiếp, làm sao tính được độ dịch chuyển chung cuộc? Cùng nhóm mình tìm hiểu nhé!",
        2: "Trong Vật lí, nếu vật thực hiện liên tiếp các độ dịch chuyển d một và d hai, thì độ dịch chuyển tổng hợp d được tính bằng quy tắc cộng vectơ: vectơ d bằng vectơ d một cộng vectơ d hai!",
        3: "Hãy xét ví dụ này: Một bạn học sinh đi từ điểm A sang B 4 km về hướng Đông, sau đó rẽ vuông góc từ B lên C 4 km về hướng Bắc.",
        4: "Về quãng đường, bạn ấy đã bước đi thực tế 4 km đoạn đầu rồi thêm 4 km đoạn sau, tổng cộng quãng đường s bằng 8 km. Quá trực quan và đơn giản phải không nào?",
        5: "Nhưng độ dịch chuyển tổng hợp lại là đường chéo nối thẳng từ A đến C. Vì hai chặng vuông góc, ta dùng định lý Pitago: d bằng căn của 4 bình cộng 4 bình, ra khoảng 5,7 km theo hướng Đông Bắc!",
        6: "Rõ ràng quãng đường 8 km lớn hơn hẳn độ lớn độ dịch chuyển 5,7 km. Một lần nữa chứng minh: cứ đổi hướng là độ dịch chuyển sẽ nhỏ hơn quãng đường!",
        7: "Để giải nhanh mọi bài tập tổng hợp: hai độ dịch chuyển cùng chiều thì cộng, ngược chiều thì lấy hiệu trị tuyệt đối, còn vuông góc nhau thì áp dụng ngay định lý Pitago!",
        8: "Câu hỏi nhanh cho các bạn: Nếu d một bằng 3 mét và d hai bằng 4 mét vuông góc nhau, độ dịch chuyển tổng hợp là bao nhiêu? Rất nhanh, chính là 5 mét!",
        9: "Như vậy nhóm mình đã đồng hành trọn vẹn cùng các bạn qua 3 phần của Bài 4. Cảm ơn thầy cô và các bạn đã chú ý lắng nghe bài thuyết trình của nhóm mình!"
    },
    # -------------------------------------------------------------
    # VIDEO 4: Bài 5 - Phần 1 (Tú Châu - female - vi-VN-HoaiMyNeural)
    # -------------------------------------------------------------
    "V4_B5_Nhom1_TocDo_VanToc": {
        1: "Chào mừng thầy cô và các bạn! Nhóm 1 xin đồng hành cùng cả lớp khám phá Bài 5: Tốc độ và Vận tốc. Trong đời sống chúng ta hay dùng lẫn lộn, nhưng trong Vật lí 10, đây là hai đại lượng mang bản chất khoa học hoàn toàn khác nhau đấy!",
        2: "Hãy quan sát vận động viên điền kinh bứt tốc trên đường chạy 100 mét hết đúng 9,98 giây. Để biết mức độ nhanh chậm trung bình trên cả chặng đua, ta lấy quãng đường chia thời gian: v bằng s chia t, đạt con số ấn tượng xấp xỉ 10 mét trên giây!",
        3: "Còn khi chúng mình ngồi trên xe máy, con số nhảy liên tục trên đồng hồ tốc kế chính là Tốc độ tức thời. Nó cho biết chính xác độ nhanh chậm tại đúng thời điểm quan sát, giúp người lái xe kiểm soát an toàn giao thông trên từng mét đường.",
        4: "Tuy nhiên, tốc độ thuần túy không cho biết vật đang lao về hướng nào. Vì thế, các nhà vật lí xây dựng khái niệm Vận tốc: Vận tốc trung bình bằng độ dịch chuyển d chia cho khoảng thời gian t, là đại lượng vectơ chỉ rõ phương chiều chuyển động!",
        5: "Nhìn vào bảng so sánh: Tốc độ bằng quãng đường chia thời gian, là đại lượng vô hướng luôn dương. Trong khi đó, vận tốc bằng độ dịch chuyển chia thời gian, là đại lượng vectơ có thể mang giá trị âm, dương hoặc bằng 0 tùy thuộc chiều dương đã chọn!",
        6: "Khắc sâu quy tắc vàng: Khi vật chuyển động thẳng và không đổi chiều, độ lớn của vận tốc mới bằng tốc độ! Cảm ơn thầy cô và các bạn, hãy đón xem tiếp Video 5 để cùng nhóm mình khám phá bí quyết cộng vận tốc nhé!"
    },
    # -------------------------------------------------------------
    # VIDEO 5: Bài 5 - Phần 2 (Minh Dũng - male - vi-VN-NamMinhNeural)
    # -------------------------------------------------------------
    "V5_B5_Nhom1_TongHop_VanToc": {
        1: "Chào các bạn! Đã bao giờ bạn tự hỏi: Khi mình bước đi thong thả trên một toa tàu đang chạy hết tốc lực, thì vận tốc thực sự của mình đối với người đứng yên bên đường là bao nhiêu chưa? Nhóm 1 sẽ giải đáp ngay sau đây!",
        2: "Để không bao giờ nhầm lẫn, nhóm mình chia sẻ mẹo đánh số thứ tự cực chuẩn: Số 1 là vật chuyển động như người đi bộ, số 2 là hệ quy chiếu chuyển động gắn với toa tàu, và số 3 là hệ quy chiếu đứng yên gắn với mặt đất.",
        3: "Công thức cộng vận tốc tổng quát phát biểu: vectơ v một ba bằng vectơ v một hai cộng vectơ v hai ba! Khi bạn đi cùng chiều tàu chạy thì vận tốc cộng dồn v một ba bằng v một hai cộng v hai ba; còn nếu đi ngược chiều lại thì ta lấy hiệu trừ bớt đi!",
        4: "Đặc biệt khi ca nô vượt sông có dòng nước chảy xiết: mũi thuyền hướng vuông góc bờ nhưng bị nước đẩy ngang. Ta ghép hai vectơ thành tam giác vuông và dùng định lý Pitago: vận tốc thực tế v một ba bằng căn bậc hai của v một hai bình phương cộng v hai ba bình phương!",
        5: "Chỉ cần nắm vững quy ước đánh số 1, 2, 3 và kết hợp quy tắc hình học vectơ, mọi bài toán cộng vận tốc đều trở nên vô cùng dễ dàng! Nhóm 1 xin chân thành cảm ơn quý thầy cô và các bạn đã chú ý lắng nghe bài thuyết trình!"
    },
    # -------------------------------------------------------------
    # VIDEO 6: Bài 5 - Góc nhìn Công nghệ (Hoàng Nam - male - vi-VN-NamMinhNeural)
    # -------------------------------------------------------------
    "V6_B5_Nhom2_TocDo_VanToc": {
        1: "Chào mừng thầy cô và các bạn đến với góc nhìn công nghệ hiện đại của Nhóm 2! Hôm nay tụi mình sẽ giúp các bạn giải mã bản chất của Tốc độ và Vận tốc thông qua thiết bị định vị vệ tinh GPS và thiết bị bay flycam thông minh!",
        2: "Quan sát từ ống kính flycam: Chiếc xe đạp gắn chíp cảm biến GPS đo quãng đường cực nhỏ sau mỗi một phần mười giây để cập nhật tức thời tốc độ 42,5 km trên giờ hiển thị sắc nét lên màn hình điều khiển theo thời gian thực.",
        3: "Một phát hiện vật lí cực kỳ thú vị: Khi tay đua xe đạp ôm cua tròn với tốc độ đều 30 km trên giờ, độ lớn tốc độ không hề đổi, nhưng vận tốc lại liên tục thay đổi! Vì sao? Vì hướng của vectơ vận tốc đã liên tục đổi hướng!",
        4: "Tại băng chuyền hành lý sân bay: Chọn chiều dương là chiều băng chuyền chuyển động, hành khách đi xuôi chiều sẽ có vận tốc mang dấu dương, người đi ngược chiều có vận tốc mang dấu âm, nhưng tốc độ của cả hai thì luôn là số dương!",
        5: "Thử tài nhanh cùng Nhóm 2: Khi chiếc flycam bay lượn tròn đều với tốc độ không đổi 10 mét trên giây, vectơ vận tốc của nó có thay đổi không? Đáp án là có, vì hướng bay đổi liên tục! Hẹn gặp lại các bạn ở Video 7 nhé!"
    },
    # -------------------------------------------------------------
    # VIDEO 7: Bài 5 - Ứng dụng Hàng không & Kayak (Cẩm Nhung - female - vi-VN-HoaiMyNeural)
    # -------------------------------------------------------------
    "V7_B5_Nhom2_TongHop_VanToc": {
        1: "Chào các bạn! Trong phần kết của chuỗi video, Nhóm 2 sẽ đưa các bạn bay lượn trên bầu trời cao và lướt sóng trên sông lớn để khám phá cách các phi công hàng không và tay chèo kayak làm chủ công thức cộng vận tốc!",
        2: "Khi máy bay chở khách bay ở tầng bình lưu độ cao 10 nghìn mét, luồng gió xuôi chiều 100 km trên giờ cùng hướng bay sẽ cộng dồn trực tiếp, giúp phi cơ đạt vận tốc thực tế 900 km trên giờ so với mặt đất, tiết kiệm hàng tấn nhiên liệu quý giá!",
        3: "Nhưng khi gặp gió thổi ngang vuông góc thân máy bay, vectơ vận tốc thực tế bị trôi dạt theo hướng chéo. Các phi công buộc phải dùng định lý Pitago và tính toán góc lệch để bẻ mũi phi cơ ngược lại, giữ đường bay an toàn tuyệt đối!",
        4: "Trên sông nước, tay chèo kayak cũng áp dụng nguyên lí này: Chèo xuôi dòng thì nước đẩy nhanh hơn, chèo ngược dòng thì triệt tiêu sức thuyền, và muốn sang đúng bờ đối diện phải chèo chếch hướng lên thượng nguồn để bù dòng nước chảy!",
        5: "Đó chính là vẻ đẹp thực tiễn của công thức cộng vận tốc trong thế giới hiện đại! Nhóm 2 xin trân trọng gửi lời cảm ơn sâu sắc tới quý thầy cô và các bạn đã đồng hành, theo dõi trọn vẹn cả 7 video Vật lí 10 của chúng mình!"
    }
}

VOICE_MAP = {
    "female": "vi-VN-HoaiMyNeural",
    "male": "vi-VN-NamMinhNeural"
}

def sanitize_for_tts(text):
    t = text
    t = t.replace(":", ", ")
    t = t.replace(";", ", ")
    t = t.replace("&", " và ")
    t = t.replace("/", " trên ")
    t = t.replace("–", ", ")
    t = t.replace("—", ", ")
    t = t.replace("-", ", ")
    t = t.replace('"', "")
    t = t.replace("'", "")
    t = t.replace("(", ", ")
    t = t.replace(")", ", ")
    t = t.replace("+", " cộng ")
    t = t.replace("=", " bằng ")
    t = t.replace("km/h", "km trên giờ")
    t = t.replace("m/s", "mét trên giây")
    t = t.replace("Oxy", "Ô-x-y")
    t = t.replace("Ox", "Ô-x")
    t = t.replace("Oy", "Ô-y")
    t = t.replace("v13", "v một ba")
    t = t.replace("v12", "v một hai")
    t = t.replace("v23", "v hai ba")
    t = t.replace("d1", "d một")
    t = t.replace("d2", "d hai")
    t = t.replace("s1", "s một")
    t = t.replace("s2", "s hai")
    t = t.replace("s3", "s ba")
    t = t.replace("10.000", "10 nghìn")
    t = t.replace("1-2-3", "1, 2, 3")
    t = re.sub(r",\s*,+", ",", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def split_subtitles(text, duration):
    raw_parts = re.split(r'([.?!;:]|\s+—\s+)', text)
    merged = []
    i = 0
    while i < len(raw_parts):
        part = raw_parts[i].strip()
        if i + 1 < len(raw_parts) and raw_parts[i+1].strip() in ['.', '?', '!', ';', ':', '—']:
            part += raw_parts[i+1].strip()
            i += 2
        else:
            i += 1
        if part:
            merged.append(part)
            
    chunks = []
    for m in merged:
        words = m.split()
        if len(words) <= 8:
            chunks.append(m)
        elif ',' in m:
            sub = [s.strip() for s in m.split(',') if s.strip()]
            cur = []
            for s_idx, sp in enumerate(sub):
                w = sp.split()
                if s_idx < len(sub) - 1:
                    w[-1] += ','
                if len(cur) + len(w) <= 8:
                    cur.extend(w)
                else:
                    if cur:
                        chunks.append(" ".join(cur))
                        cur = []
                    if len(w) > 8:
                        for k in range(0, len(w), 6):
                            chunks.append(" ".join(w[k:k+6]))
                    else:
                        cur.extend(w)
            if cur:
                chunks.append(" ".join(cur))
        else:
            for k in range(0, len(words), 7):
                chunks.append(" ".join(words[k:k+7]))
                
    chunks = [c.strip() for c in chunks if c.strip()]
    if not chunks:
        chunks = [text]
        
    total_len = sum(len(c) for c in chunks)
    timed_subtitles = []
    current_time = 0.0
    for idx, c in enumerate(chunks):
        seg_duration = (len(c) / total_len) * duration
        seg_end = min(current_time + seg_duration, duration)
        if idx == len(chunks) - 1:
            seg_end = duration
        timed_subtitles.append({
            "start": round(current_time, 2),
            "end": round(seg_end, 2),
            "text": c
        })
        current_time = seg_end
        
    return chunks, timed_subtitles

def get_audio_duration(file_path):
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ffmpeg_exe, "-i", file_path]
    proc = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors="ignore")
    for line in proc.stderr.splitlines():
        if "Duration:" in line:
            m = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", line)
            if m:
                hours, minutes, seconds = m.groups()
                return round(int(hours) * 3600 + int(minutes) * 60 + float(seconds), 2)
    return 10.0

async def generate_single_audio(text, voice, out_path, max_retries=6):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 5000:
        return True
        
    clean_text = sanitize_for_tts(text)
    for attempt in range(max_retries):
        try:
            comm = edge_tts.Communicate(clean_text, voice)
            await comm.save(out_path)
            return True
        except Exception as e:
            if attempt == max_retries - 1:
                print(f"Error generating audio for '{text[:30]}...': {e}")
                raise e
            print(f"  [Retry {attempt+1}/{max_retries}] Waiting {2.0 * (attempt + 1)}s...")
            await asyncio.sleep(2.0 * (attempt + 1))
    return False

def generate_bg_music(out_path, duration=120.0):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000000:
        cur_dur = get_audio_duration(out_path)
        if cur_dur >= 115.0:
            print(f"BGM already exists and valid ({cur_dur}s): {out_path}")
            return

    print(f"Generating smooth lofi background music ({duration}s)...")
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    chord_cycle = [
        [261.63, 329.63, 392.00, 493.88], # Cmaj7
        [220.00, 261.63, 329.63, 392.00], # Am7
        [174.61, 220.00, 261.63, 329.63], # Fmaj7
        [196.00, 246.94, 293.66, 392.00]  # G
    ]
    chord_duration = 4.0
    total_chords = int(duration / chord_duration) + 1
    audio_signal = np.zeros_like(t)

    for i in range(total_chords):
        start_t = i * chord_duration
        end_t = min((i + 1) * chord_duration, duration)
        mask = (t >= start_t) & (t < end_t)
        sub_t = t[mask] - start_t
        
        chord = chord_cycle[i % len(chord_cycle)]
        chord_sig = np.zeros_like(sub_t)
        for f in chord:
            sine = 0.7 * np.sin(2 * np.pi * f * sub_t) + 0.3 * np.sin(2 * np.pi * f * 2 * sub_t)
            chord_sig += sine
            
        attack = np.minimum(sub_t / 0.5, 1.0)
        decay = np.maximum(1.0 - (sub_t / chord_duration)**2 * 0.3, 0.2)
        env = attack * decay
        chord_sig *= env
        audio_signal[mask] += chord_sig

    bass_cycle = [130.81, 110.00, 87.31, 98.00]
    for i in range(total_chords):
        start_t = i * chord_duration
        end_t = min((i + 1) * chord_duration, duration)
        mask = (t >= start_t) & (t < end_t)
        sub_t = t[mask] - start_t
        f_bass = bass_cycle[i % len(bass_cycle)]
        bass_sig = 0.8 * np.sin(2 * np.pi * f_bass * sub_t)
        audio_signal[mask] += bass_sig

    audio_signal = audio_signal / np.max(np.abs(audio_signal)) * 0.10

    fade_in_len = int(sample_rate * 2.0)
    audio_signal[:fade_in_len] *= np.linspace(0, 1, fade_in_len)
    fade_out_len = int(sample_rate * 3.0)
    audio_signal[-fade_out_len:] *= np.linspace(1, 0, fade_out_len)

    int_signal = (audio_signal * 32767).astype(np.int16)
    
    with wave.open(out_path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(int_signal.tobytes())
        
    print(f"BGM generated successfully: {out_path}")

async def main():
    print("=== STEP 1 & 2: Process TTS and Update Master Plan ===")
    with open(PLAN_FILE, "r", encoding="utf-8") as f:
        plan = json.load(f)

    # 1. Generate 120s BGM
    bgm_path = os.path.join(WORK_DIR, "bg_music.wav")
    generate_bg_music(bgm_path, 120.0)

    total_scenes_processed = 0
    video_summaries = []

    for v in plan["videos"]:
        vid = v["video_id"]
        mc = v.get("mc_character", {})
        gender = mc.get("gender", "male")
        voice = VOICE_MAP.get(gender, "vi-VN-NamMinhNeural")
        v["voice_actor"] = voice
        mc["voice_name"] = voice
        
        print(f"\nProcessing Video: {vid} | MC: {mc.get('name')} ({gender}) | Voice: {voice}")
        scenes = v["scenes"]
        total_video_duration = 0.0

        for s in scenes:
            s_idx = s["scene_idx"]
            
            if vid in VOICEOVERS and s_idx in VOICEOVERS[vid]:
                vo_text = VOICEOVERS[vid][s_idx]
            else:
                vo_text = s.get("voiceover_text", "")
                
            s["voiceover_text"] = vo_text
            
            # Destination path: kits/<video_id>/audio/s<N>.mp3
            audio_dir = os.path.join(WORK_DIR, "kits", vid, "audio")
            os.makedirs(audio_dir, exist_ok=True)
            mp3_path = os.path.join(audio_dir, f"s{s_idx}.mp3")
            
            if not os.path.exists(mp3_path) or os.path.getsize(mp3_path) < 5000:
                print(f"  -> Generating TTS for Scene {s_idx}...")
                await generate_single_audio(vo_text, voice, mp3_path)
                await asyncio.sleep(0.5) # Gentle spacing
            else:
                print(f"  -> Scene {s_idx} audio already exists.")
            
            # Measure actual duration
            dur = get_audio_duration(mp3_path)
            s["audio_duration"] = dur
            s["duration_sec"] = dur
            total_video_duration += dur
            
            # Sync subtitle chunks and timed subtitles
            chunks, timed_subs = split_subtitles(vo_text, dur)
            s["subtitle_chunks"] = chunks
            s["subtitles"] = timed_subs
            
            total_scenes_processed += 1
            print(f"     [OK] s{s_idx}.mp3 ({dur}s, {len(chunks)} subtitle chunks)")

        total_video_duration = round(total_video_duration, 2)
        v["actual_duration_sec"] = total_video_duration
        v["estimated_duration"] = f"{int(total_video_duration // 60)}m {int(total_video_duration % 60)}s"
        print(f"==> Total duration for {vid}: {total_video_duration}s ({v['estimated_duration']})")
        
        video_summaries.append({
            "video_id": vid,
            "title": v["title"],
            "mc": f"{mc.get('name')} ({gender})",
            "voice": voice,
            "scenes": len(scenes),
            "actual_duration_sec": total_video_duration,
            "formatted_duration": v["estimated_duration"]
        })

    # Save updated plan
    with open(PLAN_FILE, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)
    print(f"\n[SUCCESS] master_plan_7videos.json updated successfully with all 48 scenes!")

    # Summary
    print("\n================ FINAL TTS & DURATION SUMMARY ================")
    print(f"Total audio files generated: {total_scenes_processed}/48")
    for vs in video_summaries:
        print(f"• {vs['video_id']}: {vs['scenes']} clips | {vs['actual_duration_sec']}s ({vs['formatted_duration']}) | {vs['mc']} [{vs['voice']}]")

if __name__ == "__main__":
    asyncio.run(main())
