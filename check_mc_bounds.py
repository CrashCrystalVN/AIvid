import os
import subprocess
import imageio_ffmpeg
from PIL import Image
import numpy as np

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
work_dir = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid"
os.chdir(work_dir)

raw_dir = os.path.join(work_dir, "output_videos", "previews_v1", "raw_mc")
os.makedirs(raw_dir, exist_ok=True)

for s in range(1, 10):
    clip = f"flow_clips/V1_B4_ViTri_HeQuyChieu/s{s}.mp4"
    print(f"=== Scene {s} ===")
    for t in [2.0, 5.0, 8.0]:
        tmp_jpg = os.path.join(raw_dir, f"s{s}_t{int(t)}.jpg")
        cmd = [ffmpeg_exe, "-y", "-ss", str(t), "-i", clip, "-vframes", "1", "-q:v", "2", tmp_jpg]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Load and analyze
        img = Image.open(tmp_jpg).convert("RGB")
        arr = np.array(img)
        # Face / skin detection in top-mid region (y: 80-600)
        face_crop = arr[80:600, :, :]
        r = face_crop[:,:,0].astype(int)
        g = face_crop[:,:,1].astype(int)
        b = face_crop[:,:,2].astype(int)
        skin = (r > 130) & (g > 80) & (b > 60) & (r > g) & (g > b) & ((r - g) > 15) & ((r - b) > 20)
        skin_cols = np.sum(skin, axis=0)
        active = np.where(skin_cols > 25)[0]
        
        # Upper body detection
        body_crop = arr[350:850, :, :]
        r_b = body_crop[:,:,0].astype(int)
        g_b = body_crop[:,:,1].astype(int)
        b_b = body_crop[:,:,2].astype(int)
        # White shirt or jacket
        clothing = (r_b > 170) & (g_b > 170) & (b_b > 170)
        cloth_cols = np.sum(clothing, axis=0)
        active_cloth = np.where(cloth_cols > 50)[0]
        
        skin_str = f"[{active[0]}, {active[-1]}] (center {int(np.mean(active))})" if len(active) > 0 else "none"
        cloth_str = f"[{active_cloth[0]}, {active_cloth[-1]}]" if len(active_cloth) > 0 else "none"
        print(f"  t={t}s: skin x={skin_str}, cloth x={cloth_str}")

