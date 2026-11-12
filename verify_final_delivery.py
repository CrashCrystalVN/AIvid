import os
import json

WORK_DIR = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid"
HTML_PATH = os.path.join(WORK_DIR, "GoogleFlow_Hybrid_7Videos_Kit.html")
PLAN_PATH = os.path.join(WORK_DIR, "master_plan_7videos.json")
BGM_PATH = os.path.join(WORK_DIR, "bg_music.wav")

print("=== VERIFY FINAL ASSETS ===")
print(f"1. HTML Web Kit: {os.path.exists(HTML_PATH)} ({os.path.getsize(HTML_PATH):,} bytes)")
print(f"2. Master Plan: {os.path.exists(PLAN_PATH)} ({os.path.getsize(PLAN_PATH):,} bytes)")
print(f"3. BGM 120s: {os.path.exists(BGM_PATH)} ({os.path.getsize(BGM_PATH):,} bytes)")

with open(PLAN_PATH, "r", encoding="utf-8") as f:
    plan = json.load(f)

print(f"\nTotal Videos in Plan: {len(plan['videos'])}")
total_clips = 0
total_dur = 0.0

for v in plan["videos"]:
    vid = v["video_id"]
    scenes = v["scenes"]
    n = len(scenes)
    total_clips += n
    v_dur = sum(s.get("audio_duration", 0) for s in scenes)
    total_dur += v_dur
    
    # Check audio files
    audio_files_ok = all(
        os.path.exists(os.path.join(WORK_DIR, "kits", vid, "audio", f"s{s['scene_idx']}.mp3"))
        for s in scenes
    )
    print(f"• {vid} [{v.get('mc_character', {}).get('name')}, {v.get('voice_actor')}]: {n} scenes, {v_dur:.2f}s | Audio Files OK: {audio_files_ok}")

print(f"\nTotal Clips across 7 Videos: {total_clips}/48")
print(f"Total Video Duration: {total_dur:.2f}s ({int(total_dur // 60)}m {int(total_dur % 60)}s)")
print(f"Budget: {total_clips * 20} credits / 1,000 credits (Reserve: {1000 - total_clips * 20} credits)")
