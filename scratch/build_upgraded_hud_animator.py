import os
import re
import ast

src_path = r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\hud_animator.py"
with open(src_path, "r", encoding="utf-8") as f:
    orig_code = f.read()

# We keep everything before `def render_title_banner`
idx_banner = orig_code.find("def render_title_banner")
idx_mc_badge = orig_code.find("def render_mc_badge")

prefix = orig_code[:idx_banner]
# We also want to check `composite_scene_frame` at the end
idx_composite = orig_code.find("def composite_scene_frame")
middle_mc_to_composite = orig_code[idx_mc_badge:idx_composite]

# New helper and new 7 renderers
new_renderers = '''
# ---------------------------------------------------------------------------
# DYNAMIC LAYOUT & SAFE-ZONE RESOLVER
# ---------------------------------------------------------------------------
def resolve_hud_rect(hud_data: Dict[str, Any], default_rect: Tuple[int, int, int, int], scene_data: Optional[Dict[str, Any]] = None) -> Tuple[int, int, int, int]:
    """
    Resolves HUD panel bounding box (x0, y0, x1, y1) based on layout parameters.
    Supports:
      - 'rect' or 'box' in hud_data or scene_data: [x0, y0, x1, y1]
      - 'layout' in hud_data or scene_data:
          * 'left_side': [60, 120, 760, 870] (lowered to y0=120 to avoid top-left badge)
          * 'lower_third': [80, 715, 1840, 880] (sits above y=900 subtitles)
          * [x0, y0, x1, y1] (custom 4-element list/tuple)
      - 'safe_x0', 'safe_x1', 'safe_y0', 'safe_y1' partial overrides
      - default_rect if no custom layout is specified (guaranteeing 100% backward compatibility)
    """
    x0, y0, x1, y1 = default_rect

    custom_rect = (
        hud_data.get("rect")
        or hud_data.get("box")
        or hud_data.get("hud_rect")
        or (scene_data.get("rect") if scene_data else None)
        or (scene_data.get("box") if scene_data else None)
    )
    if isinstance(custom_rect, (list, tuple)) and len(custom_rect) == 4:
        x0, y0, x1, y1 = int(custom_rect[0]), int(custom_rect[1]), int(custom_rect[2]), int(custom_rect[3])
    else:
        layout = (
            hud_data.get("layout")
            or hud_data.get("hud_layout")
            or (scene_data.get("layout") if scene_data else None)
            or (scene_data.get("hud_layout") if scene_data else None)
        )
        if isinstance(layout, (list, tuple)) and len(layout) == 4:
            x0, y0, x1, y1 = int(layout[0]), int(layout[1]), int(layout[2]), int(layout[3])
        elif layout == "left_side":
            x0, y0, x1, y1 = 60, 120, 760, 870
        elif layout == "lower_third":
            x0, y0, x1, y1 = 80, 715, 1840, 880

    if "safe_x0" in hud_data and hud_data["safe_x0"] is not None:
        x0 = int(hud_data["safe_x0"])
    if "safe_x1" in hud_data and hud_data["safe_x1"] is not None:
        x1 = int(hud_data["safe_x1"])
    if "safe_y0" in hud_data and hud_data["safe_y0"] is not None:
        y0 = int(hud_data["safe_y0"])
    if "safe_y1" in hud_data and hud_data["safe_y1"] is not None:
        y1 = int(hud_data["safe_y1"])

    return (x0, y0, x1, y1)


def render_title_banner(overlay: Image.Image, hud_data: Dict[str, Any], progress: float):
    """
    Renders HUD Type: title_banner
    Adaptive layout supporting custom [x0, y0, x1, y1], lower_third, left_side, and solid_card.
    Guaranteed backward compatible: defaults to right-side area (1040..1860).
    """
    draw = ImageDraw.Draw(overlay, "RGBA")
    e_p = ease_out_cubic(progress)

    banner_title = sanitize_hud_text(hud_data.get("banner_title", "BÀI HỌC VẬT LÍ 10"))
    badge_text = sanitize_hud_text(hud_data.get("badge", "VẬT LÍ 10 - KNTT"))
    subtitle = sanitize_hud_text(hud_data.get("subtitle", ""))
    presenters = sanitize_hud_text(hud_data.get("presenters", ""))

    slide_x = int((1.0 - e_p) * 40)
    alpha_mul = e_p

    # Presenters & Group info cleaning (100% clean, NO "MC" prefix, NO old names)
    clean_pres = ""
    if presenters:
        clean_pres = re.sub(r"\\bMC\\s*:\\s*", "", presenters, flags=re.IGNORECASE).strip()
        clean_pres = re.sub(r"\\bMC\\s+", "", clean_pres, flags=re.IGNORECASE).strip()
        clean_pres = re.sub(r"\\bMC\\b", "", clean_pres, flags=re.IGNORECASE).strip()
        for mc_name in ["Anh Thư", "Hữu Trọng", "Tú Châu", "Minh Dũng", "Hoàng Nam", "Cẩm Nhung", "Bảo Hân", "Bảo Yến"]:
            clean_pres = clean_pres.replace(mc_name, "").strip()
        if re.match(r"^Nhóm(\\s*\\d*)?:\\s*$", clean_pres, flags=re.IGNORECASE) or not clean_pres:
            clean_pres = ""

    has_presenters = bool(clean_pres)
    def_by1 = 430 if has_presenters else 330
    def_rect = (1040, 130, 1860, def_by1)
    rx0, ry0, rx1, ry1 = resolve_hud_rect(hud_data, def_rect)

    bx0 = rx0 + slide_x
    by0 = ry0
    bx1 = rx1
    by1 = ry1
    bw = bx1 - bx0
    bh = by1 - by0

    is_solid = bool(hud_data.get("solid_card") or hud_data.get("solid"))
    bg_fill = (8, 28, 54, int(255 * alpha_mul)) if is_solid else (8, 28, 54, int(235 * alpha_mul))
    layout_mode = hud_data.get("layout") or hud_data.get("hud_layout")

    # Lower-third horizontal mode
    if layout_mode == "lower_third":
        draw_glass_panel(
            draw,
            (bx0, by0, bx1, by1),
            fill=bg_fill,
            outline=CYAN_GLOW,
            width=2,
            radius=16,
            corner_brackets=True,
            scan_line_p=(progress * 1.8) % 1.0,
            alpha_mul=alpha_mul
        )
        draw_badge(
            draw,
            (bx0 + 24, by0 + 20),
            badge_text,
            FONTS.get(18, "bold"),
            bg_color=BG_PILL_DEEP,
            border_color=AMBER_GLOW,
            text_color=AMBER_LIGHT,
            radius=8,
            icon="diamond"
        )
        draw.text((bx0 + 24, by0 + 60), banner_title, font=FONTS.get(26, "bold"), fill=WHITE)
        if subtitle:
            draw.text((bx0 + 24, by0 + 96), subtitle, font=FONTS.get(20, "bold"), fill=CYAN_LIGHT)
        if clean_pres:
            draw_badge(
                draw,
                (bx0 + 24, by0 + 130),
                clean_pres,
                FONTS.get(16, "bold"),
                bg_color=BG_PILL_DEEP,
                border_color=EMERALD_GLOW,
                text_color=WHITE,
                radius=6,
                icon="dot"
            )
        draw.text((bx1 - 210, by0 + 24), "HOLOGRAM HUD // 4K", font=FONTS.get(16, "mono"), fill=TEXT_DIM)
        return

    # Standard / left_side / custom box mode
    badge_y = by0 - 46 if by0 >= 80 else by0 + 14
    badge_sz = 18 if bw >= 700 else (16 if bw >= 550 else 14)
    draw_badge(
        draw,
        (bx0, badge_y),
        badge_text,
        FONTS.get(badge_sz, "bold"),
        bg_color=BG_PILL_DEEP,
        border_color=AMBER_GLOW,
        text_color=AMBER_LIGHT,
        radius=8,
        icon="diamond"
    )

    if bw >= 500:
        draw.text((bx1 - 210, by0 - 36 if by0 >= 80 else by0 + 14), "HOLOGRAM HUD // 4K", font=FONTS.get(14 if bw < 700 else 16, "mono"), fill=TEXT_DIM)

    draw_glass_panel(
        draw,
        (bx0, by0, bx1, by1),
        fill=bg_fill,
        outline=CYAN_GLOW,
        width=2,
        radius=18,
        corner_brackets=True,
        scan_line_p=(progress * 1.8) % 1.0,
        alpha_mul=alpha_mul
    )

    t_font_sz = 30 if bw >= 750 else (26 if bw >= 600 else 22)
    t_font = FONTS.get(t_font_sz, "bold")
    max_t_w = bw - 60
    t_lines = wrap_text(banner_title, t_font, max_t_w)
    line_h = t_font_sz + 6
    cur_content_y = by0 + 24

    for tl in t_lines:
        if cur_content_y + line_h <= by1:
            draw.text((bx0 + 30, cur_content_y), tl, font=t_font, fill=WHITE)
            cur_content_y += line_h

    cur_content_y += 6
    if cur_content_y < by1 - 30:
        draw.line([(bx0 + 30, cur_content_y), (bx1 - 30, cur_content_y)], fill=CYAN_DIM, width=2)
        cur_content_y += 12

    if subtitle:
        sub_font_sz = 21 if bw >= 750 else (18 if bw >= 600 else 15)
        sub_font = FONTS.get(sub_font_sz, "bold")
        sub_lines = wrap_text(subtitle, sub_font, bw - 60)
        sub_line_h = sub_font_sz + 6
        for sl in sub_lines:
            if cur_content_y + sub_line_h <= by1 - 20:
                draw.text((bx0 + 30, cur_content_y), sl, font=sub_font, fill=CYAN_LIGHT)
                cur_content_y += sub_line_h
        cur_content_y += 10

    if has_presenters and cur_content_y + 36 <= by1 - 10:
        pres_font_sz = 18 if bw >= 750 else (16 if bw >= 600 else 14)
        draw_badge(
            draw,
            (bx0 + 30, cur_content_y),
            clean_pres,
            FONTS.get(pres_font_sz, "bold"),
            bg_color=BG_PILL_DEEP,
            border_color=EMERALD_GLOW,
            text_color=WHITE,
            radius=8,
            icon="dot"
        )


def render_hud_boxes(overlay: Image.Image, hud_data: Dict[str, Any], progress: float):
    """
    Renders HUD Type: hud_boxes
    Adaptive multi-card layout with high-contrast pills and deep dark backgrounds.
    Dynamically auto-scales fonts, wraps text, and adapts to custom [x0, y0, x1, y1],
    left_side, and solid_card so text never overflows.
    """
    draw = ImageDraw.Draw(overlay, "RGBA")
    def_rect = (960, 130, 1860, 870)
    rx0, ry0, rx1, ry1 = resolve_hud_rect(hud_data, def_rect)

    panel_x0 = rx0
    panel_x1 = rx1
    by0 = ry0
    by1 = ry1
    bw = panel_x1 - panel_x0
    bh = by1 - by0

    is_solid = bool(hud_data.get("solid_card") or hud_data.get("solid"))
    bg_alpha_base = 255 if is_solid else 235

    cards = []

    title = hud_data.get("title") or hud_data.get("step") or hud_data.get("kayak_rule") or hud_data.get("system")
    if title:
        cards.append(("header", sanitize_hud_text(title), None))

    if "box_1" in hud_data and "box_2" in hud_data:
        b1 = hud_data["box_1"]
        b2 = hud_data["box_2"]
        cards.append(("box", b1.get("title", ""), b1.get("content", "")))
        cards.append(("box_warning", b2.get("title", ""), b2.get("content", "")))
        if "dilemma" in hud_data:
            cards.append(("alert", "KẾT LUẬN QUAN TRỌNG", hud_data["dilemma"]))

    elif "elements" in hud_data:
        for idx, elem in enumerate(hud_data["elements"]):
            cards.append(("item", f"Thành phần {idx+1}", elem))
        if "formula" in hud_data:
            cards.append(("formula", "CÔNG THỨC QUY CHIẾU", hud_data["formula"]))

    elif "condition" in hud_data and "example" in hud_data:
        cards.append(("item", "ĐIỀU KIỆN", hud_data.get("condition", "")))
        cards.append(("item", "VÍ DỤ THỰC TẾ", hud_data.get("example", "")))
        if "rule" in hud_data:
            cards.append(("formula", "QUY TẮC", hud_data.get("rule", "")))

    elif "recap" in hud_data or "key_points" in hud_data:
        items = hud_data.get("recap") or hud_data.get("key_points") or []
        for it in items:
            cards.append(("check", "", it))
        if "next_teaser" in hud_data:
            cards.append(("alert", "TIẾP THEO", hud_data["next_teaser"]))
        elif "thanks" in hud_data:
            cards.append(("alert", "LỜI CẢM ƠN", hud_data["thanks"]))

    elif "calculation" in hud_data or "method" in hud_data:
        if "method" in hud_data:
            cards.append(("item", "PHƯƠNG PHÁP", hud_data["method"]))
        if "calculation" in hud_data:
            cards.append(("formula", "TÍNH TOÁN", hud_data["calculation"]))
        if "formula" in hud_data:
            cards.append(("formula", "CÔNG THỨC ÁP DỤNG", hud_data["formula"]))
        if "direction" in hud_data:
            cards.append(("item", "HƯỚNG VECTƠ", hud_data["direction"]))
        if "note" in hud_data:
            cards.append(("item", "GHI CHÚ", hud_data["note"]))

    elif any(k.startswith("case_") for k in hud_data.keys()):
        for k, v in hud_data.items():
            if k.startswith("case_"):
                cards.append(("item", "TRƯỜNG HỢP", v))
        if "formula" in hud_data:
            cards.append(("formula", "CÔNG THỨC CHUẨN", hud_data["formula"]))

    elif "issue" in hud_data:
        cards.append(("box_warning", hud_data.get("issue", ""), hud_data.get("description", "")))
        cards.append(("formula", hud_data.get("solution", ""), hud_data.get("formula", "")))

    else:
        for k, v in hud_data.items():
            if k not in ["title", "theme_color", "layout", "rect", "box", "solid_card", "solid", "safe_x0", "safe_x1", "safe_y0", "safe_y1", "hud_layout", "presenters"]:
                cards.append(("item", k.upper(), str(v)))

    # Also handle presenters in recap scenes if present
    if "presenters" in hud_data and hud_data["presenters"]:
        pres_str = sanitize_hud_text(hud_data["presenters"])
        pres_clean = re.sub(r"\\bMC\\s*:\\s*", "", pres_str, flags=re.IGNORECASE).strip()
        pres_clean = re.sub(r"\\bMC\\s+", "", pres_clean, flags=re.IGNORECASE).strip()
        pres_clean = re.sub(r"\\bMC\\b", "", pres_clean, flags=re.IGNORECASE).strip()
        for mc_name in ["Anh Thư", "Hữu Trọng", "Tú Châu", "Minh Dũng", "Hoàng Nam", "Cẩm Nhung", "Bảo Hân", "Bảo Yến"]:
            pres_clean = pres_clean.replace(mc_name, "").strip()
        if pres_clean and not re.match(r"^Nhóm(\\s*\\d*)?:\\s*$", pres_clean, flags=re.IGNORECASE):
            cards.append(("item", "NHÓM THỰC HIỆN", pres_clean))

    num_cards = len(cards)
    if num_cards == 0:
        return

    cur_y = by0
    card_spacing = 14 if (num_cards > 3 or bh < 650) else 18

    # Calculate available vertical space and adjust card heights dynamically
    avail_h = bh - (num_cards - 1) * card_spacing
    base_ch = max(52, avail_h // num_cards)

    for c_idx, (c_type, c_title, c_content) in enumerate(cards):
        start_p = c_idx / max(1.0, num_cards + 0.5)
        local_card_p = min(1.0, max(0.0, (progress - start_p) * 2.5))
        if local_card_p <= 0.0:
            continue

        e_cp = ease_out_cubic(local_card_p)
        slide_x = int((1.0 - e_cp) * 40)
        bx0 = panel_x0 + slide_x
        bx1 = panel_x1

        c_title_fmt = sanitize_hud_text(c_title)
        c_content_fmt = sanitize_hud_text(c_content or "")

        alpha = int(bg_alpha_base * e_cp)

        if c_type == "header":
            ch = min(72, max(56, base_ch))
            draw_glass_panel(
                draw,
                (bx0, cur_y, bx1, cur_y + ch),
                fill=(12, 38, 70, alpha),
                outline=CYAN_GLOW,
                width=2,
                radius=14,
                corner_brackets=True,
                scan_line_p=(progress * 2.0) % 1.0,
                alpha_mul=e_cp
            )
            head_sz = 22 if bw >= 750 else (20 if bw >= 600 else 17)
            draw_badge(draw, (bx0 + 20, cur_y + 16), c_title_fmt, FONTS.get(head_sz, "bold"), bg_color=BG_PILL_DEEP, border_color=CYAN_GLOW, text_color=WHITE, icon="diamond")
            cur_y += ch + card_spacing

        elif c_type == "formula":
            # Auto-scale font and wrap formula text
            f_font_sz = 26 if bw >= 750 else (22 if bw >= 600 else 18)
            f_font = FONTS.get(f_font_sz, "bold")
            max_f_w = bw - 50
            f_lines = wrap_text(c_content_fmt, f_font, max_f_w)
            f_line_h = f_font_sz + 4
            ch = max(76, 46 + len(f_lines) * f_line_h)
            if ch > base_ch * 1.5 and base_ch > 60:
                ch = int(base_ch * 1.5)

            draw_glass_panel(
                draw,
                (bx0, cur_y, bx1, cur_y + ch),
                fill=(6, 32, 58, alpha),
                outline=CYAN_GLOW,
                width=2,
                radius=14,
                corner_brackets=True,
                scan_line_p=(progress * 3.0) % 1.0,
                alpha_mul=e_cp
            )
            draw_badge(draw, (bx0 + 24, cur_y + 12), c_title_fmt, FONTS.get(15 if bw < 700 else 16, "bold"), bg_color=BG_PILL_DEEP, border_color=CYAN_GLOW, text_color=CYAN_LIGHT, icon="dot")
            text_y = cur_y + 40
            for fl in f_lines:
                if text_y + f_line_h <= cur_y + ch + 10:
                    draw.text((bx0 + 24, text_y), fl, font=f_font, fill=WHITE)
                    text_y += f_line_h
            cur_y += ch + card_spacing

        elif c_type in ["box_warning", "alert"]:
            a_font_sz = 21 if bw >= 750 else (18 if bw >= 600 else 16)
            a_font = FONTS.get(a_font_sz, "bold")
            a_lines = wrap_text(c_content_fmt, a_font, bw - 50)
            a_line_h = a_font_sz + 4
            ch = max(74, 46 + len(a_lines) * a_line_h)

            draw_glass_panel(
                draw,
                (bx0, cur_y, bx1, cur_y + ch),
                fill=(38, 22, 16, alpha),
                outline=AMBER_GLOW,
                width=2,
                radius=14,
                corner_brackets=True,
                alpha_mul=e_cp
            )
            draw_badge(draw, (bx0 + 24, cur_y + 12), c_title_fmt, FONTS.get(15 if bw < 700 else 16, "bold"), bg_color=(45, 24, 12, 240), border_color=AMBER_GLOW, text_color=AMBER_LIGHT, icon="diamond")
            text_y = cur_y + 40
            for al in a_lines:
                if text_y + a_line_h <= cur_y + ch + 10:
                    draw.text((bx0 + 24, text_y), al, font=a_font, fill=AMBER_LIGHT)
                    text_y += a_line_h
            cur_y += ch + card_spacing

        elif c_type == "check":
            ck_font_sz = 20 if bw >= 750 else (17 if bw >= 600 else 15)
            ck_font = FONTS.get(ck_font_sz, "bold")
            ck_lines = wrap_text(c_content_fmt, ck_font, bw - 85)
            ck_line_h = ck_font_sz + 4
            ch = max(58, 26 + len(ck_lines) * ck_line_h)

            draw_glass_panel(
                draw,
                (bx0, cur_y, bx1, cur_y + ch),
                fill=(6, 26, 46, alpha),
                outline=EMERALD_GLOW,
                width=1,
                radius=10,
                corner_brackets=False,
                alpha_mul=e_cp
            )
            draw_vector_checkmark(draw, (bx0 + 34, cur_y + ch // 2), radius=11, color=EMERALD_GLOW)
            text_y = cur_y + 16
            for ckl in ck_lines:
                if text_y + ck_line_h <= cur_y + ch + 10:
                    draw.text((bx0 + 64, text_y), ckl, font=ck_font, fill=WHITE)
                    text_y += ck_line_h
            cur_y += ch + 12

        else:
            it_font_sz = 20 if bw >= 750 else (17 if bw >= 600 else 15)
            it_font = FONTS.get(it_font_sz, "bold")
            it_lines = wrap_text(c_content_fmt, it_font, bw - 50)
            it_line_h = it_font_sz + 4
            ch = max(68, 42 + len(it_lines) * it_line_h)

            draw_glass_panel(
                draw,
                (bx0, cur_y, bx1, cur_y + ch),
                fill=(6, 24, 44, alpha),
                outline=CYAN_DIM,
                width=1,
                radius=12,
                corner_brackets=True,
                alpha_mul=e_cp
            )
            if c_title_fmt:
                draw_badge(draw, (bx0 + 20, cur_y + 12), c_title_fmt, FONTS.get(14 if bw < 700 else 15, "bold"), bg_color=BG_PILL_DEEP, border_color=CYAN_DIM, text_color=CYAN_LIGHT, icon="dot")
            text_y = cur_y + (40 if c_title_fmt else 16)
            for itl in it_lines:
                if text_y + it_line_h <= cur_y + ch + 10:
                    draw.text((bx0 + 20, text_y), itl, font=it_font, fill=WHITE)
                    text_y += it_line_h
            cur_y += ch + card_spacing


def render_speed_gauge(overlay: Image.Image, hud_data: Dict[str, Any], progress: float):
    """
    Renders HUD Type: speed_gauge
    High-contrast digital speedometer with live counting numbers and telemetry badges.
    Dynamically scales dial radius, ticks, and telemetry slots based on custom bounding box.
    """
    draw = ImageDraw.Draw(overlay, "RGBA")
    align_left = hud_data.get("align") == "left" or hud_data.get("position") == "left"
    def_rect = (80, 130, 800, 870) if align_left else (1020, 130, 1840, 870)
    rx0, ry0, rx1, ry1 = resolve_hud_rect(hud_data, def_rect)

    gx0, gy0, gx1, gy1 = rx0, ry0, rx1, ry1
    gw = gx1 - gx0
    gh = gy1 - gy0

    is_solid = bool(hud_data.get("solid_card") or hud_data.get("solid"))
    panel_fill = (6, 22, 42, 255) if is_solid else (6, 22, 42, 235)

    draw_glass_panel(
        draw,
        (gx0, gy0, gx1, gy1),
        fill=panel_fill,
        outline=CYAN_GLOW,
        width=2,
        radius=18,
        corner_brackets=True,
        scan_line_p=(progress * 1.5) % 1.0
    )

    gauge_title = sanitize_hud_text(hud_data.get("gauge_title") or hud_data.get("device") or hud_data.get("mode") or "TỐC KẾ SỐ HIỆN ĐẠI")
    speed_raw = hud_data.get("speed") or hud_data.get("speedometer") or hud_data.get("result") or "v = 36 km/h"

    match = re.search(r"(\\d+[\\.,]?\\d*)", speed_raw)
    target_val = float(match.group(1).replace(",", ".")) if match else 36.0
    cur_val = target_val * min(1.0, progress * 1.35)

    badge_sz = 15 if gw < 700 else 16
    draw_badge(draw, (gx0 + 24, gy0 + 20), "LIVE TELEMETRY // 10Hz", FONTS.get(badge_sz, "bold"), bg_color=BG_PILL_DEEP, border_color=EMERALD_GLOW, text_color=EMERALD_LIGHT, icon="dot")
    t_sz = 22 if gw < 700 else 26
    draw.text((gx0 + 24, gy0 + 54), gauge_title, font=FONTS.get(t_sz, "bold"), fill=WHITE)

    cx = (gx0 + gx1) // 2
    cy = gy0 + int(gh * 0.40)
    radius = min(140, int(gw * 0.22), int(gh * 0.22))

    total_ticks = 24
    for i in range(total_ticks + 1):
        deg = 135 + i * (270 / total_ticks)
        rad = math.radians(deg)
        r_inner = radius - (14 if i % 4 == 0 else 8)
        r_outer = radius
        tx1 = int(cx + r_inner * math.cos(rad))
        ty1 = int(cy + r_inner * math.sin(rad))
        tx2 = int(cx + r_outer * math.cos(rad))
        ty2 = int(cy + r_outer * math.sin(rad))
        t_color = CYAN_GLOW if i % 4 == 0 else (0, 140, 180, 160)
        draw.line([(tx1, ty1), (tx2, ty2)], fill=t_color, width=2)

    frac = min(1.0, cur_val / max(50.0, target_val * 1.2))
    arc_ticks = int(total_ticks * frac)
    for i in range(arc_ticks):
        deg = 135 + i * (270 / total_ticks)
        rad = math.radians(deg)
        tx1 = int(cx + (radius - 12) * math.cos(rad))
        ty1 = int(cy + (radius - 12) * math.sin(rad))
        tx2 = int(cx + radius * math.cos(rad))
        ty2 = int(cy + radius * math.sin(rad))
        if i < total_ticks * 0.5:
            c = CYAN_GLOW
        elif i < total_ticks * 0.8:
            c = AMBER_GLOW
        else:
            c = ROSE_GLOW
        draw.line([(tx1, ty1), (tx2, ty2)], fill=c, width=3)

    val_str = f"{cur_val:.1f}" if target_val < 20 else f"{int(cur_val)}"
    readout_sz = min(64, max(36, int(radius * 0.44)))
    v_bbox = FONTS.get(readout_sz, "mono").getbbox(val_str)
    vw = v_bbox[2] - v_bbox[0]
    draw.text((cx - vw // 2, cy - int(readout_sz * 0.7)), val_str, font=FONTS.get(readout_sz, "mono"), fill=WHITE)
    draw.text((cx - 32, cy + int(radius * 0.22)), "KM / H", font=FONTS.get(17 if radius < 120 else 20, "bold"), fill=CYAN_GLOW)

    slots = []
    if "distance" in hud_data:
        slots.append(("QUÃNG ĐƯỜNG (s)", hud_data["distance"]))
    if "time" in hud_data:
        slots.append(("THỜI GIAN (t)", hud_data["time"]))
    if "cadence" in hud_data:
        slots.append(("CADENCE", hud_data["cadence"]))
    if "formula" in hud_data:
        slots.append(("CÔNG THỨC", hud_data["formula"]))
    if "result" in hud_data:
        slots.append(("KẾT QUẢ", hud_data["result"]))
    if "definition" in hud_data:
        slots.append(("ĐỊNH NGHĨA", hud_data["definition"]))

    slot_y = cy + radius + 30
    rem_h = gy1 - slot_y - 15
    if slots and rem_h >= 60:
        num_slots = len(slots)
        sh = min(66, max(46, (rem_h - (num_slots - 1) * 8) // num_slots))
        for s_label, s_val in slots:
            if slot_y + sh <= gy1 - 10:
                draw_glass_panel(
                    draw,
                    (gx0 + 20, slot_y, gx1 - 20, slot_y + sh),
                    fill=(4, 18, 36, 225),
                    outline=CYAN_DIM,
                    width=1,
                    radius=10,
                    corner_brackets=False
                )
                draw.text((gx0 + 36, slot_y + 8), s_label, font=FONTS.get(13 if sh < 55 else 15, "bold"), fill=TEXT_MUTED)
                draw.text((gx0 + 36, slot_y + (26 if sh < 55 else 32)), sanitize_hud_text(s_val), font=FONTS.get(18 if sh < 55 else 21, "bold"), fill=WHITE)
                slot_y += sh + 8


def render_animated_axes(overlay: Image.Image, hud_data: Dict[str, Any], progress: float):
    """
    Renders HUD Type: animated_axes
    Dynamic coordinate axes (1D Ox, 2D Oxy geographic) with clean labels and high contrast.
    Adapts dynamically to custom [x0, y0, x1, y1] and solid_card.
    """
    draw = ImageDraw.Draw(overlay, "RGBA")
    e_p = ease_out_cubic(progress)
    axis_mode = hud_data.get("axis_mode") or ("1D_Ox" if "axis_direction" in hud_data or "axis" in hud_data else "2D_Geographic_Oxy")

    def_rect = (860, 140, 1860, 870)
    rx0, ry0, rx1, ry1 = resolve_hud_rect(hud_data, def_rect)
    cx0, cy0, cx1, cy1 = rx0, ry0, rx1, ry1
    w = cx1 - cx0
    h = cy1 - cy0

    is_solid = bool(hud_data.get("solid_card") or hud_data.get("solid"))
    panel_fill = (6, 20, 38, 255) if is_solid else (6, 20, 38, 230)

    draw_glass_panel(
        draw,
        (cx0, cy0, cx1, cy1),
        fill=panel_fill,
        outline=CYAN_GLOW,
        width=2,
        radius=16,
        corner_brackets=True,
        scan_line_p=(progress * 1.5) % 1.0
    )

    if axis_mode == "1D_Ox":
        draw_badge(draw, (cx0 + 26, cy0 + 22), "HỆ TỌA ĐỘ 1 CHIỀU (1D - Ox)", FONTS.get(16 if w < 750 else 17, "bold"), bg_color=BG_PILL_DEEP, border_color=CYAN_GLOW, text_color=WHITE, icon="diamond")

        y_axis = cy0 + int(h * 0.35)
        x_origin = cx0 + int(w * 0.08)
        total_len = w - int(w * 0.22)
        current_len = total_len * e_p

        draw_glow_arrow(draw, (x_origin, y_axis), (int(x_origin + current_len), y_axis), color=CYAN_GLOW, width=4, head_len=18)
        draw.text((x_origin + total_len + 15, y_axis - 16), "x (+)", font=FONTS.get(24, "bold"), fill=CYAN_LIGHT)
        draw.text((x_origin - 12, y_axis + 18), "O (0m)", font=FONTS.get(20, "bold"), fill=WHITE)

        for i in range(1, 6):
            tx = int(x_origin + (total_len * 0.85 * (i / 5.0)))
            if tx <= x_origin + current_len:
                draw.line([(tx, y_axis - 8), (tx, y_axis + 8)], fill=CYAN_GLOW, width=2)
                draw.text((tx - 16, y_axis + 16), f"+{i*20}m", font=FONTS.get(16, "bold"), fill=TEXT_MUTED)

        car_target_x = int(x_origin + (total_len * 0.85))
        car_x = int(x_origin + (car_target_x - x_origin) * min(1.0, progress * 1.4))
        r_pulse = int(12 + 6 * math.sin(progress * 10))
        draw.ellipse([(car_x - r_pulse, y_axis - r_pulse), (car_x + r_pulse, y_axis + r_pulse)], outline=AMBER_GLOW, width=2)
        draw.ellipse([(car_x - 6, y_axis - 6), (car_x + 6, y_axis + 6)], fill=AMBER_GLOW)
        draw_floating_label(draw, (car_x, y_axis - 35), "Vật chuyển động", FONTS.get(16, "bold"), outline_color=AMBER_GLOW)

        inf_y = cy0 + int(h * 0.52)
        inf_h = cy1 - inf_y - 20
        draw_glass_panel(draw, (cx0 + 24, inf_y, cx1 - 24, inf_y + inf_h), fill=(4, 18, 34, 220), outline=CYAN_DIM, width=1, radius=12, corner_brackets=False)
        line_spacing = min(42, inf_h // 4)
        c_y = inf_y + 16
        draw.text((cx0 + 40, c_y), f"[Trục Ox]: {sanitize_hud_text(hud_data.get('axis', 'Trục Ox'))}", font=FONTS.get(20, "bold"), fill=CYAN_LIGHT)
        c_y += line_spacing
        if "person_forward" in hud_data:
            draw.text((cx0 + 40, c_y), f"• {sanitize_hud_text(hud_data['person_forward'])}", font=FONTS.get(19, "bold"), fill=WHITE)
            c_y += line_spacing
        if "person_backward" in hud_data:
            draw.text((cx0 + 40, c_y), f"• {sanitize_hud_text(hud_data['person_backward'])}", font=FONTS.get(19, "bold"), fill=AMBER_LIGHT)
            c_y += line_spacing
        if "speed_note" in hud_data:
            draw.text((cx0 + 40, c_y), f"-> {sanitize_hud_text(hud_data['speed_note'])}", font=FONTS.get(20, "bold"), fill=EMERALD_LIGHT)

    else:
        draw_badge(draw, (cx0 + 26, cy0 + 22), "HỆ TỌA ĐỘ ĐỊA LÍ (2D - Oxy)", FONTS.get(16 if w < 750 else 17, "bold"), bg_color=BG_PILL_DEEP, border_color=CYAN_GLOW, text_color=WHITE, icon="diamond")

        ox = cx0 + int(w * 0.28)
        oy = cy0 + int(h * 0.52)
        axis_len = int(min(w * 0.22, h * 0.28) * e_p)

        draw.text((ox + axis_len + 10, oy - 10), "ĐÔNG (+x)", font=FONTS.get(15, "bold"), fill=CYAN_LIGHT)
        draw.text((ox - axis_len - 80, oy - 10), "TÂY (-x)", font=FONTS.get(15, "bold"), fill=TEXT_MUTED)
        draw.text((ox - 30, oy - axis_len - 25), "BẮC (+y)", font=FONTS.get(16, "bold"), fill=CYAN_LIGHT)
        draw.text((ox - 30, oy + axis_len + 10), "NAM (-y)", font=FONTS.get(16, "bold"), fill=TEXT_MUTED)

        draw_glow_arrow(draw, (int(ox - axis_len), oy), (int(ox + axis_len), oy), color=CYAN_GLOW, width=3)
        draw_glow_arrow(draw, (ox, int(oy + axis_len)), (ox, int(oy - axis_len)), color=CYAN_GLOW, width=3)

        deg_rad = math.radians(45)
        vec_len = int(axis_len * 0.85 * min(1.0, progress * 1.5))
        ax = int(ox + vec_len * math.cos(deg_rad))
        ay = int(oy - vec_len * math.sin(deg_rad))

        draw_glow_arrow(draw, (ox, oy), (ax, ay), color=AMBER_GLOW, width=4, head_len=16, pulse_p=progress * 3.0)
        draw_floating_label(draw, (ax + 20, ay - 25), "Vectơ OA (20m, 45°)", FONTS.get(16, "bold"), outline_color=AMBER_GLOW)

        draw.arc([(ox - 35, oy - 35), (ox + 35, oy + 35)], start=-45, end=0, fill=AMBER_GLOW, width=2)
        draw.text((ox + 40, oy - 22), "45°", font=FONTS.get(15, "bold"), fill=AMBER_LIGHT)

        rx0 = cx0 + int(w * 0.52)
        draw_glass_panel(draw, (rx0, cy0 + 70, cx1 - 24, cy1 - 30), fill=(4, 18, 34, 220), outline=CYAN_DIM, width=1, radius=12, corner_brackets=True)
        draw.text((rx0 + 20, cy0 + 96), "VỊ TRÍ ĐIỂM A", font=FONTS.get(22, "bold"), fill=WHITE)
        draw.text((rx0 + 20, cy0 + 140), f"- {sanitize_hud_text(hud_data.get('x_axis', 'Ox: Hướng Tây - Đông'))}", font=FONTS.get(17, "bold"), fill=CYAN_LIGHT)
        draw.text((rx0 + 20, cy0 + 180), f"- {sanitize_hud_text(hud_data.get('y_axis', 'Oy: Hướng Nam - Bắc'))}", font=FONTS.get(17, "bold"), fill=CYAN_LIGHT)
        draw.text((rx0 + 20, cy0 + 225), f"- {sanitize_hud_text(hud_data.get('point_A', 'Điểm A (20 m, 45° Đông - Bắc)'))}", font=FONTS.get(18, "bold"), fill=AMBER_GLOW)


def render_animated_vector_road(overlay: Image.Image, hud_data: Dict[str, Any], progress: float):
    """
    Renders HUD Type: animated_vector_road
    Responsive vector physics visualization. Zero overlapping labels!
    Supports Pythagoras right triangle, multi-path, river boat, curved road, and aircraft wind.
    Dynamically adapts layout based on aspect ratio of bounding box.
    """
    draw = ImageDraw.Draw(overlay, "RGBA")
    def_rect = (700, 140, 1840, 870)
    rx0, ry0, rx1, ry1 = resolve_hud_rect(hud_data, def_rect)
    cx0, cy0, cx1, cy1 = rx0, ry0, rx1, ry1
    w = cx1 - cx0
    h = cy1 - cy0

    is_solid = bool(hud_data.get("solid_card") or hud_data.get("solid"))
    panel_fill = (6, 20, 38, 255) if is_solid else (6, 20, 38, 230)

    draw_glass_panel(
        draw,
        (cx0, cy0, cx1, cy1),
        fill=panel_fill,
        outline=CYAN_GLOW,
        width=2,
        radius=16,
        corner_brackets=True,
        scan_line_p=(progress * 1.5) % 1.0
    )

    # 1. Right triangle (Pythagoras V3 s3: d1 = 4km East, d2 = 4km North)
    if "segment_1" in hud_data and "segment_2" in hud_data:
        draw_badge(draw, (cx0 + 26, cy0 + 22), "TỔNG HỢP VECTƠ ĐỘ DỊCH CHUYỂN", FONTS.get(16 if w < 750 else 17, "bold"), bg_color=BG_PILL_DEEP, border_color=CYAN_GLOW, text_color=WHITE, icon="diamond")

        # Stacking mode: side-by-side if w >= 800, else top-bottom
        if w >= 800:
            ax, ay = cx0 + 90, cy0 + int(h * 0.65)
            side_len = min(int(w * 0.28), int(h * 0.45))
            bx, by = ax + side_len, ay
            cx_pt, cy_pt = bx, by - side_len

            rx0 = cx0 + int(w * 0.50)
            panel_box = (rx0, cy0 + 75, cx1 - 24, cy1 - 30)
        else:
            ax, ay = cx0 + 80, cy0 + int(h * 0.38)
            side_len = min(int(w * 0.38), int(h * 0.26))
            bx, by = ax + side_len, ay
            cx_pt, cy_pt = bx, by - side_len

            panel_box = (cx0 + 20, cy0 + int(h * 0.44), cx1 - 20, cy1 - 20)

        # Segment 1: A -> B
        p_ab = min(1.0, progress * 2.2)
        cur_bx = int(ax + (bx - ax) * p_ab)
        draw_glow_arrow(draw, (ax, ay), (cur_bx, by), color=CYAN_GLOW, width=4)
        draw_floating_label(draw, ((ax + bx) // 2, by + 30), "d₁ = 4 km (Đông)", FONTS.get(15 if w < 750 else 17, "bold"), outline_color=CYAN_GLOW)

        # Segment 2: B -> C (North)
        if progress > 0.35:
            p_bc = min(1.0, (progress - 0.35) * 2.2)
            cur_cy = int(by + (cy_pt - by) * p_bc)
            draw_glow_arrow(draw, (bx, by), (bx, cur_cy), color=AMBER_GLOW, width=4)
            draw_floating_label(draw, (bx + 85, (by + cy_pt) // 2), "d₂ = 4 km (Bắc)", FONTS.get(15 if w < 750 else 17, "bold"), outline_color=AMBER_GLOW)
            draw.rectangle([(bx - 16, by - 16), (bx, by)], outline=WHITE, width=2)

        # Hypotenuse vector d: A -> C
        if progress > 0.65:
            p_ac = min(1.0, (progress - 0.65) * 2.5)
            cur_ac_x = int(ax + (cx_pt - ax) * p_ac)
            cur_ac_y = int(ay + (cy_pt - ay) * p_ac)
            draw_glow_arrow(draw, (ax, ay), (cur_ac_x, cur_ac_y), color=EMERALD_GLOW, width=5, pulse_p=progress * 3.0)
            draw_floating_label(draw, ((ax + cx_pt) // 2 - 25, (ay + cy_pt) // 2 - 20), "d = √32 ≈ 5,7 km", FONTS.get(16 if w < 750 else 19, "bold"), outline_color=EMERALD_GLOW)

        draw_glass_panel(draw, panel_box, fill=(4, 18, 34, 220), outline=CYAN_DIM, width=1, radius=12, corner_brackets=True)
        px0, py0 = panel_box[0] + 18, panel_box[1] + 16
        draw.text((px0, py0), "PHƯƠNG PHÁP PYTHAGORAS", font=FONTS.get(19 if w < 750 else 22, "bold"), fill=WHITE)
        py0 += 36
        draw.text((px0, py0), "• s = s₁ + s₂ = 4 + 4 = 8 km", font=FONTS.get(17 if w < 750 else 20, "bold"), fill=AMBER_LIGHT)
        py0 += 32
        draw.text((px0, py0), "• d = √(4² + 4²) ≈ 5,7 km (Đông - Bắc 45°)", font=FONTS.get(17 if w < 750 else 20, "bold"), fill=CYAN_LIGHT)
        py0 += 36
        draw.text((px0, py0), "[Kết luận]: |d| < s do đổi hướng!", font=FONTS.get(16 if w < 750 else 19, "bold"), fill=EMERALD_LIGHT)

    # 2. Multi-path comparison (V2 s4)
    elif "paths" in hud_data:
        draw_badge(draw, (cx0 + 26, cy0 + 22), "PHÂN BIỆT QUÃNG ĐƯỜNG & ĐỘ DỊCH CHUYỂN", FONTS.get(16 if w < 750 else 17, "bold"), bg_color=BG_PILL_DEEP, border_color=CYAN_GLOW, text_color=WHITE, icon="diamond")

        ax, ay = cx0 + 100, cy0 + int(h * 0.45)
        bx, by = cx0 + int(w * 0.45), cy0 + int(h * 0.45)

        draw.arc([(ax, ay - 70), (bx, ay + 70)], start=180, end=0, fill=AMBER_GLOW, width=3)
        draw.arc([(ax, ay - 70), (bx, ay + 70)], start=0, end=180, fill=EMERALD_GLOW, width=3)
        draw_glow_arrow(draw, (ax, ay), (bx, by), color=CYAN_GLOW, width=4, pulse_p=progress * 3.0)
        draw_floating_label(draw, ((ax + bx) // 2, by - 30), "Vectơ d (800m)", FONTS.get(16, "bold"), outline_color=CYAN_GLOW)

        draw.text((ax - 50, ay - 12), "Điểm A", font=FONTS.get(18, "bold"), fill=WHITE)
        draw.text((bx + 15, by - 12), "Điểm B", font=FONTS.get(18, "bold"), fill=WHITE)

        rx0 = cx0 + int(w * 0.50)
        draw_glass_panel(draw, (rx0, cy0 + 75, cx1 - 24, cy1 - 30), fill=(4, 18, 34, 220), outline=CYAN_DIM, width=1, radius=12, corner_brackets=True)
        draw.text((rx0 + 20, cy0 + 100), "SO SÁNH 3 LỘ TRÌNH", font=FONTS.get(22, "bold"), fill=WHITE)
        draw.text((rx0 + 20, cy0 + 145), "- Xe máy: s₁ = 1200 m", font=FONTS.get(19, "bold"), fill=AMBER_LIGHT)
        draw.text((rx0 + 20, cy0 + 185), "- Đi bộ: s₂ = 800 m", font=FONTS.get(19, "bold"), fill=CYAN_LIGHT)
        draw.text((rx0 + 20, cy0 + 225), "- Ô tô: s₃ = 1500 m", font=FONTS.get(19, "bold"), fill=EMERALD_LIGHT)
        draw.text((rx0 + 20, cy0 + 275), "-> Vectơ d₁ = d₂ = d₃ = 800 m", font=FONTS.get(21, "bold"), fill=CYAN_GLOW)
        draw.text((rx0 + 20, cy0 + 315), "Độ dịch chuyển chỉ phụ thuộc vị trí đầu & cuối!", font=FONTS.get(18, "bold"), fill=WHITE)

    # 3. Bike curve trajectory (V6 s3)
    elif "curve_status" in hud_data:
        draw_badge(draw, (cx0 + 26, cy0 + 22), "VẬN TỐC KHI ĐỔI HƯỚNG CHUYỂN ĐỘNG", FONTS.get(16 if w < 750 else 17, "bold"), bg_color=BG_PILL_DEEP, border_color=CYAN_GLOW, text_color=WHITE, icon="diamond")

        ax, ay = cx0 + 80, cy0 + int(h * 0.35)
        curve_r = min(int(w * 0.35), int(h * 0.35))
        draw.arc([(ax, ay - curve_r), (ax + curve_r * 2, ay + curve_r)], start=90, end=180, fill=CYAN_DIM, width=3)

        p_pt = min(1.0, progress * 1.5)
        angle_deg = 180 - p_pt * 90
        rad = math.radians(angle_deg)
        center_x, center_y = ax + curve_r, ay
        px = int(center_x + curve_r * math.cos(rad))
        py = int(center_y - curve_r * math.sin(rad))

        draw.ellipse([(px - 8, py - 8), (px + 8, py + 8)], fill=AMBER_GLOW)
        tan_rad = rad + math.pi / 2
        vx = int(px + 90 * math.cos(tan_rad))
        vy = int(py - 90 * math.sin(tan_rad))
        draw_glow_arrow(draw, (px, py), (vx, vy), color=AMBER_GLOW, width=4)
        draw_floating_label(draw, (vx + 15, vy - 15), "Vectơ v (Tiếp tuyến)", FONTS.get(15, "bold"), outline_color=AMBER_GLOW)

        inf_box = (cx0 + 20, cy0 + int(h * 0.52), cx1 - 20, cy1 - 20)
        draw_glass_panel(draw, inf_box, fill=(4, 18, 34, 220), outline=CYAN_DIM, width=1, radius=12, corner_brackets=True)
        ix0, iy0 = inf_box[0] + 18, inf_box[1] + 16
        draw.text((ix0, iy0), sanitize_hud_text(hud_data.get("curve_status", "XE ĐẠP ÔM CUA")), font=FONTS.get(19 if w < 750 else 22, "bold"), fill=WHITE)
        iy0 += 34
        draw.text((ix0, iy0), f"• {sanitize_hud_text(hud_data.get('speed_value', 'Tốc độ: v = 30 km/h (KHÔNG ĐỔI)'))}", font=FONTS.get(17 if w < 750 else 20, "bold"), fill=CYAN_LIGHT)
        iy0 += 32
        draw.text((ix0, iy0), f"• {sanitize_hud_text(hud_data.get('vector_direction', 'Hướng vectơ: ĐỔI LIÊN TỤC'))}", font=FONTS.get(17 if w < 750 else 20, "bold"), fill=AMBER_LIGHT)
        iy0 += 34
        draw.text((ix0, iy0), f"=> {sanitize_hud_text(hud_data.get('conclusion', 'VẬN TỐC BIẾN ĐỔI!'))}", font=FONTS.get(18 if w < 750 else 22, "bold"), fill=EMERALD_LIGHT)

    # 4. River boat flow / Aircraft crosswind / Relative velocity
    else:
        draw_badge(draw, (cx0 + 26, cy0 + 22), "CÔNG THỨC CỘNG VẬN TỐC", FONTS.get(16 if w < 750 else 17, "bold"), bg_color=BG_PILL_DEEP, border_color=CYAN_GLOW, text_color=WHITE, icon="diamond")

        if w >= 800:
            ox, oy = cx0 + 140, cy0 + int(h * 0.65)
            v12_len, v23_len = min(210, int(h * 0.35)), min(180, int(w * 0.22))
            panel_box = (cx0 + int(w * 0.48), cy0 + 75, cx1 - 24, cy1 - 30)
        else:
            ox, oy = cx0 + 120, cy0 + int(h * 0.38)
            v12_len, v23_len = min(140, int(h * 0.22)), min(140, int(w * 0.28))
            panel_box = (cx0 + 20, cy0 + int(h * 0.44), cx1 - 20, cy1 - 20)

        # Vector v12 (upward)
        draw_glow_arrow(draw, (ox, oy), (ox, oy - v12_len), color=CYAN_GLOW, width=4)
        draw_floating_label(draw, (ox - 90, oy - v12_len // 2), "v₁,₂ (Vật 1)", FONTS.get(14 if w < 750 else 16, "bold"), outline_color=CYAN_GLOW)

        # Vector v23 (rightward)
        draw_glow_arrow(draw, (ox, oy - v12_len), (ox + v23_len, oy - v12_len), color=AMBER_GLOW, width=4)
        draw_floating_label(draw, (ox + v23_len // 2, oy - v12_len - 28), "v₂,₃ (Vật 2)", FONTS.get(14 if w < 750 else 16, "bold"), outline_color=AMBER_GLOW)

        # Vector v13 (Resultant hypotenuse)
        if progress > 0.4:
            draw_glow_arrow(draw, (ox, oy), (ox + v23_len, oy - v12_len), color=EMERALD_GLOW, width=5, pulse_p=progress * 3.0)
            draw_floating_label(draw, (ox + v23_len // 2 + 55, oy - v12_len // 2 + 25), "v₁,₃", FONTS.get(16 if w < 750 else 19, "bold"), outline_color=EMERALD_GLOW)

        draw_glass_panel(draw, panel_box, fill=(4, 18, 34, 220), outline=CYAN_DIM, width=1, radius=12, corner_brackets=True)
        px0, py0 = panel_box[0] + 18, panel_box[1] + 16
        draw.text((px0, py0), "QUY ƯỚC 1 - 2 - 3 CHUẨN", font=FONTS.get(19 if w < 750 else 22, "bold"), fill=WHITE)
        py0 += 34
        draw.text((px0, py0), "• (1) Vật c.động • (2) Hệ Q.C c.động • (3) Đứng yên", font=FONTS.get(15 if w < 750 else 18, "bold"), fill=CYAN_LIGHT)
        py0 += 32
        draw.text((px0, py0), "Vectơ v₁,₃ = Vectơ v₁,₂ + Vectơ v₂,₃", font=FONTS.get(18 if w < 750 else 22, "bold"), fill=AMBER_LIGHT)
        py0 += 34
        if "pythagoras" in hud_data:
            draw.text((px0, py0), f"=> {sanitize_hud_text(hud_data['pythagoras'])}", font=FONTS.get(18 if w < 750 else 22, "bold"), fill=EMERALD_LIGHT)
        elif "action" in hud_data:
            draw.text((px0, py0), f"=> {sanitize_hud_text(hud_data['action'])}", font=FONTS.get(18 if w < 750 else 22, "bold"), fill=EMERALD_LIGHT)
        else:
            draw.text((px0, py0), "=> v₁,₃ = √(v₁₂² + v₂₃²)", font=FONTS.get(18 if w < 750 else 22, "bold"), fill=EMERALD_LIGHT)


def render_comparison_table(overlay: Image.Image, hud_data: Dict[str, Any], progress: float):
    """
    Renders HUD Type: comparison_table
    High contrast Sci-Fi table with rows illuminating sequentially.
    Dynamically auto-scales column widths, row heights, and font sizes to fit custom bounding box.
    """
    draw = ImageDraw.Draw(overlay, "RGBA")
    columns = hud_data.get("columns", ["Tiêu chí", "Quãng đường (s)", "Độ dịch chuyển (d)"])
    rows = hud_data.get("rows", [])

    def_rect = (680, 150, 1840, 870)
    rx0, ry0, rx1, ry1 = resolve_hud_rect(hud_data, def_rect)
    tx0, ty0, tx1, ty1 = rx0, ry0, rx1, ry1
    w = tx1 - tx0
    h = ty1 - ty0

    is_solid = bool(hud_data.get("solid_card") or hud_data.get("solid"))
    panel_fill = (6, 22, 42, 255) if is_solid else (6, 22, 42, 235)

    draw_glass_panel(
        draw,
        (tx0, ty0, tx1, ty1),
        fill=panel_fill,
        outline=CYAN_GLOW,
        width=2,
        radius=16,
        corner_brackets=True,
        scan_line_p=(progress * 1.5) % 1.0
    )

    draw_badge(draw, (tx0 + 26, ty0 + 20), "BẢNG SO SÁNH ĐỐI CHIẾU", FONTS.get(15 if w < 750 else 16, "bold"), bg_color=BG_PILL_DEEP, border_color=CYAN_GLOW, text_color=WHITE, icon="diamond")

    num_cols = len(columns)
    col_w = (w - 40) // max(1, num_cols)
    hy0 = ty0 + 64
    hh = min(56, int(h * 0.12))

    draw.rounded_rectangle([(tx0 + 16, hy0), (tx1 - 16, hy0 + hh)], radius=10, fill=(12, 38, 70, 240), outline=CYAN_DIM, width=1)
    col_font_sz = 17 if col_w < 220 else (19 if col_w < 270 else 22)
    for c_idx, col in enumerate(columns):
        col_x = tx0 + 24 + c_idx * col_w
        color = AMBER_GLOW if c_idx == 1 else (CYAN_GLOW if c_idx == 2 else WHITE)
        draw.text((col_x + 6, hy0 + 14), sanitize_hud_text(col), font=FONTS.get(col_font_sz, "bold"), fill=color)

    row_y = hy0 + hh + 12
    num_rows = len(rows)
    rem_h = ty1 - row_y - 20
    row_h = min(92, max(50, (rem_h - (num_rows - 1) * 12) // max(1, num_rows)))
    row_font_sz = 15 if col_w < 220 else (17 if col_w < 270 else 20)

    for r_idx, row in enumerate(rows):
        start_p = r_idx / max(1.0, num_rows + 0.3)
        row_p = min(1.0, max(0.0, (progress - start_p) * 2.5))
        if row_p <= 0.0:
            continue

        e_rp = ease_out_cubic(row_p)
        alpha = int(240 * e_rp) if is_solid else int(230 * e_rp)

        row_fill = (8, 28, 52, alpha) if r_idx % 2 == 0 else (4, 18, 36, alpha)
        row_outline = CYAN_GLOW if r_idx == 0 else CYAN_DIM
        draw.rounded_rectangle([(tx0 + 16, row_y), (tx1 - 16, row_y + row_h)], radius=10, fill=row_fill, outline=row_outline, width=1)

        for c_idx, val in enumerate(row):
            col_x = tx0 + 24 + c_idx * col_w
            c_text = sanitize_hud_text(val)
            t_color = AMBER_LIGHT if c_idx == 1 else (CYAN_LIGHT if c_idx == 2 else WHITE)
            r_lines = wrap_text(c_text, FONTS.get(row_font_sz, "bold"), col_w - 16)
            rl_h = row_font_sz + 4
            text_start_y = row_y + max(8, (row_h - len(r_lines) * rl_h) // 2)
            for li, line_t in enumerate(r_lines):
                if text_start_y + li * rl_h <= row_y + row_h - 4:
                    draw.text((col_x + 6, text_start_y + li * rl_h), line_t, font=FONTS.get(row_font_sz, "bold"), fill=t_color)

        row_y += row_h + 12


def render_quiz_popup(overlay: Image.Image, hud_data: Dict[str, Any], progress: float):
    """
    Renders HUD Type: quiz_popup
    Interactive Sci-Fi quiz popup with glowing emerald answer reveal and vector checkmark.
    Dynamically auto-scales to constrained bounding boxes (e.g. lower area below flying drone in V6 s5).
    """
    draw = ImageDraw.Draw(overlay, "RGBA")
    question = sanitize_hud_text(hud_data.get("question", "Câu hỏi tương tác"))
    options = hud_data.get("options", ["A. Đáp án 1", "B. Đáp án 2", "C. Đáp án 3"])
    correct = hud_data.get("correct_answer", "B")
    hint_or_exp = sanitize_hud_text(hud_data.get("explanation") or hud_data.get("hint") or "")

    def_rect = (1040, 140, 1860, 870)
    rx0, ry0, rx1, ry1 = resolve_hud_rect(hud_data, def_rect)
    qx0, qy0, qx1, qy1 = rx0, ry0, rx1, ry1
    w = qx1 - qx0
    h = qy1 - qy0

    is_solid = bool(hud_data.get("solid_card") or hud_data.get("solid"))
    panel_fill = (8, 24, 46, 255) if is_solid else (8, 24, 46, 235)

    pulse = 0.5 + 0.5 * math.sin(progress * 8.0)
    border_color = (int(AMBER_GLOW[0] * (0.8 + 0.2 * pulse)), int(AMBER_GLOW[1] * (0.8 + 0.2 * pulse)), AMBER_GLOW[2])

    draw_glass_panel(
        draw,
        (qx0, qy0, qx1, qy1),
        fill=panel_fill,
        outline=border_color,
        width=3,
        radius=18,
        corner_brackets=True,
        scan_line_p=(progress * 1.5) % 1.0
    )

    badge_sz = 15 if (w < 750 or h < 500) else 18
    draw_badge(
        draw,
        (qx0 + 26, qy0 + 18),
        "CÂU HỎI TƯƠNG TÁC",
        FONTS.get(badge_sz, "bold"),
        bg_color=BG_PILL_DEEP,
        border_color=AMBER_GLOW,
        text_color=AMBER_LIGHT,
        radius=10,
        icon="diamond"
    )

    # Dynamic question wrapping and scaling
    q_font_sz = 20 if (w < 750 or h < 500) else 23
    q_font = FONTS.get(q_font_sz, "bold")
    max_q_w = (qx1 - 30) - (qx0 + 30)
    q_lines = wrap_text(question, q_font, max_q_w)
    line_h = q_font_sz + 6
    q_start_y = qy0 + (54 if h < 500 else 72)
    for line_idx, line in enumerate(q_lines):
        draw.text((qx0 + 26, q_start_y + line_idx * line_h), line, font=q_font, fill=WHITE)

    q_bottom = q_start_y + len(q_lines) * line_h
    opt_y = q_bottom + (10 if h < 500 else 16)
    is_revealed = progress >= 0.65

    rem_h = qy1 - opt_y - 14
    num_opts = len(options)
    # Reserve space for explanation if revealed and height permits
    show_exp = is_revealed and bool(hint_or_exp) and rem_h >= 240
    exp_h_reserved = 80 if show_exp else 0

    opt_h = min(74, max(38, (rem_h - exp_h_reserved - (num_opts - 1) * 8) // max(1, num_opts)))
    opt_font_sz = 16 if (opt_h < 48 or w < 750) else (18 if opt_h < 60 else 20)
    opt_font = FONTS.get(opt_font_sz, "bold")

    for opt_text in options:
        opt_fmt = sanitize_hud_text(opt_text)
        is_this_correct = opt_text.strip().startswith(correct)

        if is_revealed and is_this_correct:
            card_fill = EMERALD_BG
            card_outline = EMERALD_GLOW
            card_width = 3
            text_color = WHITE
            show_check = True
        else:
            card_fill = (4, 18, 36, 225)
            card_outline = CYAN_DIM
            card_width = 1
            text_color = WHITE
            show_check = False

        draw_glass_panel(
            draw,
            (qx0 + 24, opt_y, qx1 - 24, opt_y + opt_h),
            fill=card_fill,
            outline=card_outline,
            width=card_width,
            radius=10,
            corner_brackets=False
        )

        draw.text((qx0 + 40, opt_y + max(6, (opt_h - opt_font_sz) // 2)), opt_fmt, font=opt_font, fill=text_color)
        if show_check:
            check_x = qx1 - 100
            draw_vector_checkmark(draw, (check_x, opt_y + opt_h // 2), radius=min(14, opt_h // 3), color=EMERALD_GLOW)
            draw.text((check_x + 22, opt_y + max(6, (opt_h - 18) // 2)), "ĐÚNG", font=FONTS.get(16, "bold"), fill=EMERALD_GLOW)

        opt_y += opt_h + (8 if h < 500 else 12)

    if show_exp:
        exp_p = min(1.0, (progress - 0.65) * 3.0)
        e_exp = ease_out_cubic(exp_p)
        exp_y = opt_y + 4
        exp_h = min(85, qy1 - exp_y - 10)

        exp_font = FONTS.get(16, "bold")
        max_exp_w = (qx1 - 40) - (qx0 + 40)
        exp_lines = wrap_text(hint_or_exp, exp_font, max_exp_w)
        exp_line_h = 22

        draw_glass_panel(
            draw,
            (qx0 + 24, exp_y, qx1 - 24, exp_y + exp_h),
            fill=(6, 36, 44, int(235 * e_exp)),
            outline=CYAN_GLOW,
            width=2,
            radius=10,
            corner_brackets=True,
            alpha_mul=e_exp
        )
        draw_badge(draw, (qx0 + 40, exp_y + 8), "GIẢI THÍCH CHI TIẾT", FONTS.get(13, "bold"), bg_color=BG_PILL_DEEP, border_color=CYAN_GLOW, text_color=CYAN_LIGHT, icon="dot")
        for l_idx, l_text in enumerate(exp_lines):
            if exp_y + 34 + l_idx * exp_line_h <= exp_y + exp_h - 4:
                draw.text((qx0 + 40, exp_y + 34 + l_idx * exp_line_h), l_text, font=exp_font, fill=WHITE)
'''

