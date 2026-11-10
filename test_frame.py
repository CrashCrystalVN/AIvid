import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
font_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 40)
font_h1 = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 32)
font_body = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 26)
font_bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
font_sm = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)

im = Image.new("RGB", (W, H), (15, 23, 42))
draw = ImageDraw.Draw(im)

# Top Bar
draw.rectangle([(0, 0), (W, 90)], fill=(11, 19, 43))
draw.line([(0, 90), (W, 90)], fill=(30, 41, 59), width=2)

# Badges
draw.rounded_rectangle([(60, 20), (220, 70)], radius=12, fill=(30, 58, 138))
draw.text((78, 30), "VẬT LÍ 10", font=font_bold, fill=(240, 249, 255))

draw.text((250, 25), "BÀI 4: VỊ TRÍ CỦA VẬT & HỆ QUY CHIẾU", font=font_title, fill=(56, 189, 248))
draw.text((1380, 32), "Nhóm: Anh Thư • Hữu Trọng • Thế Mỹ", font=font_body, fill=(148, 163, 184))

im.save("sample_frame.png")
print("Saved sample_frame.png")
