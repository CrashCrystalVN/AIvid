"""
CÔNG CỤ TỰ ĐỘNG GHÉP CÁC CLIP TỪ GOOGLE FLOW / KLING THÀNH VIDEO HOÀN CHỈNH CHO BÀI 12 & BÀI 14
Hướng dẫn sử dụng:
1. Khi tạo xong video từ Google Flow / Kling cho từng cảnh (s1 đến s5), lưu các file vào thư mục:
   - Bài 12: flow_clips/B12_ChuyenDongNem/ (đặt tên s1.mp4, s2.mp4, s3.mp4, s4.mp4, s5.mp4)
   - Bài 14: flow_clips/B14_DinhLuat1Newton/ (đặt tên s1.mp4, s2.mp4, s3.mp4, s4.mp4, s5.mp4)
2. Chạy lệnh:
   - Ghép Bài 12: python merge_b12_b14_clips.py --lesson 12
   - Ghép Bài 14: python merge_b12_b14_clips.py --lesson 14
   - Hoặc ghép cả 2: python merge_b12_b14_clips.py --all
"""

import os
import sys
import argparse
import subprocess
import imageio_ffmpeg

sys.stdout.reconfigure(encoding="utf-8")
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LESSONS = {
    "12": {
        "title": "Bài 12: Chuyển động ném",
        "clip_dir": os.path.join(BASE_DIR, "flow_clips", "B12_ChuyenDongNem"),
        "audio_dir": os.path.join(BASE_DIR, "audio", "B12_ChuyenDongNem"),
        "output_video": os.path.join(BASE_DIR, "output_videos", "Video_Bai12_ChuyenDongNem.mp4"),
    },
    "14": {
        "title": "Bài 14: Định luật 1 Newton",
        "clip_dir": os.path.join(BASE_DIR, "flow_clips", "B14_DinhLuat1Newton"),
        "audio_dir": os.path.join(BASE_DIR, "audio", "B14_DinhLuat1Newton"),
        "output_video": os.path.join(BASE_DIR, "output_videos", "Video_Bai14_DinhLuat1Newton.mp4"),
    }
}

def merge_lesson(lesson_id):
    cfg = LESSONS[lesson_id]
    clip_dir = cfg["clip_dir"]
    audio_dir = cfg["audio_dir"]
    out_final = cfg["output_video"]
    os.makedirs(os.path.dirname(out_final), exist_ok=True)
    os.makedirs(clip_dir, exist_ok=True)

    print(f"\n==========================================")
    print(f"🎬 ĐANG XỬ LÝ: {cfg['title']}")
    print(f"==========================================")

    # Check for 5 scene clips
    missing = []
    scenes = []
    for i in range(1, 6):
        v_name = f"s{i}.mp4"
        v_path = os.path.join(clip_dir, v_name)
        a_path = os.path.join(audio_dir, f"s{i}.mp3")
        if not os.path.exists(v_path):
            missing.append(v_name)
        scenes.append((v_path, a_path, os.path.join(clip_dir, f"render_s{i}.mp4")))

    if missing:
        print(f"⚠️ Chưa tìm thấy đủ clip trong {clip_dir}:")
        for m in missing:
            print(f"   - Thiếu file: {m}")
        print("💡 Hãy dán các clip tải về từ Google Flow vào thư mục trên rồi chạy lại lệnh này.")
        return False

    concat_lines = []
    for idx, (v_path, a_path, out_seg) in enumerate(scenes, 1):
        print(f"  ⚡ Đang render phân cảnh {idx}/5...")
        cmd = [
            ffmpeg_exe, "-y",
            "-stream_loop", "-1", "-i", v_path,
            "-i", a_path,
            "-map", "0:v:0", "-map", "1:a:0",
            "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=24",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest", out_seg
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        concat_lines.append(f"file '{out_seg.replace(chr(92), '/')}'")

    concat_file = os.path.join(clip_dir, "concat.txt")
    with open(concat_file, "w", encoding="utf-8") as f:
        f.write("\n".join(concat_lines) + "\n")

    print(f"  🔗 Đang ghép 5 phân cảnh thành video thành phẩm...")
    subprocess.run([
        ffmpeg_exe, "-y", "-f", "concat", "-safe", "0",
        "-i", concat_file, "-c", "copy", out_final
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    sz_mb = os.path.getsize(out_final) / (1024 * 1024)
    print(f"✅ THÀNH CÔNG! Video đã xuất tại: {out_final} ({sz_mb:.2f} MB)")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lesson", choices=["12", "14"], help="Mã bài cần ghép (12 hoặc 14)")
    parser.add_argument("--all", action="store_true", help="Ghép cả Bài 12 và Bài 14")
    args = parser.parse_args()

    if args.all:
        merge_lesson("12")
        merge_lesson("14")
    elif args.lesson:
        merge_lesson(args.lesson)
    else:
        print("Vui lòng chỉ định bài: python merge_b12_b14_clips.py --lesson 12 (hoặc 14, hoặc --all)")
