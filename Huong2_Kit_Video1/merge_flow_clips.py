"""
CÔNG CỤ TỰ ĐỘNG GHÉP 5 CLIP TỪ GOOGLE FLOW / KLING / DREAMINA THÀNH VIDEO HOÀN CHỈNH
Hướng dẫn:
1. Sau khi tải 5 clip chuyển động từ Google Flow / Kling / Dreamina về, hãy đặt tên lần lượt là:
   clip1.mp4, clip2.mp4, clip3.mp4, clip4.mp4, clip5.mp4 và bỏ vào thư mục Huong2_Kit_Video1 này.
2. Chạy lệnh: python merge_flow_clips.py
   -> Hệ thống sẽ tự động khớp độ dài từng clip với từng đoạn giọng đọc (Canh1..Canh5.mp3),
      trộn nhạc nền và xuất ra file Video1_GoogleFlow_HoanChinh.mp4!
"""
import os
import sys
import subprocess
import imageio_ffmpeg

sys.stdout.reconfigure(encoding="utf-8")
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
HERE = os.path.dirname(os.path.abspath(__file__))

clips = [
    ("clip1.mp4", "Canh1_NgaTu_Oto.mp3", "seg_out_1.mp4"),
    ("clip2.mp4", "Canh2_HocSinh_DatVanDe.mp3", "seg_out_2.mp4"),
    ("clip3.mp4", "Canh3_HeToaDo_Oxy.mp3", "seg_out_3.mp4"),
    ("clip4.mp4", "Canh4_HeQuyChieu_ChatDiem.mp3", "seg_out_4.mp4"),
    ("clip5.mp4", "Canh5_CauHoi_TuongTac.mp3", "seg_out_5.mp4"),
]

missing = [c[0] for c in clips if not os.path.exists(os.path.join(HERE, c[0]))]
if missing:
    print("Đang chờ bạn tải các clip từ Google Flow / Kling / Dreamina về thư mục này:")
    for m in missing:
        print(f"  - Thiếu file: {m}")
    sys.exit(0)

concat_list = []
for v_file, a_file, out_seg in clips:
    v_path = os.path.join(HERE, v_file)
    a_path = os.path.join(HERE, a_file)
    out_path = os.path.join(HERE, out_seg)
    # Loop video smoothly (ping-pong or stream_loop) to match exact audio length
    cmd = [
        ffmpeg_exe, "-y",
        "-stream_loop", "-1", "-i", v_path,
        "-i", a_path,
        "-map", "0:v:0", "-map", "1:a:0",
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=24",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest", out_path
    ]
    subprocess.run(cmd, check=True)
    concat_list.append(f"file '{out_seg}'")
    print(f"Đã ghép xong phân cảnh: {out_seg}")

concat_txt = os.path.join(HERE, "concat_flow.txt")
with open(concat_txt, "w", encoding="utf-8") as f:
    f.write("\n".join(concat_list) + "\n")

final_out = os.path.join(HERE, "Video1_GoogleFlow_HoanChinh.mp4")
subprocess.run([
    ffmpeg_exe, "-y", "-f", "concat", "-safe", "0",
    "-i", concat_txt, "-c", "copy", final_out
], check=True)

print("HOÀN TẤT! Video đã lưu tại:", final_out)
