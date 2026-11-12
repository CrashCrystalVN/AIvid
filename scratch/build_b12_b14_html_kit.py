import os
import json
import html

WORK_DIR = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid"
PLAN_FILE = os.path.join(WORK_DIR, "master_plan_b12_b14.json")
OUTPUT_HTML = os.path.join(WORK_DIR, "GoogleFlow_B12_B14_Kit.html")

def build_kit():
    with open(PLAN_FILE, "r", encoding="utf-8") as f:
        plan = json.load(f)

    videos = plan.get("videos", [])
    total_clips = sum(len(v.get("scenes", [])) for v in videos)
    total_credits = plan.get("budget_summary", {}).get("total_flow_credits", 200)

    html_parts = []

    # HTML Header & CSS
    html_parts.append("""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Google Flow Studio - Bài 12 & Bài 14 (Vật Lí 10) - 200 Credits</title>
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
    max-width: 820px;
  }

  /* Budget Tracker Card */
  .budget-tracker {
    background: rgba(15, 23, 42, 0.9);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 16px 20px;
    min-width: 440px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
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

  /* Video Selector Tabs */
  .tabs-wrapper {
    margin-bottom: 24px;
  }
  .nav-groups {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
  }
  .tab-btn {
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 12px 22px;
    color: var(--text-secondary);
    font-size: 14.5px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 12px;
    transition: all 0.2s ease;
  }
  .tab-btn:hover {
    background: var(--bg-card);
    color: var(--text-primary);
    border-color: #475569;
  }
  .tab-btn.active.b12 {
    background: linear-gradient(135deg, rgba(2, 132, 199, 0.25) 0%, rgba(37, 99, 235, 0.25) 100%);
    border-color: var(--accent-cyan);
    color: #fff;
    box-shadow: 0 0 15px rgba(56, 189, 248, 0.25);
  }
  .tab-btn.active.b14 {
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.25) 0%, rgba(126, 34, 206, 0.25) 100%);
    border-color: var(--accent-purple);
    color: #fff;
    box-shadow: 0 0 15px rgba(168, 85, 247, 0.25);
  }
  .tab-btn .badge-count {
    background: #1e293b;
    border: 1px solid #334155;
    font-size: 11px;
    padding: 3px 8px;
    border-radius: 6px;
    color: var(--accent-cyan);
  }
  .tab-btn.active.b12 .badge-count {
    background: var(--accent-cyan);
    color: #0b1120;
    border-color: var(--accent-cyan);
    font-weight: 800;
  }
  .tab-btn.active.b14 .badge-count {
    background: var(--accent-purple);
    color: #fff;
    border-color: var(--accent-purple);
    font-weight: 800;
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
    font-weight: 600;
  }
  .v-badge.target-b12 {
    background: rgba(56, 189, 248, 0.15);
    border-color: #38bdf8;
    color: #38bdf8;
  }
  .v-badge.target-b14 {
    background: rgba(168, 85, 247, 0.15);
    border-color: #a855f7;
    color: #d8b4fe;
  }
  .v-badge.kf-stat {
    background: rgba(16, 185, 129, 0.1);
    border-color: rgba(16, 185, 129, 0.3);
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

  /* Buttons */
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

  .prompts-container {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .prompt-box {
    background: #090e1a;
    border: 1px solid #1e293b;
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 13px;
    color: #cbd5e1;
    position: relative;
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
    font-size: 11px;
    font-weight: 800;
    color: #c084fc;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: inline-flex;
    align-items: center;
    gap: 5px;
  }
  .badge-veo {
    font-size: 11px;
    font-weight: 800;
    color: #f59e0b;
    text-transform: uppercase;
  }
  .badge-kf {
    font-size: 11px;
    font-weight: 800;
    color: #38bdf8;
    text-transform: uppercase;
  }
  .omni-dialogue-highlight {
    background: rgba(124, 58, 237, 0.18);
    border: 1px dashed rgba(192, 132, 252, 0.45);
    border-radius: 6px;
    padding: 8px 12px;
    margin: 8px 0;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .omni-dialogue-tag {
    font-size: 10.5px;
    font-weight: 800;
    color: #d8b4fe;
    text-transform: uppercase;
  }
  .omni-dialogue-text {
    font-size: 13.5px;
    color: #fdf4ff;
    font-style: italic;
    font-weight: 500;
    line-height: 1.5;
  }
  .prompt-content-text {
    line-height: 1.5;
    word-break: break-word;
    font-family: monospace;
    font-size: 12.5px;
    color: #94a3b8;
  }
  .prompt-content-text.omni-text {
    color: #e2e8f0;
    font-family: inherit;
    font-size: 13px;
  }

  /* HUD elements pills */
  .hud-list {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-top: 8px;
  }
  .hud-item {
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.25);
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 12.5px;
    color: #a7f3d0;
  }

  /* Toast Notification */
  .toast {
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: linear-gradient(135deg, #059669 0%, #10b981 100%);
    color: #fff;
    padding: 12px 24px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 600;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    transform: translateY(100px);
    opacity: 0;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    z-index: 9999;
    display: flex;
    align-items: center;
    gap: 10px;
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
          Google Flow Studio
          <span class="badge-pill">200 Credits Google Flow</span>
          <span class="badge-omni-pill">Omni 1.2 Lip-Sync Ready</span>
        </h1>
        <p>Hệ thống kịch bản, keyframe sạch 16:9, prompt Omni / Veo 3.1 Fast và thông số kỹ thuật cho Bài 12 (Chuyển động ném) &amp; Bài 14 (Định luật 1 Newton) theo chuẩn SGK Vật Lí 10 Kết Nối Tri Thức.</p>
      </div>
      <div class="budget-tracker">
        <div class="budget-title">
          <span>Tiến độ tạo clips: <strong id="clip-count">0/10</strong> clips</span>
          <span class="cr-val"><span id="credits-spent">0</span>/200 Credits</span>
        </div>
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" id="progress-bar"></div>
        </div>
        <div class="budget-details">
          <span>Chi phí: <strong>20 cr / clip</strong></span>
          <span>Bài 12: <strong>5 clips (100 cr)</strong></span>
          <span>Bài 14: <strong>5 clips (100 cr)</strong></span>
          <span style="color: #38bdf8;">Hạn mức: <strong>200 Credits</strong></span>
        </div>
      </div>
    </div>
  </header>

  <!-- NAVIGATION TABS -->
  <div class="tabs-wrapper">
    <div class="nav-groups">
      <button class="tab-btn active b12" onclick="switchVideo('V8_B12_ChuyenDongNem', this)">
        <span>🪐 Bài 12: Chuyển động ném</span>
        <span class="badge-count">5 clips • 100 cr</span>
      </button>
      <button class="tab-btn b14" onclick="switchVideo('V9_B14_DinhLuat1Newton', this)">
        <span>🍎 Bài 14: Định luật 1 Newton</span>
        <span class="badge-count">5 clips • 100 cr</span>
      </button>
    </div>
  </div>
""")

    # VIDEO PANELS
    for idx, vid in enumerate(videos):
        vid_id = vid["video_id"]
        v_title = vid["title"]
        v_lesson = vid["lesson"]
        scenes = vid.get("scenes", [])
        is_active = "active" if idx == 0 else ""
        target_badge = "target-b12" if "B12" in vid_id else "target-b14"
        lesson_code = "B12" if "B12" in vid_id else "B14"

        html_parts.append(f"""
  <!-- VIDEO PANEL: {vid_id} -->
  <div class="video-panel {is_active}" id="panel-{vid_id}">
    <div class="video-info-box">
      <div class="v-title-area">
        <h2>{html.escape(v_title)}</h2>
        <p>{html.escape(v_lesson)} • Người dẫn dắt: Cô Cẩm Nhung (Presenter) • Chuẩn 16:9 (1376x768)</p>
      </div>
      <div class="v-meta-badges">
        <span class="v-badge {target_badge}">⚡ Ngân sách: {len(scenes) * 20} Credits (5 scenes)</span>
        <span class="v-badge kf-stat">🎨 5/5 Keyframes Sạch 100%</span>
        <span class="v-badge">✨ 1-Click Omni Lip-Sync</span>
      </div>
    </div>

    <div class="scenes-container">
""")

        for sc in scenes:
            s_idx = sc["scene_idx"]
            s_id = sc["scene_id"]
            s_title = sc["title"]
            dur = sc.get("duration_sec", 15.0)
            kf_path = sc.get("keyframe_path", "")
            flow_path = sc.get("flow_clip_path", "")
            vo_text = sc.get("voiceover", "")
            kf_prompt = sc.get("keyframe_prompt", "")
            flow_prompt = sc.get("flow_i2v_prompt", "")
            omni_prompt = sc.get("omni_prompt", "")
            hud_elements = sc.get("hud_elements", [])

            html_parts.append(f"""
      <!-- SCENE CARD: {s_id} -->
      <div class="scene-card" id="card-{s_id}">
        <div class="scene-header">
          <div class="scene-header-left">
            <span class="scene-num-badge">Cảnh {s_idx}</span>
            <span class="scene-title">{html.escape(s_title)}</span>
          </div>
          <label class="scene-check-toggle">
            <input type="checkbox" id="chk-{s_id}" onchange="toggleSceneCheck('{s_id}', this)">
            <span>Đã tạo trên Google Flow</span>
          </label>
        </div>

        <div class="scene-body">
          <!-- LEFT COLUMN: Keyframe & File Info -->
          <div class="scene-left">
            <div class="keyframe-box">
              <img src="{kf_path}" alt="{s_id} Keyframe" onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'400\\' height=\\'225\\'><rect width=\\'100%\\' height=\\'100%\\' fill=\\'%231e293b\\'/><text x=\\'50%\\' y=\\'50%\\' fill=\\'%2394a3b8\\' text-anchor=\\'middle\\'>{s_id} Keyframe</text></svg>';">
              <span class="keyframe-badge">1376x768 • Clean 16:9</span>
            </div>

            <div class="file-target-tag">
              <span>Đích: <code>{flow_path}</code></span>
              <button class="btn-mini-copy" onclick="copyText('{flow_path}', 'Đã copy đường dẫn file video clip!')">Copy Path</button>
            </div>

            <button class="btn-copy-kf" style="width: 100%; justify-content: center;" onclick="copyText(`{html.escape(kf_prompt)}`, 'Đã copy Keyframe Prompt sạch!')">
              🖼️ Copy Keyframe Prompt
            </button>
          </div>

          <!-- RIGHT COLUMN: Lời thoại SGK, Omni Prompt, Flow Prompt, HUD -->
          <div class="scene-right">
            <!-- Lời thoại SGK -->
            <div class="content-section">
              <div class="content-header">
                <span class="section-label vo">🎙️ Lời Thoại Thuyết Minh SGK ({dur}s)</span>
                <div class="prompt-btn-group">
                  <button class="btn-copy-dialogue" onclick="copyText(`{html.escape(vo_text)}`, 'Đã copy nguyên văn lời thoại SGK!')">
                    📋 Copy Lời Thoại
                  </button>
                </div>
              </div>
              <p class="voiceover-p">"{html.escape(vo_text)}"</p>
            </div>

            <!-- Prompts Section -->
            <div class="prompts-container">
              <!-- Omni 1.2 Lip-Sync Box -->
              <div class="prompt-box omni-box">
                <div class="content-header">
                  <span class="badge-omni">🎙️ Google Flow / Omni 1.2 &amp; 1.1 (Video + Lời Thoại Tiếng Việt Lip-Sync)</span>
                  <button class="btn-copy-omni" onclick="copyText(`{html.escape(omni_prompt)}`, '✨ Đã copy Omni Prompt (Video + Lời thoại Lip-Sync)! Dán vào Google Flow / Omni để AI tạo video nhép miệng tiếng Việt.')">
                    ✨ 1-Click Copy Omni Prompt
                  </button>
                </div>
                <div class="omni-dialogue-highlight">
                  <span class="omni-dialogue-tag">Lời thoại lồng ghép:</span>
                  <span class="omni-dialogue-text">"{html.escape(vo_text)}"</span>
                </div>
                <div class="prompt-content-text omni-text">
                  {html.escape(omni_prompt)}
                </div>
              </div>

              <!-- Veo 3.1 Fast Box -->
              <div class="prompt-box">
                <div class="content-header">
                  <span class="badge-veo">⚡ Google Flow / Veo 3.1 Fast (I2V / T2V Prompt - 20 cr)</span>
                  <button class="btn-copy-prompt" onclick="copyText(`{html.escape(flow_prompt)}`, '⚡ Đã copy Veo 3.1 Fast Prompt!')">
                    ⚡ Copy Veo Prompt (20 cr)
                  </button>
                </div>
                <div class="prompt-content-text">{html.escape(flow_prompt)}</div>
              </div>
            </div>

            <!-- Hologram HUD Elements -->
            <div class="content-section">
              <span class="section-label hud">📐 Hologram HUD Sẽ Chiếu Vào Negative Space (Python HUD Engine)</span>
              <div class="hud-list">
""")

            for elem in hud_elements:
                html_parts.append(f"""                <div class="hud-item">• {html.escape(elem)}</div>""")

            html_parts.append("""              </div>
            </div>
          </div>
        </div>
      </div>
""")

        html_parts.append("""    </div>
  </div>
""")

    # Footer and JavaScript
    html_parts.append("""
</div>

<!-- TOAST NOTIFICATION -->
<div class="toast" id="toast">Thông báo</div>

<script>
  function switchVideo(vidId, btn) {
    document.querySelectorAll('.video-panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => {
      b.classList.remove('active');
      b.classList.remove('b12');
      b.classList.remove('b14');
    });
    
    document.getElementById('panel-' + vidId).classList.add('active');
    btn.classList.add('active');
    if (vidId.includes('B12')) {
      btn.classList.add('b12');
    } else {
      btn.classList.add('b14');
    }
  }

  function copyText(text, successMsg) {
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(() => {
        showToast(successMsg || 'Đã sao chép vào bộ nhớ đệm!');
      }).catch(err => {
        fallbackCopy(text, successMsg);
      });
    } else {
      fallbackCopy(text, successMsg);
    }
  }

  function fallbackCopy(text, successMsg) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.left = '-9999px';
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand('copy');
      showToast(successMsg || 'Đã sao chép vào bộ nhớ đệm!');
    } catch (e) {
      alert('Không thể tự động copy. Vui lòng chọn và copy thủ công.');
    }
    document.body.removeChild(ta);
  }

  function showToast(msg) {
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.add('show');
    setTimeout(() => {
      t.classList.remove('show');
    }, 3200);
  }

  function toggleSceneCheck(sceneId, chk) {
    const card = document.getElementById('card-' + sceneId);
    if (chk.checked) {
      card.classList.add('completed');
      localStorage.setItem('flow_b12_b14_' + sceneId, '1');
    } else {
      card.classList.remove('completed');
      localStorage.removeItem('flow_b12_b14_' + sceneId);
    }
    updateProgress();
  }

  function updateProgress() {
    const allChecks = document.querySelectorAll('input[type="checkbox"]');
    let completed = 0;
    allChecks.forEach(c => {
      if (c.checked) completed++;
    });
    const total = allChecks.length;
    const creditsSpent = completed * 20;
    const pct = total > 0 ? (completed / total) * 100 : 0;

    document.getElementById('clip-count').textContent = completed + '/' + total;
    document.getElementById('credits-spent').textContent = creditsSpent;
    document.getElementById('progress-bar').style.width = pct + '%';
  }

  // Restore state on load
  window.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('input[type="checkbox"]').forEach(chk => {
      const sceneId = chk.id.replace('chk-', '');
      if (localStorage.getItem('flow_b12_b14_' + sceneId) === '1') {
        chk.checked = true;
        document.getElementById('card-' + sceneId).classList.add('completed');
      }
    });
    updateProgress();
  });
</script>
</body>
</html>
""")

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write("".join(html_parts))

    print(f"Kit built successfully at: {OUTPUT_HTML}")
    print(f"File size: {os.path.getsize(OUTPUT_HTML):,} bytes")

if __name__ == "__main__":
    build_kit()
