"""
Render Hybrid Video Pipeline for Physics 10 (Google Flow + Hologram HUD)
Renders 1080p @ 24fps high-tech educational videos combining:
  1. Google Flow / Kling AI video clips (with ping-pong / cross-loop) OR Ken Burns keyframes
  2. 7 Hologram Sci-Fi HUD graphic overlays (hud_animator.py)
  3. Dynamic Vietnamese subtitles, MC presenter badge, progress bar
  4. Audio narration (voiceover + background music mixing)

Usage:
  python render_hybrid_video.py --video V1_B4_ViTri_HeQuyChieu
  python render_hybrid_video.py --all
  python render_hybrid_video.py --preview-hud
  python render_hybrid_video.py --video V1_B4_ViTri_HeQuyChieu --fast
"""

import os
import sys
import json
import time
import argparse
import subprocess
from typing import Dict, Any, List, Optional, Tuple
from PIL import Image
import imageio_ffmpeg

import hud_animator

# Configure standard encoding for Windows console
sys.stdout.reconfigure(encoding="utf-8")

WIDTH, HEIGHT = 1920, 1080
DEFAULT_FPS = 24
CROSSFADE_DUR = 0.40  # seconds between scenes
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()


# ---------------------------------------------------------------------------
# AUDIO MANAGEMENT & TTS SYNTHESIZER
# ---------------------------------------------------------------------------
def get_audio_duration(audio_path: str) -> float:
    """Probes exact audio file duration using FFmpeg."""
    if not os.path.exists(audio_path):
        return 5.0
    try:
        cmd = [ffmpeg_exe, "-i", audio_path]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in res.stderr.split("\n"):
            if "Duration:" in line:
                t_str = line.split("Duration:")[1].split(",")[0].strip()
                h, m, s = t_str.split(":")
                return float(h) * 3600 + float(m) * 60 + float(s)
    except Exception as e:
        print(f"Warning probing duration for {audio_path}: {e}")
    return 6.0


