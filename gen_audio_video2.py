import os
import sys
import time
import subprocess
import imageio_ffmpeg
from gtts import gTTS

sys.stdout.reconfigure(encoding="utf-8")
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

WORK_DIR = r"c:\Users\huy83\Downloads\AIvid"
AUDIO_DIR = os.path.join(WORK_DIR, "audio_video2")
os.makedirs(AUDIO_DIR, exist_ok=True)

segments = [
    {
        "id": "v2_s1",
        "speaker": "Anh Thư",
        "voice": "vi-VN-HoaiMyNeural",
        "text": "Quay lại ngã tư ban nãy, nếu mình nói rõ là: xe chạy 100 mét về hướng Bắc, các bạn sẽ chỉ ra ngay xe đang ở điểm B. Đại lượng vừa cho biết độ dài, vừa cho biết hướng thay đổi vị trí đó chính là Độ dịch chuyển! Độ dịch chuyển là một đại lượng vectơ, ký hiệu là d có mũi tên trên đầu, vẽ bằng một mũi tên nối từ điểm xuất phát đến điểm kết thúc."
    },
    {
        "id": "v2_s2",
        "speaker": "Hữu Trọng",
        "voice": "vi-VN-HoaiMyNeural",
        "text": "Hai khái niệm Quãng đường và Độ dịch chuyển rất dễ nhầm lẫn, các bạn chú ý nhé. Nhìn vào sơ đồ, có ba người cùng đi từ siêu thị A đến bưu điện B: người đi xe máy theo đường cong thứ nhất, người đi bộ theo đường thẳng thứ hai, và người đi ô tô theo cung đường uốn lượn thứ ba."
    },
    {
        "id": "v2_s3",
        "speaker": "Anh Thư",
        "voice": "vi-VN-HoaiMyNeural",
        "text": "Vì đi theo ba con đường khác nhau, nên Quãng đường s của họ chắc chắn khác nhau: s1 khác s2 và khác s3. Thế nhưng Độ dịch chuyển d lại chỉ quan tâm điểm đầu là siêu thị A và điểm cuối là bưu điện B. Vì cùng xuất phát từ A và cùng đến B, nên độ dịch chuyển của cả ba người là hoàn toàn như nhau!"
    },
    {
        "id": "v2_s4",
        "speaker": "Hữu Trọng",
        "voice": "vi-VN-HoaiMyNeural",
        "text": "Một quy tắc cốt lõi mà tụi mình rút ra: Chỉ khi vật chuyển động thẳng và tuyệt đối không quay đầu đổi chiều thì độ lớn độ dịch chuyển mới bằng quãng đường: trị tuyệt đối của d bằng s. Còn nếu vật đi đường cong hoặc quay đầu ngược lại, độ lớn độ dịch chuyển sẽ luôn nhỏ hơn quãng đường!"
    },
    {
        "id": "v2_s5",
        "speaker": "Thế Mỹ & Nhóm 1",
        "voice": "vi-VN-HoaiMyNeural",
        "text": "Câu hỏi tương tác ghi nhớ cho cả lớp: Khi nào độ lớn độ dịch chuyển bằng đúng quãng đường đi được? Đó chính là khi vật chuyển động thẳng và không đổi chiều! Cảm ơn thầy cô và các bạn đã chú ý theo dõi bài thuyết trình của nhóm mình!"
    }
]

def get_audio_duration(path):
    res = subprocess.run([ffmpeg_exe, "-i", path], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    for line in res.stderr.split("\n"):
        if "Duration:" in line:
            t_str = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = t_str.split(":")
            return float(h)*3600 + float(m)*60 + float(s)
    return 10.0

concat_lines = []
for sc in segments:
    txt_file = os.path.join(AUDIO_DIR, f"{sc['id']}.txt")
    mp3_file = os.path.join(AUDIO_DIR, f"{sc['id']}.mp3")
    
    # Check if valid file already exists
    if not (os.path.exists(mp3_file) and os.path.getsize(mp3_file) > 5000):
        if os.path.exists(mp3_file):
            try: os.remove(mp3_file)
            except: pass
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(sc["text"])
        
        # Try edge_tts first
        success = False
        try:
            res = subprocess.run([
                sys.executable, "-m", "edge_tts",
                "--voice", sc["voice"],
                "-f", txt_file,
                "--write-media", mp3_file
            ], timeout=15)
            if res.returncode == 0 and os.path.exists(mp3_file) and os.path.getsize(mp3_file) > 5000:
                success = True
        except:
            pass
            
        # Fallback to gTTS if edge-tts fails
        if not success:
            print(f"Fallback to gTTS for {sc['id']}...")
            tts = gTTS(text=sc["text"], lang="vi", slow=False)
            tts.save(mp3_file)
            
    dur = get_audio_duration(mp3_file)
    sc["duration"] = dur
    concat_lines.append(f"file '{mp3_file.replace(chr(92), '/')}'")
    print(f"Audio {sc['id']} ready ({sc['speaker']}): {dur:.2f}s")

concat_file = os.path.join(AUDIO_DIR, "concat_video2.txt")
with open(concat_file, "w", encoding="utf-8") as f:
    f.write("\n".join(concat_lines) + "\n")

out_voice = os.path.join(AUDIO_DIR, "voice_video2.mp3")
subprocess.run([
    ffmpeg_exe, "-y", "-f", "concat", "-safe", "0",
    "-i", concat_file, "-c", "copy", out_voice
], check=True)

total_dur = sum(sc["duration"] for sc in segments)
print(f"Total narration duration for Video 2: {total_dur:.2f}s")

bg_music = os.path.join(WORK_DIR, "bg_music.wav")
out_final_audio = os.path.join(AUDIO_DIR, "final_audio_video2.mp3")
subprocess.run([
    ffmpeg_exe, "-y",
    "-i", out_voice,
    "-i", bg_music,
    "-filter_complex", "[0:a]volume=1.25[a0];[1:a]aloop=loop=-1:size=2e+09,volume=0.22[a1];[a0][a1]amix=inputs=2:duration=first:dropout_transition=2[aout]",
    "-map", "[aout]",
    "-c:a", "libmp3lame", "-b:a", "192k",
    out_final_audio
], check=True)

print("Generated final_audio_video2.mp3 successfully!")
