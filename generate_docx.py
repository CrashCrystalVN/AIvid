import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

doc = docx.Document()

# Page Margins
sections = doc.sections
for s in sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

# Title
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_t = p_title.add_run("KỊCH BẢN THUYẾT TRÌNH VIDEO BÀI GIẢNG VẬT LÍ 10")
run_t.font.name = "Arial"
run_t.font.size = Pt(20)
run_t.font.bold = True
run_t.font.color.rgb = RGBColor(24, 76, 120)

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_sub = p_sub.add_run("Chủ đề: Động học & Động lực học (Bài 4, Bài 5 & Các bài mở rộng)\nPhong cách thuyết trình học sinh năng động, trực quan")
run_sub.font.name = "Arial"
run_sub.font.size = Pt(11)
run_sub.font.italic = True
run_sub.font.color.rgb = RGBColor(100, 110, 120)

doc.add_paragraph().paragraph_format.space_after = Pt(10)

# Section: Phân công nhóm
p_sec1 = doc.add_paragraph()
r_sec1 = p_sec1.add_run("I. BẢNG TỔNG HỢP VÀ PHÂN CÔNG THÀNH VIÊN")
r_sec1.font.name = "Arial"
r_sec1.font.size = Pt(13)
r_sec1.font.bold = True
r_sec1.font.color.rgb = RGBColor(30, 60, 100)

table_assign = doc.add_table(rows=1, cols=4)
table_assign.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Chương / Bài", "Nội dung phân đoạn", "Hình thức Video", "Người thực hiện"]
hdr_cells = table_assign.rows[0].cells
for i, h in enumerate(headers):
    hdr_cells[i].text = h
    set_cell_background(hdr_cells[i], "1F497D")
    set_cell_margins(hdr_cells[i], top=120, bottom=120, left=150, right=150)
    for p in hdr_cells[i].paragraphs:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.name = "Arial"
            run.font.bold = True
            run.font.color.rgb = RGBColor(255, 255, 255)
            run.font.size = Pt(10)

assignments = [
    ("Bài 4: Độ dịch chuyển", "Video 1: Vị trí của vật & Hệ quy chiếu", "Video AI (~2p)", "Anh Thư, Hữu Trọng, Thế Mỹ"),
    ("Bài 4: Độ dịch chuyển", "Video 2: Độ dịch chuyển & Phân biệt Quãng đường", "Video AI (~2p30s)", "Anh Thư, Hữu Trọng, Thế Mỹ"),
    ("Bài 4: Độ dịch chuyển", "Video 3: Tổng hợp Độ dịch chuyển", "Video AI (~2p)", "Anh Thư, Hữu Trọng, Thế Mỹ"),
    ("Bài 5: Tốc độ & Vận tốc", "Video 4: Tốc độ & Vận tốc", "Video AI (~2p30s)", "Tú Châu, Minh Dũng, Bảo Hân, Thế Mỹ, Hữu Trọng"),
    ("Bài 5: Tốc độ & Vận tốc", "Video 5: Tổng hợp Vận tốc & Công thức cộng", "Video AI (~2p15s)", "Tú Châu, Minh Dũng, Bảo Hân, Thế Mỹ, Hữu Trọng"),
    ("Bài 12: Chuyển động ném", "Ném ngang (Khái niệm, TN, công thức)", "Video AI", "Lê Gia, Minh Dũng, Lê H Bách, Bảo Yến, Cẩm Nhung"),
    ("Bài 12: Chuyển động ném", "Ném xiên (Phân tích, tầm cao, tầm xa)", "Video AI", "Lê Gia, Minh Dũng, Lê H Bách, Bảo Yến, Cẩm Nhung"),
    ("Bài 14: Định luật 1 Newton", "Nội dung ĐL 1 Newton & Quán tính", "Video AI", "Quang Huy, Tú Châu, Bảo Yến, Cẩm Nhung"),
    ("Bài 15: Định luật 2 Newton", "Nội dung ĐL 2 Newton & Khối lượng", "Video AI", "Lê Gia, Quang Huy, Bảo Hân, Anh Thư, Tú Châu"),
    ("Bài 16: Định luật 3 Newton", "Lực và Phản lực", "Video AI", "Tú Châu, Lê H Bách, Bảo Yến, Quang Huy"),
]