# New composite_scene_frame with skip_hud support
new_composite = '''def composite_scene_frame(
    bg_frame: Image.Image,
    scene_data: Dict[str, Any],
    local_t: float,
    duration: float,
    total_progress: float,
    lesson_title: str = "Vật lí 10"
) -> Image.Image:
    frame = bg_frame.copy()
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))

    progress = min(1.0, max(0.0, local_t / max(0.1, duration)))
    hud_type = scene_data.get("hud_type", "hud_boxes")
    hud_data = scene_data.get("hud_data", {})

    layout_mode = hud_data.get("layout") or scene_data.get("hud_layout") or hud_data.get("hud_layout")

    # If skip_hud is requested, skip HUD rendering and only render badge & subtitles
    if layout_mode == "skip_hud" or hud_type in ["none", "skip_hud"]:
        render_mc_badge(overlay, "", lesson_title)
        subtitles = scene_data.get("subtitles", [])
        render_subtitles(overlay, subtitles, local_t, duration)
        render_progress_bar(overlay, total_progress)
        frame.paste(overlay, (0, 0), overlay)
        return frame

    if hud_type == "title_banner":
        render_title_banner(overlay, hud_data, progress)
    elif hud_type == "speed_gauge":
        render_speed_gauge(overlay, hud_data, progress)
    elif hud_type == "animated_axes":
        render_animated_axes(overlay, hud_data, progress)
    elif hud_type == "animated_vector_road":
        render_animated_vector_road(overlay, hud_data, progress)
    elif hud_type == "comparison_table":
        render_comparison_table(overlay, hud_data, progress)
    elif hud_type == "quiz_popup":
        render_quiz_popup(overlay, hud_data, progress)
    else:
        render_hud_boxes(overlay, hud_data, progress)

    # Strictly pass blank speaker to guarantee no MC name is rendered
    render_mc_badge(overlay, "", lesson_title)

    subtitles = scene_data.get("subtitles", [])
    render_subtitles(overlay, subtitles, local_t, duration)

    render_progress_bar(overlay, total_progress)

    frame.paste(overlay, (0, 0), overlay)
    return frame
'''

full_code = prefix + new_renderers + "\n\n" + middle_mc_to_composite + new_composite + "\n"

# Verify ast parse
tree = ast.parse(full_code)
print("AST parse SUCCESSFUL! Nodes count:", len(tree.body))

# Write to hud_animator.py
with open(src_path, "w", encoding="utf-8") as f:
    f.write(full_code)

print("hud_animator.py successfully updated!")
