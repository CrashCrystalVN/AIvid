import sys
import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

WIDTH, HEIGHT = 1920, 1080
FPS = 24
TOTAL_DURATION = 64.42 # seconds
TOTAL_FRAMES = int(TOTAL_DURATION * FPS)

# Fonts
font_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 36)
font_h1 = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 30)
font_h2 = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 24)
font_body = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 22)
font_body_b = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
font_sub = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
font_sm = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)

# Audio timeline segments
# seg1: 0.00 -> 19.01
# seg2: 19.01 -> 38.43
# seg3: 38.43 -> 58.47
# seg4: 58.47 -> 64.42
TIMELINE = [
    (0.00, 19.01, "Chào thầy cô và các bạn! Hãy cùng nhóm mình bắt đầu bằng một tình huống thực tế: Ô tô đi qua ngã tư 36 km/h trong 10s (s = 100m). Liệu có biết xe đang ở đâu?"),
    (19.01, 38.43, "Chắc chắn là chưa thể! Chúng ta cần một hệ tọa độ gắn với vật mốc: trục Ox (Tây - Đông), trục Oy (Nam - Bắc) để định vị chính xác vị trí điểm A."),
    (38.43, 58.47, "Hệ quy chiếu = Hệ tọa độ + Mốc thời gian + Đồng hồ đo. Khi kích thước xe rất nhỏ so với quãng đường 100m, ta coi nó là một chất điểm!"),
    (58.47, 64.42, "Câu hỏi tương tác: Khi nào độ dài quãng đường cho phép chúng ta coi một vật chuyển động là một chất điểm?")
]

def get_subtitle(t):
    for start, end, text in TIMELINE:
        if start <= t < end:
            return text
    return ""

def draw_arrow(draw, p1, p2, color=(56, 189, 248), width=3, head_len=14):
    draw.line([p1, p2], fill=color, width=width)
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    angle = math.atan2(dy, dx)
    angle1 = angle + math.pi * 0.85
    angle2 = angle - math.pi * 0.85
    a1 = (p2[0] + head_len * math.cos(angle1), p2[1] + head_len * math.sin(angle1))
    a2 = (p2[0] + head_len * math.cos(angle2), p2[1] + head_len * math.sin(angle2))
    draw.polygon([p2, a1, a2], fill=color)

def draw_car(draw, cx, cy, width=54, height=30, color=(239, 68, 68)):
    # Simple sleek sports car top-down
    x0, y0 = cx - width//2, cy - height//2
    x1, y1 = cx + width//2, cy + height//2
    # Shadow
    draw.rounded_rectangle([(x0+2, y0+4), (x1+4, y1+4)], radius=8, fill=(10, 15, 25))
    # Car body
    draw.rounded_rectangle([(x0, y0), (x1, y1)], radius=8, fill=color)
    # Windshield / roof
    draw.rounded_rectangle([(cx - 10, y0 + 4), (cx + 12, y1 - 4)], radius=4, fill=(30, 41, 59))
    # Headlights (front facing right)
    draw.rectangle([(x1 - 3, y0 + 3), (x1, y0 + 9)], fill=(254, 240, 138))
    draw.rectangle([(x1 - 3, y1 - 9), (x1, y1 - 3)], fill=(254, 240, 138))
    # Wheels
    draw.rectangle([(x0 + 6, y0 - 3), (x0 + 16, y0)], fill=(15, 23, 42))
    draw.rectangle([(x1 - 16, y0 - 3), (x1 - 6, y0)], fill=(15, 23, 42))
    draw.rectangle([(x0 + 6, y1), (x0 + 16, y1 + 3)], fill=(15, 23, 42))
    draw.rectangle([(x1 - 16, y1), (x1 - 6, y1 + 3)], fill=(15, 23, 42))

