import asyncio
import edge_tts

VOICE = "vi-VN-HoaiMyNeural"
TEXT = "Chào thầy cô và các bạn! Hãy cùng nhóm mình bắt đầu bằng một tình huống thực tế nhé!"

async def main():
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save("test_audio.mp3")
    print("DONE_TTS")

if __name__ == "__main__":
    asyncio.run(main())
