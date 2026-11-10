# 🎬 AIvid - Dự Án Video Bài Giảng Vật Lí 10 Bằng Trí Tuệ Nhân Tạo

Dự án tự động hóa sản xuất video bài giảng môn Vật lí lớp 10 theo phong cách học sinh thuyết trình hiện đại, tương tác trước bảng thông minh (Smartboard) và mô phỏng 3D.

---

## 📌 Các Sản Phẩm Trong Dự Án

### 1. File Video MP4 Hoàn Chỉnh (Full HD 1080p)
- **`Video1_Sample_Huong1_Smartboard.mp4`**: Bài 4 (Phần 1) - Vị trí của vật & Hệ quy chiếu (Thời lượng: ~1p14s).
- **`Video2_DoDichChuyen_QuangDuong.mp4`**: Bài 4 (Phần 2) - Độ dịch chuyển & Phân biệt Quãng đường (Thời lượng: ~1p38s).

### 2. Kịch Bản & Phân Công Nhóm (.docx)
- **`Kich_Ban_Thuyet_Trinh_Vat_Ly_10.docx`**: Tài liệu kịch bản thuyết trình đầy đủ 5 video (Bài 4, Bài 5) và phụ lục (Bài 12, 14, 15, 16) kèm bảng phân công 11 thành viên trong nhóm.

### 3. Bộ Kit Prompt Tạo Chuyển Động Người (Google Flow / Kling / Dreamina)
- **`Huong2_GoogleFlow_Kit.html`**: Giao diện web 1-click copy prompt chuyển động và nghe audio cho từng cảnh.
- **`Huong2_Kit_Video1/`**: Bộ ảnh gốc kèm file audio lẻ và tool tự động ghép clip `merge_flow_clips.py`.

### 4. Tài Nguyên Đồ Họa Bảng Thông Minh
- **`scenes_video1/`**: 5 ảnh gốc AI độ phân giải cao cho Video 1.
- **`scenes_video2/`**: 5 ảnh gốc AI độ phân giải cao cho Video 2.

---

## 🚀 Hướng Dẫn Đồng Bộ & Mở Trên Máy PC Khác

Để tải toàn bộ dự án về máy tính khác của bạn, chỉ cần mở Terminal / Command Prompt / PowerShell và chạy:

```bash
git clone https://github.com/CrashCrystalVN/AIvid.git
cd AIvid
```

### Chạy Render Lại Video Trên PC Khác:
1. Cài đặt các thư viện cần thiết:
   ```bash
   pip install edge-tts imageio-ffmpeg pillow python-docx gTTS
   ```
2. Render Video 1:
   ```bash
   python build_sample_huong1.py
   ```
3. Render Video 2:
   ```bash
   python build_video2.py
   ```

---
*Dự án thực hiện bởi nhóm học sinh: Anh Thư, Hữu Trọng, Thế Mỹ, Tú Châu, Minh Dũng, Bảo Hân, Lê Gia, Lê H Bách, Bảo Yến, Cẩm Nhung, Quang Huy.*