def create_frame(t):
    im = Image.new("RGB", (WIDTH, HEIGHT), (11, 19, 43))
    draw = ImageDraw.Draw(im)

    # Subtle background grid
    grid_color = (18, 29, 58)
    for x in range(0, WIDTH, 80):
        draw.line([(x, 90), (x, HEIGHT - 100)], fill=grid_color, width=1)
    for y in range(90, HEIGHT - 100, 80):
        draw.line([(0, y), (WIDTH, y)], fill=grid_color, width=1)

    # 1. Top Bar
    draw.rectangle([(0, 0), (WIDTH, 90)], fill=(15, 23, 42))
    draw.line([(0, 90), (WIDTH, 90)], fill=(30, 58, 138), width=2)
    # Badge
    draw.rounded_rectangle([(50, 20), (220, 70)], radius=10, fill=(37, 99, 235))
    draw.text((70, 30), "VẬT LÍ 10", font=font_h2, fill=(255, 255, 255))
    # Title
    draw.text((250, 26), "BÀI 4: VỊ TRÍ CỦA VẬT & HỆ QUY CHIẾU", font=font_title, fill=(56, 189, 248))
    # Authors
    draw.text((1360, 32), "Nhóm: Anh Thư • Hữu Trọng • Thế Mỹ", font=font_body, fill=(148, 163, 184))

    # 2. Main Content based on t
    if t < 19.01:
        # SCENE 1: NGÃ TƯ & Ô TÔ CHUYỂN ĐỘNG
        # Left Panel: Intersection graphic
        panel_box = (80, 130, 1020, 900)
        draw.rounded_rectangle(panel_box, radius=18, fill=(16, 26, 52), outline=(37, 99, 235), width=2)
        draw.text((110, 150), "HOẠT HỌA MÔ PHỎNG: NGÃ TƯ GIAO LỘ 4 HƯỚNG", font=font_h2, fill=(251, 191, 36))

        # Draw 4-way Intersection
        cx, cy = 550, 530
        road_w = 140
        # Horizontal road
        draw.rectangle([(120, cy - road_w//2), (980, cy + road_w//2)], fill=(30, 41, 59))
        # Vertical road
        draw.rectangle([(cx - road_w//2, 220), (cx + road_w//2, 840)], fill=(30, 41, 59))
        
        # Center intersection asphalt
        draw.rectangle([(cx - road_w//2, cy - road_w//2), (cx + road_w//2, cy + road_w//2)], fill=(35, 48, 70))

        # Road dashed lines
        for x in range(130, cx - road_w//2, 30):
            draw.line([(x, cy), (x+15, cy)], fill=(234, 179, 8), width=3)
        for x in range(cx + road_w//2 + 10, 970, 30):
            draw.line([(x, cy), (x+15, cy)], fill=(234, 179, 8), width=3)
        for y in range(230, cy - road_w//2, 30):
            draw.line([(cx, y), (cx, y+15)], fill=(234, 179, 8), width=3)
        for y in range(cy + road_w//2 + 10, 830, 30):
            draw.line([(cx, y), (cx, y+15)], fill=(234, 179, 8), width=3)

        # Compass labels
        draw.text((cx - 30, 230), "▲ BẮC", font=font_h2, fill=(244, 63, 94))
        draw.text((cx - 30, 800), "▼ NAM", font=font_h2, fill=(56, 189, 248))
        draw.text((130, cy - 15), "◀ TÂY", font=font_h2, fill=(168, 85, 247))
        draw.text((900, cy - 15), "ĐÔNG ▶", font=font_h2, fill=(34, 197, 94))

        # Origin O
        draw.ellipse([(cx - 8, cy - 8), (cx + 8, cy + 8)], fill=(239, 68, 68), outline=(255, 255, 255), width=2)
        draw.text((cx - 24, cy - 35), "Gốc O", font=font_body_b, fill=(255, 255, 255))

        # Car animation from O to East
        car_t = max(0.0, min(1.0, (t - 3.0) / 10.0))
        car_x = cx + car_t * 300
        car_y = cy + 25

        if car_t > 0:
            # Trailing distance measurement line
            draw.line([(cx, cy + 55), (car_x, cy + 55)], fill=(56, 189, 248), width=3)
            draw.line([(cx, cy + 45), (cx, cy + 65)], fill=(56, 189, 248), width=2)
            draw.line([(car_x, cy + 45), (car_x, cy + 65)], fill=(56, 189, 248), width=2)
            draw.text(((cx + car_x)//2 - 60, cy + 65), f"s = {int(car_t * 100)} m", font=font_body_b, fill=(56, 189, 248))

        draw_car(draw, int(car_x), int(car_y))

        # Right Panel: Physics Problem & Question
        r_box = (1060, 130, 1840, 900)
        draw.rounded_rectangle(r_box, radius=18, fill=(16, 26, 52), outline=(51, 65, 85), width=2)
        
        # Card 1: Data
        draw.rounded_rectangle([(1090, 160), (1810, 390)], radius=14, fill=(22, 36, 71), outline=(37, 99, 235), width=1)
        draw.text((1120, 180), "📌 DỮ LIỆU ĐỀ BÀI THỰC TẾ", font=font_h2, fill=(56, 189, 248))
        draw.text((1120, 230), "• Tốc độ của ô tô:  v = 36 km/h = 10 m/s", font=font_body, fill=(241, 245, 249))
        draw.text((1120, 275), "• Thời gian chuyển động:  t = 10 s", font=font_body, fill=(241, 245, 249))
        draw.text((1120, 320), "• Quãng đường đi được:  s = v . t = 100 m", font=font_body_b, fill=(34, 197, 94))

        # Card 2: Question (at t >= 6s)
        if t >= 6.0:
            draw.rounded_rectangle([(1090, 420), (1810, 620)], radius=14, fill=(45, 30, 20), outline=(245, 158, 11), width=2)
            draw.text((1120, 440), "❓ CÂU HỎI ĐẶT RA", font=font_h2, fill=(251, 191, 36))
            draw.text((1120, 490), "Chỉ biết quãng đường s = 100 m,", font=font_body, fill=(255, 255, 255))
            draw.text((1120, 530), "chúng ta có biết xe đang ở ĐÂU trên bản đồ?", font=font_body_b, fill=(254, 240, 138))

        # Card 3: Conclusion (at t >= 12s)
        if t >= 12.0:
            draw.rounded_rectangle([(1090, 650), (1810, 860)], radius=14, fill=(45, 20, 25), outline=(239, 68, 68), width=2)
            draw.text((1120, 670), "❌ CHẮC CHẮN LÀ CHƯA THỂ!", font=font_h2, fill=(248, 113, 113))
            draw.text((1120, 720), "Vì Quãng đường (s) chỉ cho biết ĐỘ DÀI,", font=font_body, fill=(255, 255, 255))
            draw.text((1120, 760), "chưa cho biết HƯỚNG chuyển động của xe!", font=font_body_b, fill=(252, 165, 165))
            draw.text((1120, 805), "Xe có thể đang ở phía Đông, Tây, Nam hay Bắc!", font=font_sm, fill=(203, 213, 225))

    elif t < 38.43:
        # SCENE 2: HỆ TỌA ĐỘ VÀ VẬT MỐC
        # Left Panel: Coordinate Grid Oxy
        panel_box = (80, 130, 1020, 900)
        draw.rounded_rectangle(panel_box, radius=18, fill=(16, 26, 52), outline=(37, 99, 235), width=2)
        draw.text((110, 150), "HỆ TRỤC TỌA ĐỘ VUÔNG GÓC Oxy ĐỊA LÍ", font=font_h2, fill=(56, 189, 248))

        ox, oy = 350, 700
        axis_len = 480
        # Draw axes
        draw_arrow(draw, (ox - 40, oy), (ox + axis_len, oy), color=(56, 189, 248), width=4, head_len=18)
        draw_arrow(draw, (ox, oy + 40), (ox, oy - axis_len), color=(34, 197, 94), width=4, head_len=18)
        
        draw.text((ox + axis_len + 10, oy - 15), "Ox (Đông)", font=font_h2, fill=(56, 189, 248))
        draw.text((ox - 70, oy - axis_len - 30), "Oy (Bắc)", font=font_h2, fill=(34, 197, 94))
        draw.text((ox - 30, oy + 10), "O", font=font_h2, fill=(255, 255, 255))
        draw.text((ox - 120, oy + 45), "(Vật mốc)", font=font_sm, fill=(148, 163, 184))

        # Scale marks (every 80px = 10m)
        for i in range(1, 5):
            xm = ox + i * 80
            draw.line([(xm, oy - 5), (xm, oy + 5)], fill=(56, 189, 248), width=2)
            draw.text((xm - 15, oy + 12), f"{i*10}m", font=font_sm, fill=(148, 163, 184))
            ym = oy - i * 80
            draw.line([(ox - 5, ym), (ox + 5, ym)], fill=(34, 197, 94), width=2)
            draw.text((ox - 50, ym - 10), f"{i*10}m", font=font_sm, fill=(148, 163, 184))

        # Point A at (20m, 45 deg)
        # 20m = 160px. at 45 deg: dx = 160 * cos(45) = 113px, dy = 113px
        ax = ox + 160
        ay = oy - 160
        
        # Dashed projections
        draw.line([(ax, oy), (ax, ay)], fill=(100, 116, 139), width=2)
        draw.line([(ox, ay), (ax, ay)], fill=(100, 116, 139), width=2)
        
        # Position vector OA
        draw_arrow(draw, (ox, oy), (ax, ay), color=(239, 68, 68), width=4, head_len=16)
        
        # Angle arc 45 deg
        draw.arc([(ox - 40, oy - 40), (ox + 40, oy + 40)], start=315, end=360, fill=(251, 191, 36), width=3)
        draw.text((ox + 50, oy - 35), "45°", font=font_body_b, fill=(251, 191, 36))

        # Point A circle
        draw.ellipse([(ax - 8, ay - 8), (ax + 8, ay + 8)], fill=(239, 68, 68), outline=(255, 255, 255), width=2)
        draw.text((ax + 15, ay - 20), "Điểm A (20m, 45° Đông - Bắc)", font=font_h2, fill=(254, 240, 138))

        # Right Panel: Explanation
        r_box = (1060, 130, 1840, 900)
        draw.rounded_rectangle(r_box, radius=18, fill=(16, 26, 52), outline=(51, 65, 85), width=2)
        draw.text((1090, 160), "🧭 XÁC ĐỊNH VỊ TRÍ CỦA VẬT", font=font_h1, fill=(251, 191, 36))

        draw.rounded_rectangle([(1090, 220), (1810, 480)], radius=14, fill=(22, 36, 71), outline=(37, 99, 235), width=1)
        draw.text((1120, 245), "Hai yếu tố cốt lõi:", font=font_h2, fill=(56, 189, 248))
        draw.text((1120, 295), "1. VẬT MỐC: Vật được chọn làm chuẩn đứng yên", font=font_body, fill=(241, 245, 249))
        draw.text((1150, 335), "(Ví dụ: Ngã tư đường, cột mốc cây số...)", font=font_sm, fill=(148, 163, 184))
        draw.text((1120, 375), "2. HỆ TRỤC TỌA ĐỘ Oxy gắn liền với vật mốc:", font=font_body, fill=(241, 245, 249))
        draw.text((1150, 415), "• Trục Ox: Hướng Tây – Đông", font=font_body_b, fill=(56, 189, 248))
        draw.text((1150, 445), "• Trục Oy: Hướng Bắc – Nam", font=font_body_b, fill=(34, 197, 94))

        draw.rounded_rectangle([(1090, 520), (1810, 840)], radius=14, fill=(30, 41, 59), outline=(148, 163, 184), width=1)
        draw.text((1120, 550), "💡 KẾT LUẬN QUAN TRỌNG:", font=font_h2, fill=(34, 197, 94))
        draw.text((1120, 605), "Nhờ có hệ tọa độ Oxy gắn với vật mốc O,", font=font_body, fill=(255, 255, 255))
        draw.text((1120, 645), "ta xác định chính xác vị trí của bất kỳ vật nào:", font=font_body, fill=(255, 255, 255))
        draw.text((1150, 695), "• Tọa độ điểm A: cách O là 20 m", font=font_body_b, fill=(254, 240, 138))
        draw.text((1150, 735), "• Hướng: 45° lệch về phía Đông – Bắc", font=font_body_b, fill=(254, 240, 138))
        draw.text((1120, 785), "=> Không còn sự nhầm lẫn về vị trí nữa!", font=font_body, fill=(56, 189, 248))

    elif t < 58.47:
        # SCENE 3: HỆ QUY CHIẾU & CHẤT ĐIỂM
        # Top Formula Banner
        draw.rounded_rectangle([(120, 130), (1800, 260)], radius=16, fill=(30, 41, 59), outline=(251, 191, 36), width=3)
        draw.text((150, 150), "CÔNG THỨC VÀNG VẬT LÍ:", font=font_h2, fill=(251, 191, 36))
        draw.text((150, 195), "HỆ QUY CHIẾU = HỆ TỌA ĐỘ + MỐC THỜI GIAN + ĐỒNG HỒ ĐO", font=font_title, fill=(255, 255, 255))

        # 3 Component Columns
        cols = [
            ("1. HỆ TỌA ĐỘ Oxy", "Gắn với vật mốc đứng yên.\nXác định chính xác VỊ TRÍ của vật trong không gian tại mọi thời điểm.", (56, 189, 248)),
            ("2. MỐC THỜI GIAN", "Thời điểm bắt đầu khảo sát\nchuyển động (thường chọn t₀ = 0 khi vật bắt đầu chuyển động).", (34, 197, 94)),
            ("3. ĐỒNG HỒ ĐO", "Dụng cụ dùng để đo khoảng\nthời gian trôi qua giữa các thời điểm (Δt = t₂ - t₁).", (251, 191, 36))
        ]
        for idx, (head, desc, col) in enumerate(cols):
            x1 = 120 + idx * 580
            x2 = x1 + 540
            draw.rounded_rectangle([(x1, 290), (x2, 540)], radius=14, fill=(16, 26, 52), outline=col, width=2)
            draw.text((x1 + 25, 315), head, font=font_h2, fill=col)
            draw.line([(x1 + 25, 360), (x2 - 25, 360)], fill=(51, 65, 85), width=1)
            y_offset = 380
            for line in desc.split("\n"):
                draw.text((x1 + 25, y_offset), line, font=font_body, fill=(226, 232, 240))
                y_offset += 38

        # Bottom Box: KHÁI NIỆM CHẤT ĐIỂM
        draw.rounded_rectangle([(120, 570), (1800, 890)], radius=16, fill=(22, 36, 71), outline=(168, 85, 247), width=2)
        draw.text((160, 595), "🎯 KHÁI NIỆM CHẤT ĐIỂM TRONG VẬT LÍ", font=font_h1, fill=(192, 132, 252))
        
        # Left graphic of car vs distance
        draw.text((160, 660), "So sánh kích thước:", font=font_h2, fill=(255, 255, 255))
        draw.text((160, 710), "• Chiều dài ô tô:  L ≈ 4 m", font=font_body, fill=(244, 63, 94))
        draw.text((160, 755), "• Quãng đường đi:  s = 100 m", font=font_body, fill=(34, 197, 94))
        draw.text((160, 810), "=> Kích thước xe RẤT NHỎ so với quãng đường (L << s)", font=font_body_b, fill=(251, 191, 36))

        # Right graphic: Car collapsing into a Point Mass
        draw.rounded_rectangle([(1100, 620), (1750, 850)], radius=12, fill=(15, 23, 42))
        draw.text((1130, 645), "QUY TẮC CHẤT ĐIỂM:", font=font_h2, fill=(34, 197, 94))
        draw.text((1130, 695), "Một vật được coi là CHẤT ĐIỂM nếu", font=font_body, fill=(255, 255, 255))
        draw.text((1130, 735), "kích thước của nó rất nhỏ so với quãng đường", font=font_body, fill=(255, 255, 255))
        draw.text((1130, 775), "đi được hoặc khoảng cách mà ta khảo sát!", font=font_body_b, fill=(56, 189, 248))
        draw.ellipse([(1400, 810), (1420, 830)], fill=(239, 68, 68), outline=(255, 255, 255), width=2)
        draw.text((1435, 807), "Chất điểm (m)", font=font_body_b, fill=(254, 240, 138))

    else:
        # SCENE 4: CÂU HỎI TƯƠNG TÁC (POP-UP QUIZ)
        draw.rounded_rectangle([(240, 160), (1680, 870)], radius=24, fill=(15, 23, 42), outline=(251, 191, 36), width=3)
        
        # Pop-up Header
        draw.rounded_rectangle([(650, 120), (1270, 200)], radius=18, fill=(245, 158, 11))
        draw.text((680, 138), "🔔 CÂU HỎI TƯƠNG TÁC", font=font_h1, fill=(15, 23, 42))

        # Question
        draw.text((300, 260), "Hỏi cả lớp:", font=font_h2, fill=(251, 191, 36))
        draw.text((300, 310), "\"Khi nào độ dài quãng đường cho phép chúng ta", font=font_title, fill=(255, 255, 255))
        draw.text((300, 370), "coi một vật chuyển động là một CHẤT ĐIỂM?\"", font=font_title, fill=(56, 189, 248))

        # Answer Box
        draw.rounded_rectangle([(300, 460), (1620, 640)], radius=16, fill=(22, 36, 71), outline=(34, 197, 94), width=2)
        draw.text((340, 490), "✓ ĐÁP ÁN CHÍNH XÁC:", font=font_h2, fill=(34, 197, 94))
        draw.text((340, 545), "Khi kích thước hình học của vật RẤT NHỎ so với quãng đường", font=font_body_b, fill=(255, 255, 255))
        draw.text((340, 585), "đi được hoặc khoảng cách mà ta đang xem xét!", font=font_body_b, fill=(254, 240, 138))

        # Thank you footer
        draw.text((540, 720), "CẢM ƠN THẦY CÔ VÀ CÁC BẠN ĐÃ THEO DÕI!", font=font_h1, fill=(56, 189, 248))
        draw.text((680, 780), "Thực hiện: Anh Thư • Hữu Trọng • Thế Mỹ", font=font_h2, fill=(148, 163, 184))

    # 3. Bottom Subtitle Pill
    sub_text = get_subtitle(t)
    if sub_text:
        # Wrap subtitle if needed
        draw.rounded_rectangle([(100, 930), (1820, 1020)], radius=14, fill=(10, 15, 28, 240), outline=(56, 189, 248), width=1)
        draw.text((130, 955), sub_text, font=font_sub, fill=(255, 255, 255))

    # 4. Progress bar at bottom
    prog = min(1.0, max(0.0, t / TOTAL_DURATION))
    draw.rectangle([(0, HEIGHT - 8), (WIDTH, HEIGHT)], fill=(30, 41, 59))
    draw.rectangle([(0, HEIGHT - 8), (int(WIDTH * prog), HEIGHT)], fill=(56, 189, 248))

    return im

def main():
    out_mp4 = "Video1_ViTri_HeQuyChieu.mp4"
    audio_file = "final_audio.mp3"
    
    # Start ffmpeg process piping raw RGB frames
    cmd = [
        ffmpeg_exe, "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-", # stdin
        "-i", audio_file,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-pix_fmt", "yuv420p",
        "-crf", "20",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        out_mp4
    ]
    
    print(f"Starting video rendering: {TOTAL_FRAMES} frames ({TOTAL_DURATION:.1f}s) at {FPS} FPS...")
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    
    for frame_idx in range(TOTAL_FRAMES):
        t = frame_idx / FPS
        im = create_frame(t)
        proc.stdin.write(im.tobytes())
        if frame_idx % 120 == 0:
            pct = (frame_idx / TOTAL_FRAMES) * 100
            print(f"Rendered frame {frame_idx}/{TOTAL_FRAMES} ({pct:.1f}%) - time {t:.1f}s")
            
    proc.stdin.close()
    proc.wait()
    print(f"Render completed successfully! Output: {out_mp4}")

if __name__ == "__main__":
    main()