def ensure_scene_audio(
    work_dir: str,
    video_id: str,
    scene: Dict[str, Any],
    voice_actor: Optional[str] = None,
    use_clip_audio: bool = False
) -> str:
    """
    Checks for existing audio file or synthesizes via edge-tts if missing.
    If use_clip_audio is True, prioritizes extracting native speech from
    Google Flow / Omni 1.2 lip-sync video clips.
    Returns absolute path to the valid audio file.
    """
    audio_dir = os.path.join(work_dir, "audio", video_id)
    os.makedirs(audio_dir, exist_ok=True)

    sidx = scene["scene_idx"]
    target_mp3 = os.path.join(audio_dir, f"s{sidx}.mp3")

    # Priority 0: Native Omni 1.2 / 1.1 lip-sync speech audio from Flow clip
    if use_clip_audio:
        flow_clip = os.path.join(work_dir, "flow_clips", video_id, f"s{sidx}.mp4")
        if os.path.exists(flow_clip):
            if hud_animator.check_clip_has_audio(flow_clip):
                omni_mp3 = os.path.join(audio_dir, f"s{sidx}_omni.mp3")
                if hud_animator.extract_clip_audio(flow_clip, omni_mp3):
                    dur = get_audio_duration(omni_mp3)
                    print(f"  🎙️ [Omni 1.2 Lip-Sync Audio] Scene s{sidx}: Using native speech ({dur:.2f}s) from {flow_clip}")
                    return omni_mp3
                else:
                    print(f"  ⚠️ [Omni Audio] Failed extracting audio from {flow_clip}, falling back to studio TTS...")
            else:
                print(f"  ℹ️ [Audio Notice] Scene s{sidx}: Flow clip has no audio track, falling back to studio TTS...")
        else:
            print(f"  ℹ️ [Audio Notice] Scene s{sidx}: Flow clip not found at {flow_clip}, falling back to studio TTS...")

    # Priority 1: Check kits directory first (highest priority, always sync)
    kit_mp3 = os.path.join(work_dir, "kits", video_id, "audio", f"s{sidx}.mp3")
    if os.path.exists(kit_mp3) and os.path.getsize(kit_mp3) > 1000:
        import shutil
        shutil.copy2(kit_mp3, target_mp3)
        return target_mp3

    # Priority 2: If already exists in audio_dir and valid size (> 1KB), return
    if os.path.exists(target_mp3) and os.path.getsize(target_mp3) > 1000:
        return target_mp3

    # Check alternative existing locations (e.g., from earlier kits)
    alt_candidates = [
        os.path.join(work_dir, "Huong2_Kit_Video1", f"Canh{sidx}_*.mp3"),
        os.path.join(work_dir, "audio_video2", f"v2_s{sidx}.mp3"),
        os.path.join(work_dir, f"tts_s{sidx}.mp3"),
        os.path.join(work_dir, f"audio_seg{sidx}.mp3"),
    ]
    for alt in alt_candidates:
        if "*" in alt:
            import glob
            matches = glob.glob(alt)
            if matches and os.path.getsize(matches[0]) > 1000:
                import shutil
                shutil.copy2(matches[0], target_mp3)
                return target_mp3
        elif os.path.exists(alt) and os.path.getsize(alt) > 1000:
            import shutil
            shutil.copy2(alt, target_mp3)
            return target_mp3

    # Synthesize via edge-tts with retry and silent fallback
    speaker = scene.get("speaker", "Anh Thư")
    male_names = ["Hữu Trọng", "Thế Mỹ", "Minh Dũng", "Hoàng Nam", "Nam"]
    if any(m.lower() in speaker.lower() for m in male_names):
        voice = "vi-VN-NamMinhNeural"
    else:
        voice = "vi-VN-HoaiMyNeural"

    text = scene.get("voiceover_text", "Chào thầy cô và các bạn!")
    txt_file = os.path.join(audio_dir, f"s{sidx}.txt")
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(text)

    success = False
    for attempt in range(3):
        try:
            print(f"  [TTS] Synthesizing s{sidx} ({speaker} - {voice}) [attempt {attempt+1}]...")
            cmd = [
                sys.executable, "-m", "edge_tts",
                "--voice", voice,
                "-f", txt_file,
                "--write-media", target_mp3
            ]
            res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if res.returncode == 0 and os.path.exists(target_mp3) and os.path.getsize(target_mp3) > 1000:
                success = True
                break
        except Exception:
            pass
        time.sleep(1.0)

    if not success:
        print(f"  [TTS Fallback] Generating audio fallback for s{sidx}...")
        fallback_dur = float(scene.get("duration_sec", 6.0))
        cmd_fallback = [
            ffmpeg_exe, "-y",
            "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
            "-t", str(fallback_dur),
            "-c:a", "libmp3lame", "-b:a", "128k",
            target_mp3
        ]
        subprocess.run(cmd_fallback, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    return target_mp3


def prepare_full_audio(
    work_dir: str,
    video_id: str,
    scenes: List[Dict[str, Any]],
    use_clip_audio: bool = False
) -> Tuple[str, List[float]]:
    """
    Ensures all scene audio files exist, calculates exact durations,
    concatenates and mixes with bg_music.wav.
    Returns (final_audio_path, list_of_scene_durations).
    """
    audio_dir = os.path.join(work_dir, "audio", video_id)
    os.makedirs(audio_dir, exist_ok=True)

    durations = []
    concat_files = []

    for s in scenes:
        audio_path = ensure_scene_audio(work_dir, video_id, s, use_clip_audio=use_clip_audio)
        dur = get_audio_duration(audio_path)
        durations.append(dur)
        concat_files.append(f"file '{os.path.abspath(audio_path).replace(chr(92), '/')}'")

    # Concat file list
    concat_list_txt = os.path.join(audio_dir, "concat_scenes.txt")
    with open(concat_list_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(concat_files) + "\n")

    voice_only_mp3 = os.path.join(audio_dir, "voice_concat.mp3")
    cmd_concat = [
        ffmpeg_exe, "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list_txt, "-c", "copy", voice_only_mp3
    ]
    subprocess.run(cmd_concat, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    # Mix with BGM
    bgm_path = os.path.join(work_dir, "bg_music.wav")
    final_audio_mp3 = os.path.join(audio_dir, "final_audio.mp3")

    if os.path.exists(bgm_path):
        # Mix with voice boost and gentle BGM ducking
        cmd_mix = [
            ffmpeg_exe, "-y",
            "-i", voice_only_mp3,
            "-i", bgm_path,
            "-filter_complex",
            "[0:a]volume=1.35[a_voice];[1:a]aloop=loop=-1:size=2e+09,volume=0.18[a_bgm];[a_voice][a_bgm]amix=inputs=2:duration=first:dropout_transition=2[aout]",
            "-map", "[aout]",
            "-c:a", "libmp3lame", "-b:a", "192k",
            final_audio_mp3
        ]
        subprocess.run(cmd_mix, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    else:
        # Just copy voice only
        import shutil
        shutil.copy2(voice_only_mp3, final_audio_mp3)

    return final_audio_mp3, durations


# ---------------------------------------------------------------------------
# VIDEO RENDER ENGINE
# ---------------------------------------------------------------------------
def render_video(
    work_dir: str,
    video_plan: Dict[str, Any],
    out_dir: str,
    fps: int = DEFAULT_FPS,
    fast: bool = False,
    max_scenes: Optional[int] = None,
    use_clip_audio: bool = False
) -> str:
    """
    Renders full video combining background (Flow / Keyframe) + HUD overlay.
    """
    video_id = video_plan["video_id"]
    lesson_title = video_plan.get("title", "Vật lí 10")
    scenes = video_plan["scenes"]

    if max_scenes and max_scenes < len(scenes):
        scenes = scenes[:max_scenes]

    os.makedirs(out_dir, exist_ok=True)
    output_mp4 = os.path.join(out_dir, f"{video_id}.mp4")

    print(f"\n========================================================")
    print(f"🎬 RENDERING VIDEO: {video_id}")
    print(f"📖 Title: {lesson_title}")
    print(f"🔢 Total Scenes: {len(scenes)}")
    if use_clip_audio:
        print(f"🎙️ Audio Mode: Prioritize Omni 1.2 / 1.1 Lip-Sync Clip Audio")
    print(f"========================================================")

    # 1. Prepare Audio
    print("🔊 Step 1/3: Preparing narration audio and background music...")
    final_audio_path, durations = prepare_full_audio(work_dir, video_id, scenes, use_clip_audio=use_clip_audio)
    total_duration = sum(durations)
    print(f"  ✓ Audio ready: {total_duration:.2f}s total duration.")

    # 2. Compute Scene Timelines
    timeline = []
    cur_t = 0.0
    for s_idx, (s, dur) in enumerate(zip(scenes, durations)):
        start_t = cur_t
        end_t = cur_t + dur
        timeline.append({
            "idx": s_idx,
            "scene": s,
            "start_t": start_t,
            "end_t": end_t,
            "duration": dur
        })
        cur_t = end_t
        flow_file = os.path.join(work_dir, "flow_clips", video_id, f"s{s['scene_idx']}.mp4")
        src_tag = f"🎬 Flow Clip (s{s['scene_idx']}.mp4)" if os.path.exists(flow_file) else "🖼️ Fallback Keyframe"
        print(f"  • Scene s{s['scene_idx']} [{s.get('hud_type', 'hud_boxes')}]: {start_t:.1f}s -> {end_t:.1f}s ({dur:.1f}s) | Source: {src_tag}")

    # 3. Setup FFmpeg Output Pipe
    actual_fps = 12 if fast else fps
    preset = "ultrafast" if fast else "veryfast"
    crf = "23" if fast else "19"
    total_frames = int(total_duration * actual_fps)

    print(f"\n🎥 Step 2/3: Rendering {total_frames} frames @ {actual_fps}fps (1920x1080)...")

    cmd_render = [
        ffmpeg_exe, "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}", "-pix_fmt", "rgb24",
        "-r", str(actual_fps), "-i", "-",
        "-i", final_audio_path,
        "-c:v", "libx264", "-preset", preset,
        "-pix_fmt", "yuv420p", "-crf", crf,
        "-c:a", "aac", "-b:a", "192k",
        "-shortest", output_mp4
    ]

    pipe = subprocess.Popen(cmd_render, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    bg_provider = hud_animator.BackgroundVideoProvider(work_dir)

    start_render_time = time.time()
    last_reported_pct = -5

    # Render frame loop
    for f_idx in range(total_frames):
        t = f_idx / actual_fps

        # Find active scene
        active_entry = timeline[-1]
        for entry in timeline:
            if entry["start_t"] <= t <= entry["end_t"]:
                active_entry = entry
                break

        s_idx = active_entry["idx"]
        s_data = active_entry["scene"]
        s_dur = active_entry["duration"]
        local_t = t - active_entry["start_t"]
        total_p = min(1.0, max(0.0, t / max(0.1, total_duration)))

        # Background frame
        bg = bg_provider.get_frame(video_id, s_data["scene_idx"], local_t, s_dur)

        # Composite HUD frame
        frame = hud_animator.composite_scene_frame(
            bg_frame=bg,
            scene_data=s_data,
            local_t=local_t,
            duration=s_dur,
            total_progress=total_p,
            lesson_title=lesson_title
        )

        # Crossfade transition (between scenes)
        if s_idx > 0 and local_t < CROSSFADE_DUR:
            prev_entry = timeline[s_idx - 1]
            prev_bg = bg_provider.get_frame(
                video_id,
                prev_entry["scene"]["scene_idx"],
                prev_entry["duration"],
                prev_entry["duration"]
            )
            prev_frame = hud_animator.composite_scene_frame(
                bg_frame=prev_bg,
                scene_data=prev_entry["scene"],
                local_t=prev_entry["duration"],
                duration=prev_entry["duration"],
                total_progress=total_p,
                lesson_title=lesson_title
            )
            blend_alpha = local_t / CROSSFADE_DUR
            frame = Image.blend(prev_frame, frame, blend_alpha)

        # Write frame to pipe
        pipe.stdin.write(frame.tobytes())

        # Progress reporting
        pct = int(f_idx * 100 / total_frames)
        if pct >= last_reported_pct + 5:
            elapsed = time.time() - start_render_time
            fps_speed = (f_idx + 1) / max(0.1, elapsed)
            remaining_s = (total_frames - f_idx) / max(1.0, fps_speed)
            print(f"  [{pct:3d}%] Frame {f_idx}/{total_frames} ({fps_speed:.1f} fps) | ETA: {remaining_s:.0f}s")
            last_reported_pct = pct

    pipe.stdin.close()
    pipe.wait()

    render_elapsed = time.time() - start_render_time
    file_size_mb = os.path.getsize(output_mp4) / (1024 * 1024)

    print(f"\n🎉 Step 3/3: COMPLETED!")
    print(f"  • File: {output_mp4}")
    print(f"  • Size: {file_size_mb:.2f} MB")
    print(f"  • Render Time: {render_elapsed:.1f} seconds")
    return output_mp4


# ---------------------------------------------------------------------------
# PREVIEW HUD GENERATOR
# ---------------------------------------------------------------------------
def generate_preview_huds(work_dir: str, out_dir: str):
    """Renders high-res 1920x1080 preview stills of all 7 HUD types."""
    os.makedirs(out_dir, exist_ok=True)
    plan_path = os.path.join(work_dir, "master_plan_7videos.json")
    with open(plan_path, "r", encoding="utf-8") as f:
        plan = json.load(f)

    types_needed = {
        "title_banner": None,
        "hud_boxes": None,
        "speed_gauge": None,
        "animated_axes": None,
        "animated_vector_road": None,
        "comparison_table": None,
        "quiz_popup": None
    }

    for v in plan["videos"]:
        for s in v["scenes"]:
            ht = s.get("hud_type")
            if ht in types_needed and types_needed[ht] is None:
                types_needed[ht] = (v["video_id"], s, v.get("title", "Vật lí 10"))

    bg_provider = hud_animator.BackgroundVideoProvider(work_dir)
    print("\n========================================================")
    print("🎨 GENERATING HIGH-RES PREVIEWS FOR ALL 7 HUD TYPES")
    print("========================================================")

    for ht, triple in types_needed.items():
        if not triple:
            continue
        vid, scene, l_title = triple
        bg = bg_provider.get_frame(vid, scene["scene_idx"], 3.0, 7.0)
        frame = hud_animator.composite_scene_frame(
            bg_frame=bg,
            scene_data=scene,
            local_t=5.6,
            duration=7.0,
            total_progress=0.7,
            lesson_title=l_title
        )
        out_file = os.path.join(out_dir, f"preview_{ht}.png")
        frame.save(out_file)
        print(f"  ✓ {ht:22s} -> {out_file}")

    print("\nPreviews saved in:", os.path.abspath(out_dir))


# ---------------------------------------------------------------------------
# CLI ENTRY POINT
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Render Hybrid Educational Videos with Hologram HUD.")
    parser.add_argument("--video", type=str, help="Specific video_id to render (e.g. V1_B4_ViTri_HeQuyChieu)")
    parser.add_argument("--all", action="store_true", help="Render all 7 videos from master_plan_7videos.json")
    parser.add_argument("--preview-hud", action="store_true", help="Generate 1920x1080 preview stills for all 7 HUD types")
    parser.add_argument("--out-dir", type=str, default="output_videos", help="Output directory for rendered MP4s")
    parser.add_argument("--fps", type=int, default=24, help="Frames per second (default 24)")
    parser.add_argument("--fast", action="store_true", help="Fast draft rendering mode (12fps, ultrafast)")
    parser.add_argument("--max-scenes", type=int, help="Render only first N scenes for quick verification")
    parser.add_argument("--use-clip-audio", action="store_true", help="Prioritize native speech audio from Google Flow/Omni clips (smart fallback to studio TTS)")

    args = parser.parse_args()
    work_dir = os.path.dirname(os.path.abspath(__file__))

    if args.preview_hud:
        generate_preview_huds(work_dir, os.path.join(work_dir, "preview_huds"))
        return

    plan_path = os.path.join(work_dir, "master_plan_7videos.json")
    if not os.path.exists(plan_path):
        print(f"Error: {plan_path} not found!")
        sys.exit(1)

    with open(plan_path, "r", encoding="utf-8") as f:
        plan = json.load(f)

    videos = plan.get("videos", [])

    if args.video:
        target_ids = [vid.strip() for vid in args.video.split(",") if vid.strip()]
        matched = [v for v in videos if v["video_id"] in target_ids]
        if not matched:
            print(f"Error: Video ID '{args.video}' not found in master_plan_7videos.json!")
            print("Available video IDs:")
            for v in videos:
                print(f"  - {v['video_id']}")
            sys.exit(1)
        for idx, v in enumerate(matched):
            print(f"\n>>> PROCESSING VIDEO {idx+1}/{len(matched)}: {v['video_id']}")
            render_video(
                work_dir,
                v,
                os.path.join(work_dir, args.out_dir),
                fps=args.fps,
                fast=args.fast,
                max_scenes=args.max_scenes,
                use_clip_audio=args.use_clip_audio
            )

    elif args.all:
        for idx, v in enumerate(videos):
            print(f"\n>>> PROCESSING VIDEO {idx+1}/{len(videos)}: {v['video_id']}")
            render_video(
                work_dir,
                v,
                os.path.join(work_dir, args.out_dir),
                fps=args.fps,
                fast=args.fast,
                max_scenes=args.max_scenes,
                use_clip_audio=args.use_clip_audio
            )

    else:
        print("Please specify an action:")
        print("  --video <video_id>   : Render a specific video")
        print("  --all                : Render all 7 videos")
        print("  --preview-hud        : Generate preview images for all 7 HUD types")


if __name__ == "__main__":
    main()
