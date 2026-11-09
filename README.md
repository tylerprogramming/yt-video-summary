# YouTube Video Summarizer/Translator

> **Updated 2026-11.** The video used `whisper-1` and `gpt-4o`. OpenAI removes `gpt-4o` on 2027-01-14 and `whisper-1` on 2027-02-26 ([deprecations](https://developers.openai.com/api/docs/deprecations)), so the code now uses `gpt-transcribe` and `gpt-6-luna`. Everything else matches the video.

## How to Install
1. git clone https://github.com/tylerprogramming/yt-video-summary.git
2. `cd yt-video-summary`
3. type `pip install -r requirements.txt` in terminal (Python 3.10 to 3.12; `pyautogen==0.2.28` does not support 3.13)
4. add your YouTube URL into *main.py*
5. copy `.env.example` to `.env` and put your OpenAI key in it (`.env` is gitignored, so the key stays out of git)
6. run `python main.py`

You also need `ffmpeg` on your PATH: yt-dlp uses it to extract the m4a audio and pydub uses it to split it.

If the download step fails, YouTube has likely changed something that the pinned `yt-dlp==2024.5.27` cannot handle. Run `pip install -U yt-dlp`.
