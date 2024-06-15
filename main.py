import os
from dotenv import load_dotenv

from youtube.YouTubeAudioDownloader import YouTubeAudioDownloader
from youtube.AudioTranscriber import AudioTranscriber
from youtube.AutoGenInteraction import AutoGenInteraction

load_dotenv()


def main():
    url = 'https://www.youtube.com/watch?v=zjkBMFhNj_g'
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # gives you the filename from yt video
    downloader = YouTubeAudioDownloader(url)
    filename = downloader.download_audio()
    print(f"Downloaded and saved audio (m4a) as: {filename}")

    # transcribes the audio
    transcriber = AudioTranscriber(api_key=openai_api_key)
    transcription = transcriber.transcribe_audio(filename)
    print("Transcription completed.")

    # ai agents summarize/translate
    autogen_interaction = AutoGenInteraction(api_key=openai_api_key, transcription=transcription)
    autogen_interaction.initiate_chat()
    print("Chat completed.")


if __name__ == "__main__":
    main()
