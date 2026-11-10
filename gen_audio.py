import asyncio
import edge_tts
import os
import subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

VOICE = "vi-VN-HoaiMyNeural" # Giọng nữ ấm áp, rõ ràng chuẩn giáo dục

segments = [
    {
        "id": "seg1",
        "text": "Chào thầy cô và các bạn! Hãy cùng nhóm mình bắt đầu bằng một tình huống thực tế nhé: Một chiếc ô tô đi qua ngã tư với tốc độ 36 km trên giờ. Sau 10 giây, xe đi được quãng đường 100 mét. Câu hỏi đặt ra là: Liệu chỉ biết quãng đường 100 mét, chúng mình có thể xác định chính xác xe đang ở đâu trên bản đồ không?"
    },
    {
        "id": "seg2",
        "text": "Chắc chắn là chưa thể rồi đúng không? Để biết chính xác vị trí, chúng ta cần một hệ tọa độ gắn với vật mốc. Trong đời sống, các bạn thường thấy hệ tọa độ địa lí với trục Ô-xơ theo hướng Tây - Đông và trục Ô-y theo hướng Bắc - Nam."
    },
    {
        "id": "seg3",
        "text": "Khi chúng mình kết hợp hệ tọa độ này cùng với mốc thời gian và một chiếc đồng hồ bấm giờ, ta sẽ có một hệ quy chiếu hoàn chỉnh. Nếu xe chỉ chạy thẳng trên một đường, chúng mình chỉ cần chọn duy nhất một trục Ô-xơ trùng với đường đi. Và khi kích thước xe rất nhỏ so với quãng đường 100 mét, tụi mình hoàn toàn có thể coi nó là một chất điểm!"
    },
    {
        "id": "seg4",
        "text": "Câu hỏi tương tác cho cả lớp: Khi nào độ dài quãng đường cho phép chúng ta coi một vật chuyển động là một chất điểm?"
    }
]

async def gen_audio():
    for seg in segments:
        file_path = f"audio_{seg['id']}.mp3"
        comm = edge_tts.Communicate(seg['text'], VOICE, rate="+0%")
        await comm.save(file_path)
        print(f"Generated {file_path}")

asyncio.run(gen_audio())
print("All audio generated!")
