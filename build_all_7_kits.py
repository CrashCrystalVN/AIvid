import os
import json
import html

WORK_DIR = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid"
PLAN_FILE = os.path.join(WORK_DIR, "master_plan_7videos.json")
OUTPUT_HTML = os.path.join(WORK_DIR, "GoogleFlow_Hybrid_7Videos_Kit.html")

def build_kit():
    with open(PLAN_FILE, "r", encoding="utf-8") as f:
        plan = json.load(f)

    videos = plan.get("videos", [])
    total_clips = sum(len(v.get("scenes", [])) for v in videos)
    
    # Calculate account specific clip counts
    acc1_vids = ["V1_B4_ViTri_HeQuyChieu", "V2_B4_DoDichChuyen_QuangDuong", "V3_B4_TongHop_DoDichChuyen"]
    acc2_vids = ["V4_B5_Nhom1_TocDo_VanToc", "V5_B5_Nhom1_TongHop_VanToc", "V6_B5_Nhom2_TocDo_VanToc", "V7_B5_Nhom2_TongHop_VanToc"]
    
    acc1_clips = sum(len(v.get("scenes", [])) for v in videos if v["video_id"] in acc1_vids)
    acc2_clips = sum(len(v.get("scenes", [])) for v in videos if v["video_id"] in acc2_vids)

    html_parts = []

    # HTML Header
    html_parts.append("""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Google Flow 7 Videos Hybrid Studio - 2,000 Credits Pro</title>
<style>
  :root {
    --bg-primary: #0a0f1d;
    --bg-secondary: #11192d;
    --bg-card: #182238;
    --bg-card-hover: #1f2c48;
    --border-color: #273552;
    --border-highlight: #38bdf8;
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --accent-cyan: #38bdf8;
    --accent-emerald: #10b981;
    --accent-amber: #f59e0b;
    --accent-purple: #a855f7;
    --accent-rose: #f43f5e;
    --accent-indigo: #6366f1;
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: var(--font-sans);
    background-color: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.5;
    padding: 24px;
    min-height: 100vh;
  }

  .container {
    max-width: 1480px;
    margin: 0 auto;
  }

  /* Header Section */
  .studio-header {
    background: linear-gradient(135deg, #111a30 0%, #1e293b 100%);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 24px;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
    position: relative;
    overflow: hidden;
  }
  .studio-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc, #10b981, #38bdf8);
    background-size: 200% auto;
    animation: gradientShift 6s linear infinite;
  }
  @keyframes gradientShift { 0% { background-position: 0% 0%; } 100% { background-position: 200% 0%; } }

  .header-main {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 20px;
  }
  .title-group h1 {
    font-size: 28px;
    font-weight: 800;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }
  .title-group h1 span.badge-pill {
    background: linear-gradient(135deg, #059669, #10b981);
    font-size: 13px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 9999px;
    letter-spacing: 0.5px;
    box-shadow: 0 0 12px rgba(16, 185, 129, 0.3);
  }
  .title-group h1 span.badge-sub {
    background: linear-gradient(135deg, #0284c7, #2563eb);
    font-size: 13px;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 9999px;
  }
  .title-group h1 span.badge-omni-pill {
    background: linear-gradient(135deg, #7c3aed, #06b6d4);
    font-size: 13px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 9999px;
    letter-spacing: 0.5px;
    box-shadow: 0 0 12px rgba(124, 58, 237, 0.4);
    color: #fff;
  }
  .title-group p {
    color: var(--text-secondary);
    margin-top: 8px;
    font-size: 14.5px;
    max-width: 780px;
  }

  /* Dual Account Switcher & Budget Tracker Card */
  .budget-tracker {
    background: rgba(15, 23, 42, 0.9);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 16px 20px;
    min-width: 440px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  }
  .account-switcher-tabs {
    display: flex;
    gap: 6px;
    margin-bottom: 12px;
    background: #090d16;
    padding: 4px;
    border-radius: 8px;
    border: 1px solid #1e293b;
  }
  .acc-tab-btn {
    flex: 1;
    background: transparent;
    border: none;
    color: var(--text-secondary);
    font-size: 11.5px;
    font-weight: 700;
    padding: 6px 8px;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    text-align: center;
  }
  .acc-tab-btn:hover {
    color: #fff;
    background: rgba(255, 255, 255, 0.05);
  }
  .acc-tab-btn.active {
    background: #1e293b;
    color: var(--accent-cyan);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(56, 189, 248, 0.3);
  }
  .acc-tab-btn.active.acc-1 {
    color: #38bdf8;
    border-color: rgba(56, 189, 248, 0.4);
  }
  .acc-tab-btn.active.acc-2 {
    color: #a855f7;
    border-color: rgba(168, 85, 247, 0.4);
  }

  .budget-title {
    display: flex;
    justify-content: space-between;
    font-size: 13.5px;
    font-weight: 700;
    color: var(--text-secondary);
    margin-bottom: 8px;
  }
  .budget-title span.cr-val {
    color: var(--accent-cyan);
    font-size: 15px;
    font-weight: 800;
  }
  .progress-bar-bg {
    background: #1e293b;
    border-radius: 999px;
    height: 12px;
    overflow: hidden;
    margin-bottom: 10px;
    border: 1px solid #334155;
  }
  .progress-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #10b981, #38bdf8);
    width: 0%;
    transition: width 0.4s ease;
  }
  .budget-details {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: var(--text-muted);
  }
  .budget-details strong {
    color: var(--text-primary);
  }

  /* Tab Navigation */
  .tabs-wrapper {
    margin-bottom: 24px;
  }
  .nav-groups {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .group-label {
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--accent-cyan);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .group-tabs {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }
  .tab-btn {
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 10px 18px;
    color: var(--text-secondary);
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: all 0.2s ease;
  }
  .tab-btn:hover {
    background: var(--bg-card);
    color: var(--text-primary);
    border-color: #475569;
  }
  .tab-btn.active {
    background: linear-gradient(135deg, rgba(2, 132, 199, 0.2) 0%, rgba(37, 99, 235, 0.2) 100%);
    border-color: var(--accent-cyan);
    color: #fff;
    box-shadow: 0 0 15px rgba(56, 189, 248, 0.2);
  }
  .tab-btn.active.acc2 {
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.2) 0%, rgba(126, 34, 206, 0.2) 100%);
    border-color: var(--accent-purple);
    box-shadow: 0 0 15px rgba(168, 85, 247, 0.2);
  }
  .tab-btn .badge-count {
    background: #1e293b;
    border: 1px solid #334155;
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 6px;
    color: var(--accent-cyan);
  }
  .tab-btn.active .badge-count {
    background: var(--accent-cyan);
    color: #0b1120;
    border-color: var(--accent-cyan);
    font-weight: 700;
  }
  .tab-btn.active.acc2 .badge-count {
    background: var(--accent-purple);
    color: #ffffff;
    border-color: var(--accent-purple);
  }

  /* Video Panel */
  .video-panel {
    display: none;
  }
  .video-panel.active {
    display: block;
  }

  .video-info-box {
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 20px 24px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }
  .v-title-area h2 {
    font-size: 20px;
    font-weight: 800;
    color: #fff;
  }
  .v-title-area p {
    color: var(--text-secondary);
    font-size: 13.5px;
    margin-top: 4px;
  }
  .v-meta-badges {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }
  .v-badge {
    background: #1e293b;
    border: 1px solid #334155;
    font-size: 12px;
    padding: 6px 14px;
    border-radius: 8px;
    color: #cbd5e1;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-weight: 500;
  }
  .v-badge.acc-target-1 {
    background: rgba(56, 189, 248, 0.15);
    border: 1px solid #38bdf8;
    color: #38bdf8;
    font-weight: 700;
  }
  .v-badge.acc-target-2 {
    background: rgba(168, 85, 247, 0.15);
    border: 1px solid #a855f7;
    color: #d8b4fe;
    font-weight: 700;
  }
  .v-badge.kf-stat {
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: #10b981;
  }

  /* Scenes Container */
  .scenes-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .scene-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    overflow: hidden;
    transition: all 0.25s ease;
  }
  .scene-card:hover {
    border-color: #3b82f6;
  }
  .scene-card.completed {
    border-color: var(--accent-emerald);
    background: rgba(16, 185, 129, 0.03);
  }

  .scene-header {
    background: #111a30;
    padding: 12px 20px;
    border-bottom: 1px solid var(--border-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .scene-header-left {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .scene-num-badge {
    background: #0284c7;
    color: #fff;
    font-size: 13px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 6px;
  }
  .scene-title {
    font-size: 16px;
    font-weight: 700;
    color: #fff;
  }
  .scene-check-toggle {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    font-weight: 600;
    color: var(--text-secondary);
    cursor: pointer;
    user-select: none;
  }
  .scene-check-toggle input[type="checkbox"] {
    width: 18px;
    height: 18px;
    cursor: pointer;
    accent-color: var(--accent-emerald);
  }

  .scene-body {
    padding: 20px;
    display: grid;
    grid-template-columns: 420px 1fr;
    gap: 24px;
  }
  @media (max-width: 1024px) {
    .scene-body { grid-template-columns: 1fr; }
  }

  /* Left Column: Keyframe & Audio */
  .scene-left {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .keyframe-box {
    position: relative;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #334155;
    background: #0f172a;
    aspect-ratio: 16/9;
  }
  .keyframe-box img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }
  .keyframe-badge {
    position: absolute;
    bottom: 8px;
    left: 8px;
    background: rgba(0, 0, 0, 0.75);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 3px 10px;
    border-radius: 6px;
    font-size: 11px;
    color: #38bdf8;
    font-weight: 600;
  }
  .keyframe-badge.warning {
    color: #f59e0b;
    border-color: rgba(245, 158, 11, 0.35);
  }
  .keyframe-box.no-kf {
    display: flex;
    align-items: center;
    justify-content: center;
    background: radial-gradient(circle at center, #1e293b 0%, #0b1120 100%);
    border: 1px dashed rgba(245, 158, 11, 0.4);
  }
  .keyframe-missing-placeholder {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 14px;
    gap: 6px;
  }
  .missing-text {
    font-size: 13px;
    font-weight: 600;
    color: #f1f5f9;
  }
  .missing-sub {
    font-size: 11px;
    color: #94a3b8;
  }
  .badge-no-keyframe-alert {
    background: rgba(245, 158, 11, 0.1);
    border: 1px solid rgba(245, 158, 11, 0.35);
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 11.5px;
    line-height: 1.4;
    color: #fbbf24;
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 500;
  }
  .audio-player-wrapper {
    background: #0f172a;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 10px 14px;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
  .audio-meta {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: var(--text-secondary);
  }
  .audio-meta strong {
    color: var(--accent-cyan);
  }
  audio {
    width: 100%;
    height: 36px;
    border-radius: 6px;
  }
  .file-target-tag {
    background: #0f172a;
    border: 1px dashed #334155;
    border-radius: 8px;
    padding: 8px 12px;
    font-family: monospace;
    font-size: 12px;
    color: #94a3b8;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .file-target-tag code {
    color: #38bdf8;
  }
  .btn-mini-copy {
    background: #1e293b;
    border: 1px solid #475569;
    color: #cbd5e1;
    font-size: 11px;
    padding: 3px 8px;
    border-radius: 4px;
    cursor: pointer;
  }
  .btn-mini-copy:hover {
    background: #334155;
    color: #fff;
  }

  /* Right Column: Prompts, Voiceover, HUD */
  .scene-right {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .content-section {
    background: #0f172a;
    border: 1px solid #273552;
    border-radius: 10px;
    padding: 14px 18px;
  }
  .content-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
    flex-wrap: wrap;
    gap: 8px;
  }
  .section-label {
    font-size: 12.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .section-label.vo { color: #a855f7; }
  .section-label.prompt { color: #38bdf8; }
  .section-label.hud { color: #10b981; }

  .voiceover-p {
    font-size: 14.5px;
    color: #f1f5f9;
    line-height: 1.6;
    font-style: italic;
  }
  .subtitles-tag-list {
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  .sub-chunk-pill {
    background: #1e293b;
    border: 1px solid #334155;
    color: #94a3b8;
    font-size: 12px;
    padding: 2px 8px;
    border-radius: 4px;
  }

  /* Flow, Keyframe & B-Roll Prompts */
  .prompt-btn-group {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }
  .btn-copy-omni {
    background: linear-gradient(135deg, #7c3aed 0%, #06b6d4 100%);
    border: 1px solid #c084fc;
    color: #ffffff;
    font-weight: 700;
    font-size: 11.5px;
    padding: 6px 13px;
    border-radius: 6px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 0 12px rgba(124, 58, 237, 0.4);
    transition: transform 0.15s ease, filter 0.15s ease, box-shadow 0.15s ease;
  }
  .btn-copy-omni:hover {
    filter: brightness(1.15);
    transform: translateY(-1px);
    box-shadow: 0 0 16px rgba(6, 182, 212, 0.5);
  }
  .btn-copy-dialogue {
    background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
    border: 1px solid #818cf8;
    color: #c7d2fe;
    font-weight: 600;
    font-size: 11.5px;
    padding: 6px 12px;
    border-radius: 6px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: transform 0.15s ease, filter 0.15s ease;
  }
  .btn-copy-dialogue:hover {
    background: #3730a3;
    color: #ffffff;
    transform: translateY(-1px);
  }
  .btn-copy-kf {
    background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
    border: 1px solid #38bdf8;
    color: #ffffff;
    font-weight: 700;
    font-size: 11.5px;
    padding: 6px 12px;
    border-radius: 6px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: transform 0.15s ease, filter 0.15s ease;
  }
  .btn-copy-kf:hover {
    filter: brightness(1.2);
    transform: translateY(-1px);
  }
  .btn-copy-prompt {
    background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
    border: none;
    color: #0b1120;
    font-weight: 700;
    font-size: 11.5px;
    padding: 6px 13px;
    border-radius: 6px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: transform 0.15s ease, filter 0.15s ease;
  }
  .btn-copy-prompt:hover {
    filter: brightness(1.1);
    transform: translateY(-1px);
  }
  .btn-copy-broll {
    background: linear-gradient(135deg, #059669 0%, #047857 100%);
    border: 1px solid #34d399;
    color: #ffffff;
    font-weight: 700;
    font-size: 11.5px;
    padding: 6px 12px;
    border-radius: 6px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: transform 0.15s ease, filter 0.15s ease;
  }
  .btn-copy-broll:hover {
    filter: brightness(1.2);
    transform: translateY(-1px);
  }

  .prompts-container {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .prompt-box {
    position: relative;
    background: #090d16;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 13px;
    color: #e2e8f0;
    line-height: 1.5;
  }
  .prompt-box.kf-box {
    background: #0b1220;
    border: 1px dashed #223759;
    font-size: 12.5px;
    color: #94a3b8;
  }
  .prompt-box.broll-box {
    background: #0a1917;
    border: 1px dashed #134e4a;
    font-size: 12.5px;
    color: #a7f3d0;
  }
  .prompt-box.omni-box {
    background: linear-gradient(145deg, #110e23 0%, #0c1424 100%);
    border: 1px solid #7c3aed;
    border-left: 4px solid #a855f7;
    border-radius: 8px;
    padding: 12px 14px;
    box-shadow: 0 4px 16px rgba(124, 58, 237, 0.18);
  }
  .badge-omni {
    font-size: 10.5px;
    font-weight: 800;
    color: #c084fc;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: inline-flex;
    align-items: center;
    gap: 5px;
  }
  .omni-dialogue-highlight {
    background: rgba(168, 85, 247, 0.12);
    border: 1px dashed rgba(168, 85, 247, 0.45);
    border-radius: 6px;
    padding: 8px 12px;
    margin: 8px 0;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .omni-dialogue-tag {
    font-size: 11px;
    font-weight: 700;
    color: #e9d5ff;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .omni-dialogue-text {
    font-size: 14px;
    color: #38bdf8;
    font-style: italic;
    font-weight: 600;
    line-height: 1.5;
  }
  .prompt-content-text.omni-text {
    font-size: 12.5px;
    color: #cbd5e1;
    line-height: 1.5;
    background: rgba(0, 0, 0, 0.35);
    padding: 8px 10px;
    border-radius: 6px;
    border: 1px solid rgba(255, 255, 255, 0.05);
  }
  .omni-text-label {
    display: block;
    font-size: 10.5px;
    font-weight: 700;
    color: #94a3b8;
    margin-bottom: 4px;
    text-transform: uppercase;
  }
  .omni-guide-note {
    margin-top: 8px;
    padding-top: 6px;
    border-top: 1px solid rgba(124, 58, 237, 0.25);
    font-size: 11.5px;
    color: #a5b4fc;
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 500;
  }
  .omni-guide-note svg {
    flex-shrink: 0;
    color: #38bdf8;
  }
  .prompt-tag-label {
    margin-bottom: 5px;
  }
  .badge-veo {
    font-size: 10px;
    font-weight: 700;
    color: #f59e0b;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .badge-imagen {
    font-size: 10px;
    font-weight: 700;
    color: #38bdf8;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .badge-broll {
    font-size: 10px;
    font-weight: 700;
    color: #34d399;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .hud-badge-tag {
    background: rgba(168, 85, 247, 0.15);
    border: 1px solid #a855f7;
    color: #d8b4fe;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    text-transform: uppercase;
  }
  .hud-desc {
    font-size: 13px;
    color: #cbd5e1;
    line-height: 1.5;
  }
  .hud-key-val {
    margin-top: 8px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 8px;
  }
  .kv-item {
    background: #151e33;
    border: 1px solid #23314e;
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 12px;
  }
  .kv-key { color: #94a3b8; font-weight: 600; }
  .kv-val { color: #38bdf8; font-family: monospace; font-weight: 600; margin-left: 4px; }

  /* Notification toast */
  .toast {
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: #10b981;
    color: #0b1120;
    font-weight: 700;
    padding: 12px 20px;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
    transform: translateY(100px);
    opacity: 0;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    z-index: 9999;
  }
  .toast.show {
    transform: translateY(0);
    opacity: 1;
  }
</style>
</head>
<body>

<div class="container">
  <!-- STUDIO HEADER -->
  <header class="studio-header">
    <div class="header-main">
      <div class="title-group">
        <h1>
          Google Flow 7 Videos Hybrid Studio
          <span class="badge-pill">2,000 CREDITS PRO</span>
          <span class="badge-sub">VẬT LÍ 10</span>
          <span class="badge-omni-pill">🎙️ OMNI 1.2 / 1.1 LIP-SYNC READY</span>
        </h1>
        <p>Bộ công cụ tổ chức sản xuất 7 Video AI | Tích hợp <strong>Omni 1.2 / 1.1 Lip-Sync Speech</strong> (Video sinh kèm nhép miệng tiếng Việt tự nhiên) &amp; Veo 3.1 Fast | Phân bổ độc lập trên 2 Tài khoản Pro (1,000 credits/acc): <strong>Tài khoản 1 (Bài 4: V1, V2, V3)</strong> &amp; <strong>Tài khoản 2 (Bài 5: V4, V5, V6, V7)</strong> | Sẵn sàng B-Roll Cinematic &amp; Reroll thoải mái.</p>
      </div>

      <!-- DUAL ACCOUNT BUDGET TRACKER -->
      <div class="budget-tracker">
        <!-- Switcher Buttons -->
        <div class="account-switcher-tabs">
          <button class="acc-tab-btn active" id="btn-filter-all" onclick="setAccountFilter('all')">TỔNG HỢP (2 ACC - 2,000 CR)</button>
          <button class="acc-tab-btn acc-1" id="btn-filter-acc1" onclick="setAccountFilter('acc_1')">ACC 1: BÀI 4 (1,000 CR)</button>
          <button class="acc-tab-btn acc-2" id="btn-filter-acc2" onclick="setAccountFilter('acc_2')">ACC 2: BÀI 5 (1,000 CR)</button>
        </div>

        <div class="budget-title">
          <span id="filter-title">TIẾN ĐỘ TỔNG HỢP (2 TÀI KHOẢN PRO)</span>
          <span class="cr-val"><span id="stat-completed">0</span> / <span id="stat-total-clips">""" + str(total_clips) + """</span> clips (<span id="stat-credits">0</span> cr)</span>
        </div>
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" id="progress-bar"></div>
        </div>
        <div class="budget-details">
          <span>Ngân sách còn lại: <strong id="stat-remaining">2000</strong> / <span id="stat-cap">2000</span> credits</span>
          <span>Dự trữ B-roll/Reroll: <strong id="stat-reserve" style="color: #34d399;">1040 cr</strong></span>
        </div>
      </div>
    </div>
  </header>

  <!-- TAB NAVIGATION -->
  <div class="tabs-wrapper">
    <div class="nav-groups">
      <!-- Group 1: Nhóm 1 (5 Video) -->
      <div class="group-label" style="color: #38bdf8;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
        NHÓM 1 (5 VIDEO) — THẾ MỸ • ĐP.HOÀNG BÁCH • VĂN HOÀNG • THANH TÙNG • GIA NGUYÊN
      </div>
      <div class="group-tabs">
""")

    vid_to_v = {v["video_id"]: v for v in videos}
    nhom1_ids = ["V1_B4_ViTri_HeQuyChieu", "V2_B4_DoDichChuyen_QuangDuong", "V3_B4_TongHop_DoDichChuyen", "V6_B5_Nhom2_TocDo_VanToc", "V7_B5_Nhom2_TongHop_VanToc"]
    nhom2_ids = ["V4_B5_Nhom1_TocDo_VanToc", "V5_B5_Nhom1_TongHop_VanToc"]

    # Tab Buttons for Nhóm 1
    for vid in nhom1_ids:
        if vid in vid_to_v:
            v = vid_to_v[vid]
            v_title_short = v["title"].split(":")[1].strip() if ":" in v["title"] else v["title"]
            scenes_count = len(v.get("scenes", []))
            kf_ready_count = sum(1 for sc in v.get("scenes", []) if os.path.exists(os.path.join(WORK_DIR, "keyframes", vid, f"s{sc['scene_idx']}.png")))
            btn_cls = "tab-btn" if vid in acc1_vids else "tab-btn acc2"
            html_parts.append(f"""        <button class="{btn_cls}" onclick="switchTab('{vid}', this)" id="btn-tab-{vid}">
          <span>{v_title_short}</span>
          <span class="badge-count">{scenes_count} clips • {kf_ready_count}/{scenes_count} KF</span>
        </button>
""")

    html_parts.append("""      </div>

      <!-- Group 2: Nhóm 2 (2 Video) -->
      <div class="group-label" style="color: #a855f7; margin-top: 8px;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        NHÓM 2 (2 VIDEO) — BÀI 5: TỐC ĐỘ &amp; VẬN TỐC (CHƯA ĐIỀN THÀNH VIÊN)
      </div>
      <div class="group-tabs">
""")

    for vid in nhom2_ids:
        if vid in vid_to_v:
            v = vid_to_v[vid]
            v_title_short = v["title"].split(":")[1].strip() if ":" in v["title"] else v["title"]
            scenes_count = len(v.get("scenes", []))
            kf_ready_count = sum(1 for sc in v.get("scenes", []) if os.path.exists(os.path.join(WORK_DIR, "keyframes", vid, f"s{sc['scene_idx']}.png")))
            html_parts.append(f"""        <button class="tab-btn acc2" onclick="switchTab('{vid}', this)" id="btn-tab-{vid}">
          <span>{v_title_short}</span>
          <span class="badge-count">{scenes_count} clips • {kf_ready_count}/{scenes_count} KF</span>
        </button>
""")

    html_parts.append("""      </div>
    </div>
  </div>

  <!-- VIDEO CONTENT PANELS -->
  <main>
""")

    # Panels for each video
    for v_idx, v in enumerate(videos):
        vid = v["video_id"]
        acc_target = v.get("account_target", "Account 1 (Bài 4)" if vid in acc1_vids else "Account 2 (Bài 5)")
        acc_badge_class = "acc-target-1" if "Account 1" in acc_target else "acc-target-2"
        
        mc = v.get("mc_character", {})
        mc_name = mc.get("name", "MC")
        gender = mc.get("gender", "male")
        voice = v.get("voice_actor", "vi-VN-NamMinhNeural")
        scenes = v.get("scenes", [])
        actual_dur = v.get("actual_duration_sec", 0.0)
        formatted_dur = v.get("estimated_duration", f"{actual_dur}s")

        kf_ready_count = sum(1 for sc in scenes if os.path.exists(os.path.join(WORK_DIR, "keyframes", vid, f"s{sc['scene_idx']}.png")))

        presenters_display = v.get("presenters") or v.get("group_assignment", "")
        html_parts.append(f"""    <!-- PANEL: {vid} -->
    <section class="video-panel" id="panel-{vid}">
      <div class="video-info-box">
        <div class="v-title-area">
          <h2>{v['title']}</h2>
          <p>Thành viên thực hiện: <strong>{presenters_display}</strong> • Chủ đề: {v.get('theme', '')}</p>
        </div>
        <div class="v-meta-badges">
          <div class="v-badge {acc_badge_class}">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"></rect><path d="M7 15h0M2 9.5h20"></path></svg>
            {acc_target} (Hạn mức 1,000 cr)
          </div>
          <div class="v-badge duration">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            Thời lượng: {formatted_dur} ({len(scenes)} cảnh)
          </div>
          <div class="v-badge presenter">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
            Giọng đọc Omni AI: {voice}
          </div>
          <div class="v-badge kf-stat">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
            Keyframe mốc: {kf_ready_count}/{len(scenes)} sẵn sàng
          </div>
        </div>
      </div>

      <!-- SCENES LIST -->
      <div class="scenes-container">
""")

        for s in scenes:
            s_idx = s["scene_idx"]
            s_id = s.get("scene_id", f"{vid}_S{s_idx:02d}")
            s_title = s.get("title", f"Cảnh {s_idx}")
            s_dur = s.get("audio_duration", s.get("duration_sec", 10.0))
            vo_text = s.get("voiceover_text", "")
            flow_prompt = s.get("flow_i2v_prompt", "")
            kf_prompt = s.get("keyframe_prompt", "")
            broll_prompt = s.get("broll_prompt", "")
            hud_type = s.get("hud_type", "hud_overlay")
            hud_data = s.get("hud_data", {})
            sub_chunks = s.get("subtitle_chunks", [])
            
            # Omni 1.2 / 1.1 Lip-sync prompt combination
            clean_vo = vo_text.strip().replace('"', "'")
            clean_motion = flow_prompt.strip().rstrip('.')
            omni_prompt = f'{clean_motion}. Character speaks naturally in Vietnamese with matching lip-sync: "{clean_vo}"'
            
            # Keyframe image path & check
            keyframe_rel = f"keyframes/{vid}/s{s_idx}.png"
            keyframe_abs = os.path.join(WORK_DIR, "keyframes", vid, f"s{s_idx}.png")
            keyframe_exists = os.path.exists(keyframe_abs)

            # Audio path
            audio_rel = f"kits/{vid}/audio/s{s_idx}.mp3"
            # Target clip path
            clip_rel = f"flow_clips/{vid}/s{s_idx}.mp4"

            # Checkbox ID
            cb_id = f"cb_{vid}_s{s_idx}"

            if keyframe_exists:
                kf_block_html = f"""              <div class="keyframe-box">
                <img src="{keyframe_rel}" alt="Keyframe Cảnh {s_idx}" onerror="this.onerror=null; this.src='https://placehold.co/600x338/1e293b/38bdf8?text=Keyframe+s{s_idx}.png';">
                <div class="keyframe-badge">Keyframe s{s_idx}.png • {s_dur}s</div>
              </div>"""
            else:
                kf_block_html = f"""              <div class="keyframe-box no-kf">
                <div class="keyframe-missing-placeholder">
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                  <div class="missing-text">Chưa có Keyframe s{s_idx}.png</div>
                  <div class="missing-sub">Dùng Keyframe Prompt hoặc chạy Text-to-Video</div>
                </div>
                <div class="keyframe-badge warning">Chưa có Keyframe • {s_dur}s</div>
              </div>
              <div class="badge-no-keyframe-alert">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                <span>Chưa có Keyframe (Có thể copy Keyframe Prompt dưới đây hoặc chạy thẳng Text-to-Video trên Flow)</span>
              </div>"""

            html_parts.append(f"""        <!-- SCENE {s_idx} -->
        <article class="scene-card" id="card_{vid}_s{s_idx}">
          <div class="scene-header">
            <div class="scene-header-left">
              <span class="scene-num-badge">Cảnh {s_idx}</span>
              <span class="scene-title">{html.escape(s_title)}</span>
            </div>
            <label class="scene-check-toggle" for="{cb_id}">
              <input type="checkbox" id="{cb_id}" onchange="toggleSceneDone('{vid}', {s_idx}, this.checked)">
              <span>Đã tạo Flow (20 credits)</span>
            </label>
          </div>

          <div class="scene-body">
            <!-- Left: Keyframe & Audio -->
            <div class="scene-left">
{kf_block_html}

              <!-- Audio Player -->
              <div class="audio-player-wrapper">
                <div class="audio-meta">
                  <span>Thuyết minh TTS / Voice:</span>
                  <strong>{s_dur}s</strong>
                </div>
                <audio controls src="{audio_rel}" preload="none"></audio>
              </div>

              <!-- Destination file -->
              <div class="file-target-tag">
                <span>File lưu: <code>{clip_rel}</code></span>
                <button class="btn-mini-copy" onclick="copyText('{clip_rel}')">Copy Path</button>
              </div>
            </div>

            <!-- Right: Content, Prompts, HUD -->
            <div class="scene-right">
              <!-- Voiceover -->
              <div class="content-section">
                <div class="content-header">
                  <span class="section-label vo">1. Lời thoại thuyết minh (Voiceover &amp; Subtitle)</span>
                </div>
                <p class="voiceover-p">"{html.escape(vo_text)}"</p>
                <div class="subtitles-tag-list">
""")
            for sc in sub_chunks:
                html_parts.append(f"""                  <span class="sub-chunk-pill">{html.escape(sc)}</span>
""")

            html_parts.append(f"""                </div>
              </div>

              <!-- Flow, Keyframe & B-Roll Prompts -->
              <div class="content-section">
                <div class="content-header">
                  <span class="section-label prompt">2. Lệnh tạo video Google Flow &amp; Prompts Tùy chọn</span>
                  <div class="prompt-btn-group">
                    <button class="btn-copy-omni" onclick="copyOmniPrompt(this)" data-prompt="{html.escape(omni_prompt, quote=True)}">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
                      ✨ 1-Click Copy Omni Prompt (Video + Lời thoại)
                    </button>
                    <button class="btn-copy-dialogue" onclick="copyDialogue(this)" data-dialogue="{html.escape(vo_text, quote=True)}">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                      Copy Lời Thoại Riêng (Dialogue)
                    </button>
                    <button class="btn-copy-prompt" onclick="copyFlowPrompt(this)" data-prompt="{html.escape(flow_prompt, quote=True)}">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                      1-Click Copy Flow (Veo)
                    </button>
                    <button class="btn-copy-kf" onclick="copyKfPrompt(this)" data-prompt="{html.escape(kf_prompt, quote=True)}">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                      Copy Keyframe
                    </button>
                    <button class="btn-copy-broll" onclick="copyBrollPrompt(this)" data-prompt="{html.escape(broll_prompt, quote=True)}">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"></polygon><rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect></svg>
                      1-Click Copy B-Roll
                    </button>
                  </div>
                </div>
                <div class="prompts-container">
                  <!-- OMNI 1.2 / 1.1 LIP-SYNC BOX -->
                  <div class="prompt-box omni-box">
                    <div class="prompt-tag-label">
                      <span class="badge-omni">🎙️ Google Flow / Omni 1.2 &amp; 1.1 (Video + Lời Thoại Nhép Miệng Lip-Sync)</span>
                    </div>
                    <div class="omni-dialogue-highlight">
                      <span class="omni-dialogue-tag">🎙️ Lời thoại Omni (Lip-sync):</span>
                      <span class="omni-dialogue-text">"{html.escape(vo_text)}"</span>
                    </div>
                    <div class="prompt-content-text omni-text">
                      <span class="omni-text-label">Cấu trúc prompt Motion + Speech:</span>
                      {html.escape(omni_prompt)}
                    </div>
                    <div class="omni-guide-note">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                      <span>Khi dùng Omni 1.2/1.1, dán prompt kèm lời thoại này để AI tự động nhép miệng và phát âm tiếng Việt chuẩn theo nhân vật.</span>
                    </div>
                  </div>
                  <div class="prompt-box">
                    <div class="prompt-tag-label"><span class="badge-veo">Google Flow / Veo 3.1 Fast (I2V / T2V Prompt - 20 cr)</span></div>
                    <div class="prompt-content-text">{html.escape(flow_prompt)}</div>
                  </div>
                  <div class="prompt-box broll-box">
                    <div class="prompt-tag-label"><span class="badge-broll">B-Roll &amp; Cận Cảnh Cinematic (Shot phụ / góc máy 2 - 20 cr)</span></div>
                    <div class="prompt-content-text">{html.escape(broll_prompt)}</div>
                  </div>
                  <div class="prompt-box kf-box">
                    <div class="prompt-tag-label"><span class="badge-imagen">Keyframe Master Prompt (Imagen / Midjourney)</span></div>
                    <div class="prompt-content-text">{html.escape(kf_prompt)}</div>
                  </div>
                </div>
              </div>

              <!-- HUD Spec -->
              <div class="content-section">
                <div class="content-header">
                  <span class="section-label hud">3. Hiệu ứng Python HUD đè lên video</span>
                  <span class="hud-badge-tag">{hud_type}</span>
                </div>
                <div class="hud-desc">
                  Mô hình HUD overlay sẽ được Python vẽ đè lên video Flow để hiển thị chính xác các ký hiệu Vật lí:
                </div>
                <div class="hud-key-val">
""")
            for k, val in hud_data.items():
                html_parts.append(f"""                  <div class="kv-item">
                    <span class="kv-key">{html.escape(str(k))}:</span>
                    <span class="kv-val">{html.escape(str(val))}</span>
                  </div>
""")

            html_parts.append("""                </div>
              </div>
            </div>
          </div>
        </article>
""")

        html_parts.append("""      </div>
    </section>
""")

    # Bottom JavaScript
    html_parts.append(f"""  </main>
</div>

<!-- TOAST NOTIFICATION -->
<div class="toast" id="toast">Đã copy vào clipboard!</div>

<script>
  const TOTAL_CLIPS = {total_clips};
  const ACC1_CLIPS = {acc1_clips};
  const ACC2_CLIPS = {acc2_clips};
  const CREDIT_PER_CLIP = 20;

  const ACC1_VIDEOS = ['V1_B4_ViTri_HeQuyChieu', 'V2_B4_DoDichChuyen_QuangDuong', 'V3_B4_TongHop_DoDichChuyen'];
  const ACC2_VIDEOS = ['V4_B5_Nhom1_TocDo_VanToc', 'V5_B5_Nhom1_TongHop_VanToc', 'V6_B5_Nhom2_TocDo_VanToc', 'V7_B5_Nhom2_TongHop_VanToc'];

  const STORAGE_KEY = 'google_flow_7videos_status';
  const FILTER_KEY = 'google_flow_account_filter';

  let currentFilter = 'all';
  try {{
    const savedFilter = localStorage.getItem(FILTER_KEY);
    if (savedFilter && ['all', 'acc_1', 'acc_2'].includes(savedFilter)) {{
      currentFilter = savedFilter;
    }}
  }} catch(e) {{}}

  let checkedStatus = {{}};
  try {{
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) checkedStatus = JSON.parse(saved);
  }} catch(e) {{}}

  function switchTab(videoId, btn) {{
    document.querySelectorAll('.video-panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    
    const targetPanel = document.getElementById('panel-' + videoId);
    if (targetPanel) targetPanel.classList.add('active');
    if (btn) btn.classList.add('active');
  }}

  function toggleSceneDone(vid, sceneIdx, isChecked) {{
    const key = vid + '_s' + sceneIdx;
    checkedStatus[key] = isChecked;
    try {{
      localStorage.setItem(STORAGE_KEY, JSON.stringify(checkedStatus));
    }} catch(e) {{}}

    const card = document.getElementById('card_' + vid + '_s' + sceneIdx);
    if (card) {{
      if (isChecked) card.classList.add('completed');
      else card.classList.remove('completed');
    }}
    updateBudgetStats();
  }}

  function setAccountFilter(filter) {{
    currentFilter = filter;
    try {{
      localStorage.setItem(FILTER_KEY, filter);
    }} catch(e) {{}}

    document.querySelectorAll('.acc-tab-btn').forEach(b => b.classList.remove('active'));
    if (filter === 'all') document.getElementById('btn-filter-all').classList.add('active');
    if (filter === 'acc_1') document.getElementById('btn-filter-acc1').classList.add('active');
    if (filter === 'acc_2') document.getElementById('btn-filter-acc2').classList.add('active');

    updateBudgetStats();
  }}

  function updateBudgetStats() {{
    let totalTargetClips = TOTAL_CLIPS;
    let capCredits = 2000;
    let titleText = 'TIẾN ĐỘ TỔNG HỢP (2 TÀI KHOẢN PRO)';
    let reserveCredits = 1040;

    let completedCount = 0;

    for (const k in checkedStatus) {{
      if (!checkedStatus[k]) continue;
      const vid = k.split('_s')[0];
      if (currentFilter === 'all') {{
        completedCount++;
      }} else if (currentFilter === 'acc_1' && ACC1_VIDEOS.includes(vid)) {{
        completedCount++;
      }} else if (currentFilter === 'acc_2' && ACC2_VIDEOS.includes(vid)) {{
        completedCount++;
      }}
    }}

    if (currentFilter === 'all') {{
      totalTargetClips = TOTAL_CLIPS;
      capCredits = 2000;
      titleText = 'TIẾN ĐỘ TỔNG HỢP (2 TÀI KHOẢN PRO)';
      reserveCredits = 1040;
    }} else if (currentFilter === 'acc_1') {{
      totalTargetClips = ACC1_CLIPS;
      capCredits = 1000;
      titleText = 'TÀI KHOẢN 1: BÀI 4 (V1, V2, V3)';
      reserveCredits = 460;
    }} else if (currentFilter === 'acc_2') {{
      totalTargetClips = ACC2_CLIPS;
      capCredits = 1000;
      titleText = 'TÀI KHOẢN 2: BÀI 5 (V4, V5, V6, V7)';
      reserveCredits = 580;
    }}

    const usedCredits = completedCount * CREDIT_PER_CLIP;
    const remainingCredits = capCredits - usedCredits;
    const pct = totalTargetClips > 0 ? Math.round((completedCount / totalTargetClips) * 100) : 0;

    document.getElementById('filter-title').innerText = titleText;
    document.getElementById('stat-completed').innerText = completedCount;
    document.getElementById('stat-total-clips').innerText = totalTargetClips;
    document.getElementById('stat-credits').innerText = usedCredits;
    document.getElementById('stat-remaining').innerText = remainingCredits;
    document.getElementById('stat-cap').innerText = capCredits;
    document.getElementById('stat-reserve').innerText = reserveCredits + ' cr';
    document.getElementById('progress-bar').style.width = pct + '%';
  }}

  function copyOmniPrompt(btn) {{
    const text = btn.getAttribute('data-prompt');
    navigator.clipboard.writeText(text).then(() => {{
      showToast('✨ Đã copy Omni Prompt (Video + Lời thoại)! Dán vào Omni 1.2/1.1 để AI tự động nhép miệng và phát âm tiếng Việt.');
    }}).catch(() => {{
      fallbackCopy(text);
    }});
  }}

  function copyDialogue(btn) {{
    const text = btn.getAttribute('data-dialogue');
    navigator.clipboard.writeText(text).then(() => {{
      showToast('🎙️ Đã copy Lời thoại tiếng Việt riêng! Dán vào ô Dialogue/Speech trên giao diện Google Flow.');
    }}).catch(() => {{
      fallbackCopy(text);
    }});
  }}

  function copyKfPrompt(btn) {{
    const text = btn.getAttribute('data-prompt');
    navigator.clipboard.writeText(text).then(() => {{
      showToast('Đã copy Keyframe Prompt! Hãy dán vào Imagen / Midjourney để tạo ảnh mốc.');
    }}).catch(() => {{
      fallbackCopy(text);
    }});
  }}

  function copyFlowPrompt(btn) {{
    const text = btn.getAttribute('data-prompt');
    navigator.clipboard.writeText(text).then(() => {{
      showToast('Đã copy Flow Prompt! Hãy chọn Veo 3.1 Fast, tải ảnh Keyframe lên và dán prompt.');
    }}).catch(() => {{
      fallbackCopy(text);
    }});
  }}

  function copyBrollPrompt(btn) {{
    const text = btn.getAttribute('data-prompt');
    navigator.clipboard.writeText(text).then(() => {{
      showToast('Đã copy B-Roll Prompt! Tận dụng thêm 20 credits để sinh góc máy điện ảnh thứ hai.');
    }}).catch(() => {{
      fallbackCopy(text);
    }});
  }}

  function copyText(text) {{
    navigator.clipboard.writeText(text).then(() => {{
      showToast('Đã copy đường dẫn: ' + text);
    }}).catch(() => {{
      fallbackCopy(text);
    }});
  }}

  function fallbackCopy(text) {{
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('Đã copy vào clipboard!');
  }}

  function showToast(msg) {{
    const t = document.getElementById('toast');
    t.innerText = msg;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 3500);
  }}

  // Initialize
  window.addEventListener('DOMContentLoaded', () => {{
    // Set initial filter
    setAccountFilter(currentFilter);

    // Activate first tab by default
    const firstTabBtn = document.querySelector('.tab-btn');
    if (firstTabBtn) {{
      firstTabBtn.click();
    }}

    // Restore checkboxes
    for (const key in checkedStatus) {{
      if (checkedStatus[key]) {{
        const parts = key.split('_s');
        if (parts.length === 2) {{
          const cb = document.getElementById('cb_' + key);
          if (cb) cb.checked = true;
          const card = document.getElementById('card_' + key);
          if (card) card.classList.add('completed');
        }}
      }}
    }}
    updateBudgetStats();
  }});
</script>
</body>
</html>
""")

    full_html = "".join(html_parts)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[SUCCESS] GoogleFlow_Hybrid_7Videos_Kit.html created at: {OUTPUT_HTML} ({len(full_html)} bytes)")

if __name__ == "__main__":
    build_kit()
