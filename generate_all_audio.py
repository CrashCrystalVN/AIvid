import subprocess
import sys
import os
import json
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

VOICE = "vi-VN-HoaiMyNeural"

segments = [
    {
        "id": "seg1",
        "title": "Tình huống thực tế",
        "text": "Chào thầy cô và các bạn! Hãy cùng nhóm mình bắt đầu bằng một tình huống thực tế nhé: Một chiếc ô tô đi qua ngã tư với tốc độ 36 km/h. Sau 10 giây, xe đi được quãng đường 100 m. Câu hỏi đặt ra là: Liệu chỉ biết quãng đường 100 m, chúng mình có thể xác định chính xác xe đang ở đâu trên bản đồ không?"
    },
    {
        "id": "seg2",
        "title": "Hệ tọa độ",
        "text": "Chắc chắn là chưa thể rồi, đúng không? Để biết chính xác vị trí, chúng ta cần một hệ tọa độ gắn với vật mốc. Trong đời sống, các bạn thường thấy hệ tọa độ địa lí với trục Ox theo hướng Tây – Đông và trục Oy theo hướng Bắc – Nam. Điểm A có tọa độ 20 m theo hướng 45 độ Đông – Bắc."
    },
    {
        "id": "seg3",
        "title": "Hệ quy chiếu & Chất điểm",
        "text": "Khi chúng mình kết hợp hệ tọa độ này cùng với mốc thời gian và một chiếc đồng hồ bấm giờ, ta sẽ có một hệ quy chiếu hoàn chỉnh. Nếu xe chỉ chạy thẳng trên một đường, chúng mình chỉ cần chọn duy nhất một trục Ox trùng với đường đi. Và khi kích thước xe rất nhỏ so với quãng đường 100 m, tụi mình hoàn toàn có thể coi nó là một chất điểm!"
    },
    {
        "id": "seg4",
        "title": "Câu hỏi tương tác",
        "text": "Câu hỏi tương tác: Khi nào độ dài quãng đường cho phép chúng ta coi một vật chuyển động là một chất điểm?"
    }
]

for seg in segments:
    out_mp3 = f"audio_{seg['id']}.mp3"
    txt_file = f"text_{seg['id']}.txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(seg["text"])
    
    cmd = [
        sys.executable, "-m", "edge_tts",
        "--voice", VOICE,
        "-f", txt_file,
        "--write-media", out_mp3
    ]
    subprocess.run(cmd, check=True)
    
    # Get audio duration using ffprobe/ffmpeg
    probe_cmd = [
        ffmpeg_exe, "-i", out_mp3
    ]
    res = subprocess.run(probe_cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    # Parse duration
    duration = 0.0
    for line in res.stderr.split("\n"):
        if "Duration:" in line:
            t_str = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = t_str.split(":")
            duration = float(h)*3600 + float(m)*60 + float(s)
            break
    print(f"Segment {seg['id']}: {duration:.2f} seconds")

print("All segments generated successfully!")
