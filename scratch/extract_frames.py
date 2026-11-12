import os
import sys
import subprocess
import json
import datetime
from pathlib import Path
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
print(f"Using ffmpeg: {ffmpeg_exe}")

base_dir = Path(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid")
flow_clips_dir = base_dir / "flow_clips"
output_dir = base_dir / "scratch" / "flow_frame_audit"
output_dir.mkdir(parents=True, exist_ok=True)

targets = [
    ("V3", "V3_B4_TongHop_DoDichChuyen", 9),
    ("V4", "V4_B5_Nhom1_TocDo_VanToc", 6),
    ("V5", "V5_B5_Nhom1_TongHop_VanToc", 5),
    ("V6", "V6_B5_Nhom2_TocDo_VanToc", 5),
    ("V7", "V7_B5_Nhom2_TongHop_VanToc", 5),
]

# We will probe each video using ffprobe or ffmpeg
results = []

for v_code, folder_name, n_scenes in targets:
    v_dir = flow_clips_dir / folder_name
    for i in range(1, n_scenes + 1):
        s_name = f"s{i}.mp4"
        clip_path = v_dir / s_name
        if not clip_path.exists():
            print(f"Missing {clip_path}")
            continue
        
        stat = clip_path.stat()
        mtime = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        size_mb = stat.st_size / (1024 * 1024)
        
        # Probe video using ffmpeg
        probe_cmd = [ffmpeg_exe, "-i", str(clip_path)]
        p = subprocess.run(probe_cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors="ignore")
        output = p.stderr
        
        duration = None
        width = None
        height = None
        fps = None
        
        for line in output.splitlines():
            if "Duration:" in line:
                # Duration: 00:00:05.00, start: 0.000000, bitrate: 6046 kb/s
                parts = line.split("Duration:")[1].split(",")[0].strip()
                try:
                    h, m, s = parts.split(":")
                    duration = float(h) * 3600 + float(m) * 60 + float(s)
                except Exception as e:
                    pass
            if "Video:" in line and "Stream #" in line:
                # Stream #0:0[0x1](und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709, progressive), 1920x1080 [SAR 1:1 DAR 16:9], 6042 kb/s, 24 fps, 24 tbr, 12288 tbn (default)
                try:
                    for token in line.split(","):
                        token = token.strip()
                        if "x" in token and any(c.isdigit() for c in token):
                            sub = token.split()[0]
                            if "x" in sub:
                                w_str, h_str = sub.split("x")
                                if w_str.isdigit() and h_str.isdigit():
                                    width = int(w_str)
                                    height = int(h_str)
                        if "fps" in token:
                            fps_str = token.split("fps")[0].strip()
                            fps = float(fps_str)
                except Exception as e:
                    pass
        
        # Determine extraction time
        target_t = 2.5
        if duration and duration <= 2.5:
            target_t = duration / 2.0
            
        frame_filename = f"{v_code}_s{i}.jpg"
        frame_path = output_dir / frame_filename
        
        # Extract frame
        extract_cmd = [
            ffmpeg_exe, "-y",
            "-ss", str(target_t),
            "-i", str(clip_path),
            "-vframes", "1",
            "-q:v", "2",
            str(frame_path)
        ]
        subprocess.run(extract_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        info = {
            "video": v_code,
            "scene": f"s{i}",
            "filename": frame_filename,
            "frame_path": str(frame_path),
            "clip_path": str(clip_path),
            "width": width,
            "height": height,
            "fps": fps,
            "duration": round(duration, 2) if duration else None,
            "mtime": mtime,
            "size_mb": round(size_mb, 2)
        }
        results.append(info)
        print(f"Extracted {v_code} s{i}: {width}x{height}, {fps}fps, {info['duration']}s, mtime={mtime}")

with open(output_dir / "audit_meta.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"Total extracted: {len(results)} frames to {output_dir}")