for row_idx, item in enumerate(assignments):
    row_cells = table_assign.add_row().cells
    bg_color = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, text in enumerate(item):
        row_cells[col_idx].text = text
        set_cell_background(row_cells[col_idx], bg_color)
        set_cell_margins(row_cells[col_idx], top=80, bottom=80, left=120, right=120)
        p = row_cells[col_idx].paragraphs[0]
        if col_idx in [0, 2]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = "Arial"
            r.font.size = Pt(9.5)

doc.add_paragraph().paragraph_format.space_after = Pt(15)

# Videos Data
videos = [
    {
        "id": 1,
        "title": "Video 1: Vị trí của vật & Hệ quy chiếu (Bài 4 - Phần 1)",
        "duration": "~2 phút",
        "members": "Anh Thư, Hữu Trọng, Thế Mỹ",
        "visual": (
            "- Hoạt họa ngã tư đường có 4 hướng Đông – Tây – Nam – Bắc. Một chiếc ô tô đi đến ngã tư O và chuyển động tiếp trong 10 s với tốc độ 36 km/h.\n"
            "- Dòng chữ lớn nổi bật: 'Quãng đường đi được = 100 m. Ô tô đang ở đâu?'\n"
            "- Đồ họa hệ trục tọa độ vuông góc Oxy gắn với địa lí: Trục Ox là hướng Tây – Đông, Trục Oy là hướng Bắc – Nam.\n"
            "- Chấm điểm A trên bản đồ: tọa độ (20 m, hướng 45° Đông – Bắc).\n"
            "- Khung công thức đóng hộp: Hệ quy chiếu = Hệ tọa độ + Mốc thời gian + Đồng hồ đo."
        ),
        "voiceover": (
            "\"Chào thầy cô và các bạn! Hãy cùng nhóm mình bắt đầu bằng một tình huống thực tế nhé: Một chiếc ô tô đi qua ngã tư với tốc độ 36 km/h. Sau 10 giây, xe đi được quãng đường 100 m. Câu hỏi đặt ra là: Liệu chỉ biết quãng đường 100 m, chúng mình có thể xác định chính xác xe đang ở đâu trên bản đồ không?\n\n"
            "Chắc chắn là chưa thể rồi, đúng không? Để biết chính xác vị trí, chúng ta cần một hệ tọa độ gắn với vật mốc. Trong đời sống, các bạn thường thấy hệ tọa độ địa lí với trục Ox theo hướng Tây – Đông và trục Oy theo hướng Bắc – Nam.\n\n"
            "Khi chúng mình kết hợp hệ tọa độ này cùng với mốc thời gian và một chiếc đồng hồ bấm giờ, ta sẽ có một hệ quy chiếu hoàn chỉnh. Nếu xe chỉ chạy thẳng trên một đường, chúng mình chỉ cần chọn duy nhất một trục Ox trùng với đường đi. Và khi kích thước xe rất nhỏ so với quãng đường 100 m, tụi mình hoàn toàn có thể coi nó là một chất điểm!\""
        ),
        "pedagogy": "Xuất hiện câu hỏi tương tác pop-up trên màn hình: \"Khi nào độ dài quãng đường cho phép coi vật là chất điểm?\" Tạo mâu thuẫn nhận thức: quãng đường chỉ cho biết độ dài, chưa cho biết hướng nên chưa xác định được vị trí."
    },
    {
        "id": 2,
        "title": "Video 2: Độ dịch chuyển & Phân biệt Quãng đường (Bài 4 - Phần 2)",
        "duration": "~2 phút 30 giây",
        "members": "Anh Thư, Hữu Trọng, Thế Mỹ",
        "visual": (
            "- Tiếp tục cảnh xe ở ngã tư: Xuất hiện mũi tên đỏ nối từ gốc O đến điểm B ở hướng Bắc; ký hiệu d_OB tượng trưng cho 100 m.\n"
            "- Chữ nổi bật đổi màu: Độ dịch chuyển (d) là một đại lượng vectơ.\n"
            "- Sơ đồ 3 người đi từ siêu thị A đến bưu điện B: Người đi xe máy (đường cong 1), Người đi bộ (đường thẳng 2), Người đi ô tô (đường cong 3).\n"
            "- Bảng so sánh 2 cột trực quan:\n"
            "   + Quãng đường (s): Độ dài thực tế đường đi (s1 ≠ s2 ≠ s3).\n"
            "   + Độ dịch chuyển (d): Nối thẳng từ A đến B (d1 = d2 = d3)."
        ),
        "voiceover": (
            "\"Quay lại ngã tư ban nãy, nếu mình nói rõ là: xe chạy 100 m về hướng Bắc, các bạn sẽ chỉ ra ngay xe đang ở điểm B. Đại lượng vừa cho biết độ dài, vừa cho biết hướng thay đổi vị trí đó chính là Độ dịch chuyển!\n\n"
            "Độ dịch chuyển là một đại lượng vecto, ký hiệu là d có mũi tên. Chúng mình vẽ nó bằng một mũi tên nối từ điểm xuất phát đến điểm kết thúc, độ dài mũi tên tỉ lệ thuận với độ lớn dịch chuyển.\n\n"
            "Hai khái niệm Quãng đường và Độ dịch chuyển rất dễ nhầm lẫn, các bạn chú ý nhé: Quãng đường s là độ dài cung đường thực tế mà vật đã đi. Nhìn vào hình, ba người đi theo ba tuyến đường khác nhau nên quãng đường của họ chắc chắn khác nhau.\n\n"
            "Thế nhưng độ dịch chuyển d lại chỉ quan tâm điểm đầu là siêu thị A và điểm cuối là bưu điện B. Vì cùng đi từ A đến B, nên độ dịch chuyển của cả ba người là hoàn toàn như nhau!\n\n"
            "Một mẹo nhỏ tụi mình rút ra: Chỉ khi vật đi thẳng và tuyệt đối không quay đầu đổi chiều thì độ lớn độ dịch chuyển mới bằng quãng đường (|d| = s).\""
        ),
        "pedagogy": "Chốt đọng lại công thức điều kiện cốt lõi: |d| = s khi chuyển động thẳng không đổi hướng. Ngược lại (|d| ≠ s)."
    },
    {
        "id": 3,
        "title": "Video 3: Tổng hợp Độ dịch chuyển (Bài 4 - Phần 3)",
        "duration": "~2 phút",
        "members": "Anh Thư, Hữu Trọng, Thế Mỹ",
        "visual": (
            "- Mô hình đường đi tam giác vuông ABC: Đi từ A đến B (4 km hướng Đông), rồi rẽ từ B đến C (4 km hướng Bắc).\n"
            "- Biểu diễn 2 vecto thành phần d1 = AB, d2 = BC và vecto tổng hợp d = AC.\n"
            "- Chèn phép tính trực quan:\n"
            "   + Quãng đường: s = 4 + 4 = 8 km.\n"
            "   + Độ dịch chuyển: d = √(4² + 4²) ≈ 5,7 km (hướng 45° Đông – Bắc).\n"
            "- Đồ họa 3 quy tắc tổng quát: Cùng chiều (d = d1 + d2), Ngược chiều (d = |d1 - d2|), Vuông góc (d = √(d1² + d2²))."
        ),
        "voiceover": (
            "\"Nếu một vật di chuyển nhiều chặng liên tiếp thì làm sao tính được độ dịch chuyển chung cuộc? Chúng mình sẽ dùng quy tắc cộng vecto: d = d1 + d2.\n\n"
            "Hãy xem ví dụ này cùng mình: Một bạn đi từ A sang B 4 km về hướng Đông, sau đó rẽ tiếp từ B lên C 4 km về hướng Bắc. Quãng đường thực tế bạn ấy đi là 4 cộng 4 bằng 8 km. Nhưng độ dịch chuyển tổng hợp lại là đường chéo nối thẳng từ A đến C.\n\n"
            "Áp dụng định lý Pitago quen thuộc, độ lớn độ dịch chuyển của bạn ấy là căn của 4 bình cộng 4 bình, ra khoảng 5,7 km theo hướng Đông – Bắc!\n\n"
            "Như vậy, khi làm bài tập, các bạn chỉ cần nhớ: cùng chiều thì cộng, ngược chiều thì lấy hiệu, còn vuông góc nhau thì dùng ngay Pitago nhé!\""
        ),
        "pedagogy": "Làm rõ bản chất: tổng hợp vecto dịch chuyển không phải cộng đại số thuần túy, phải chú ý hướng và quy tắc hình học."
    },
    {
        "id": 4,
        "title": "Video 4: Tốc độ & Vận tốc (Bài 5 - Phần 1)",
        "duration": "~2 phút 30 giây",
        "members": "Tú Châu, Minh Dũng, Bảo Hân, Thế Mỹ, Hữu Trọng",
        "visual": (
            "- Chia đôi màn hình: Một bên là vận động viên điền kinh 100 m bứt tốc; một bên là cận cảnh đồng hồ tốc kế xe máy đang rung kim chỉ 50 km/h.\n"
            "- Hiển thị công thức tốc độ trung bình: v = s / t (kèm số liệu mẫu 100 m / 9,98 s ≈ 10 m/s).\n"
            "- Hiển thị công thức vận tốc: v = d / t, vecto vận tốc vẽ cùng chiều vecto dịch chuyển.\n"
            "- Bảng tóm tắt 2 cột phân biệt:\n"
            "   + Tốc độ (v): Đại lượng vô hướng, chỉ đo mức độ nhanh/chậm, luôn ≥ 0.\n"
            "   + Vận tốc (v): Đại lượng vecto, có cả phương chiều, có thể mang giá trị âm, dương hoặc bằng 0."
        ),
        "voiceover": (
            "\"Chào các bạn! Trong giao tiếp hàng ngày, chúng mình hay nói 'chạy với tốc độ này' hay 'vận tốc kia' như hai từ đồng nghĩa. Nhưng trong môn Vật lí, hai khái niệm này khác nhau hoàn toàn đấy!\n\n"
            "Đầu tiên là Tốc độ. Để biết vật đi nhanh hay chậm trên cả quãng đường, ta lấy quãng đường chia thời gian: v = s/t. Ví dụ vận động viên chạy 100 m hết 9,98 giây thì tốc độ trung bình khoảng 10 m/s. Còn con số hiện trên đồng hồ xe máy lúc chúng mình đang chạy xe chính là tốc độ tức thời.\n\n"
            "Tuy nhiên, tốc độ không cho biết vật đang lao về hướng nào. Vì thế, chúng ta cần khái niệm Vận tốc. Vận tốc trung bình bằng độ dịch chuyển chia cho thời gian: v = d/t.\n\n"
            "Vì độ dịch chuyển là vecto nên vận tốc cũng mang tính vecto. Tốc độ thì luôn không bao giờ âm, nhưng vận tốc thì hoàn toàn có thể âm hoặc bằng không nếu chúng mình đi lùi hay quay ngược chiều chọn!\""
        ),
        "pedagogy": "Nhấn mạnh: Chỉ khi chuyển động thẳng một chiều không đổi hướng thì tốc độ mới bằng độ lớn của vận tốc."
    },
    {
        "id": 5,
        "title": "Video 5: Tổng hợp Vận tốc & Công thức cộng vận tốc (Bài 5 - Phần 2)",
        "duration": "~2 phút 15 giây",
        "members": "Tú Châu, Minh Dũng, Bảo Hân, Thế Mỹ, Hữu Trọng",
        "visual": (
            "- Đồ họa hoạt hình một hành khách đang bước đi trên một đoàn tàu hỏa đang chạy trên đường ray:\n"
            "   + Gán số quy ước: (1) Người, (2) Toa tàu, (3) Mặt đường ray.\n"
            "   + Đánh dấu 3 vecto: v_1,2 (vận tốc tương đối), v_2,3 (vận tốc kéo theo), v_1,3 (vận tốc tuyệt đối).\n"
            "- Khung công thức cộng vận tốc nổi bật: v_1,3 = v_1,2 + v_2,3.\n"
            "- Minh họa chiếc ca nô chạy qua sông có dòng nước chảy xiết: mũi tên ca nô hướng vuông góc bờ sông, dòng nước đẩy ngang => vecto tổng hợp chéo theo Pitago: v_1,3 = √(v_1,2² + v_2,3²).\n"
            "- Bảng 3 trường hợp đặc biệt:\n"
            "   + Cùng hướng: v_1,3 = v_1,2 + v_2,3\n"
            "   + Ngược hướng: v_1,3 = |v_1,2 - v_2,3|\n"
            "   + Vuông góc: v_1,3 = √(v_1,2² + v_2,3²)"
        ),
        "voiceover": (
            "\"Đã bao giờ các bạn tự hỏi: Khi mình vừa đi bộ trên một toa tàu đang chạy, thì vận tốc thực sự của mình đối với người đứng bên đường là bao nhiêu chưa?\n\n"
            "Để giải quyết bài toán này, nhóm mình xin giới thiệu Công thức cộng vận tốc: v_1,3 = v_1,2 + v_2,3.\n\n"
            "Quy ước cực kỳ dễ nhớ nhé: Số 1 là vật chuyển động (chính là bạn), số 2 là hệ quy chiếu chuyển động (đoàn tàu), và số 3 là hệ quy chiếu đứng yên (mặt đất).\n\n"
            "Nếu bạn đi cùng chiều tàu chạy, vận tốc sẽ tăng lên; nếu đi ngược lại, vận tốc sẽ bị trừ bớt. Còn khi gặp trường hợp ca nô băng qua sông bị dòng nước đẩy vuông góc, chúng mình chỉ việc ghép thành tam giác vuông và tính bằng định lý Pitago: v_1,3 = căn bậc hai của v_1,2 bình phương cộng v_2,3 bình phương.\n\n"
            "Cảm ơn thầy cô và các bạn đã theo dõi video thuyết trình của nhóm mình!\""
        ),
        "pedagogy": "Giúp cả lớp nắm vững mẹo đánh số thứ tự 1 - 2 - 3 để không bao giờ bị nhầm lẫn khi làm bài tập trắc nghiệm cộng vận tốc."
    }
]

p_sec2 = doc.add_paragraph()
r_sec2 = p_sec2.add_run("II. CHI TIẾT KỊCH BẢN 5 VIDEO (BÀI 4 & BÀI 5)")
r_sec2.font.name = "Arial"
r_sec2.font.size = Pt(13)
r_sec2.font.bold = True
r_sec2.font.color.rgb = RGBColor(30, 60, 100)

for v in videos:
    h = doc.add_heading(level=2)
    hr = h.add_run(f"★ {v['title']}")
    hr.font.name = "Arial"
    hr.font.size = Pt(12)
    hr.font.bold = True
    hr.font.color.rgb = RGBColor(192, 0, 0)
    
    # Meta info
    p_meta = doc.add_paragraph()
    r_m = p_meta.add_run(f"Thời lượng dự kiến: {v['duration']} | Thành viên thực hiện: {v['members']}")
    r_m.font.name = "Arial"
    r_m.font.italic = True
    r_m.font.size = Pt(9.5)
    r_m.font.color.rgb = RGBColor(80, 80, 80)
    
    # Table for detail
    tbl = doc.add_table(rows=3, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    labels = ["1. Hình ảnh / Đồ họa (Visual)", "2. Lời thoại thuyết trình (Voiceover)", "3. Ghi chú sư phạm & Điểm nhấn"]
    contents = [v["visual"], v["voiceover"], v["pedagogy"]]
    colors = ["E9EEF4", "F8F9FA", "FFF2CC"]
    
    for r_idx in range(3):
        c0 = tbl.rows[r_idx].cells[0]
        c1 = tbl.rows[r_idx].cells[1]
        
        c0.width = Inches(2.2)
        c1.width = Inches(4.7)
        
        c0.text = labels[r_idx]
        set_cell_background(c0, colors[r_idx])
        set_cell_margins(c0, top=100, bottom=100, left=120, right=120)
        p0 = c0.paragraphs[0]
        for run in p0.runs:
            run.font.name = "Arial"
            run.font.bold = True
            run.font.size = Pt(10)
            run.font.color.rgb = RGBColor(30, 50, 80)
            
        c1.text = contents[r_idx]
        set_cell_background(c1, "FFFFFF" if r_idx != 2 else "FFFDF0")
        set_cell_margins(c1, top=100, bottom=100, left=120, right=120)
        p1 = c1.paragraphs[0]
        for run in p1.runs:
            run.font.name = "Arial"
            run.font.size = Pt(9.5)
            if r_idx == 1:
                run.font.italic = True
                
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

# Section III: Các bài mở rộng từ bảng
p_sec3 = doc.add_paragraph()
r_sec3 = p_sec3.add_run("III. PHỤ LỤC: KỊCH BẢN CÁC CHỦ ĐỀ MỞ RỘNG (BÀI 12, 14, 15, 16)")
r_sec3.font.name = "Arial"
r_sec3.font.size = Pt(13)
r_sec3.font.bold = True
r_sec3.font.color.rgb = RGBColor(30, 60, 100)

more_topics = [
    {
        "title": "Bài 12: Chuyển động ném ngang",
        "members": "Lê Gia, Minh Dũng, Lê H Bách, Bảo Yến, Cẩm Nhung",
        "visual": "Mô phỏng thí nghiệm 2 hòn bi A (ném ngang) và B (rơi tự do). Phân tích chuyển động trên hệ trục Oxy: Phương Ox (thẳng đều, vx = v0, tầm xa L = v0 * √(2H/g)), phương Oy (rơi tự do, t = √(2H/g)).",
        "voiceover": "\"Quan sát ảnh chụp hoạt nghiệm hai viên bi: Viên B rơi tự do, còn viên A bị ném ngang. Thật kinh ngạc khi thấy rằng ở mọi thời điểm, cả hai viên bi đều ở cùng một độ cao và chạm đất cùng một lúc! Điều này chứng tỏ: Chuyển động ném ngang theo phương thẳng đứng hoàn toàn giống như một chuyển động rơi tự do!\""
    },
    {
        "title": "Bài 12: Chuyển động ném xiên",
        "members": "Lê Gia, Minh Dũng, Lê H Bách, Bảo Yến, Cẩm Nhung",
        "visual": "Mô phỏng quả bóng ném lên góc α. Phân tích v0 thành v0x = v0.cosα, v0y = v0.sinα. Quỹ đạo parabol. Công thức Tầm cao H = (v0² sin²α)/(2g), Tầm xa L = (v0² sin2α)/g. Góc α = 45° cho tầm xa lớn nhất.",
        "voiceover": "\"Bằng phương pháp phân tích chuyển động, chúng ta tính được Tầm cao H và Tầm xa L của chuyển động ném xiên. Một mẹo nhỏ thú vị: Để vật ném đi xa nhất với cùng một vận tốc ban đầu, góc ném lý tưởng chính là 45 độ!\""
    },
    {
        "title": "Bài 14: Định luật 1 Newton & Quán tính",
        "members": "Quang Huy, Tú Châu, Bảo Yến, Cẩm Nhung",
        "visual": "Chân dung Isaac Newton (1687). Khung định luật: Nếu vật không chịu lực nào hoặc hợp lực bằng 0 => Đứng yên tiếp tục đứng yên, đang chuyển động tiếp tục chuyển động thẳng đều. Minh họa quả cầu treo trên dây cân bằng, tàu vũ trụ Voyager bay vô tận trong không gian.",
        "voiceover": "\"Định luật 1 khẳng định: Lực không phải là nguyên nhân duy trì chuyển động, mà lực là nguyên nhân làm thay đổi vận tốc của vật! Nếu một vật đang bay với vận tốc 3 m/s mà tất cả lực tác dụng biến mất, nó không dừng lại mà sẽ tiếp tục bay thẳng đều với vận tốc 3 m/s mãi mãi!\""
    },
    {
        "title": "Bài 15: Định luật 2 Newton & Khối lượng",
        "members": "Lê Gia, Quang Huy, Bảo Hân, Anh Thư, Tú Châu",
        "visual": "Biểu thức vecto: a = F / m hay F = m.a. Đơn vị 1 N = 1 kg.m/s². Đồ họa so sánh xe tải rỗng và xe tải chở nặng: khối lượng càng lớn, càng khó đổi vận tốc (mức quán tính càng lớn).",
        "voiceover": "\"Định luật 2 Newton cho ta thấy: Gia tốc của một vật tỉ lệ thuận với lực tác dụng và tỉ lệ nghịch với khối lượng của nó. Qua đó, khối lượng chính là đại lượng đặc trưng cho mức quán tính của vật!\""
    },
    {
        "title": "Bài 16: Định luật 3 Newton (Lực và Phản lực)",
        "members": "Tú Châu, Lê H Bách, Bảo Yến, Quang Huy",
        "visual": "Khung 4 đặc điểm: (1) Xuất hiện & mất đi đồng thời; (2) Trực đối (cùng phương, ngược chiều, cùng độ lớn); (3) Đặt vào 2 VẬT KHÁC NHAU => KHÔNG TRIỆT TIÊU NHAU; (4) Cùng loại. Minh họa búa đóng đinh.",
        "voiceover": "\"Trong tương tác, nếu có lực tác dụng thì ắt có phản lực. Tại sao lực và phản lực ngược chiều, cùng độ lớn nhưng lại không triệt tiêu nhau? Vì điểm đặt của chúng nằm ở hai vật hoàn toàn khác nhau!\""
    }
]

for t in more_topics:
    hp = doc.add_paragraph()
    r = hp.add_run(f"• {t['title']} (Thành viên: {t['members']})")
    r.font.name = "Arial"
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0, 102, 153)
    
    pv = doc.add_paragraph()
    rv1 = pv.add_run("   Visual: ")
    rv1.font.bold = True
    pv.add_run(t["visual"])
    
    pvo = doc.add_paragraph()
    rvo1 = pvo.add_run("   Voiceover: ")
    rvo1.font.bold = True
    rvo2 = pvo.add_run(t["voiceover"])
    rvo2.font.italic = True
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

output_file = r"c:\Users\huy83\Downloads\AIvid\Kich_Ban_Thuyet_Trinh_Vat_Ly_10.docx"
doc.save(output_file)
print("SUCCESS: Saved to", output_file)
