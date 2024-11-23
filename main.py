from pytube import YouTube
from moviepy.audio import AudioClip


def download_audio(youtube_url):
    try:
        # Download YouTube video as audio-only
        yt = YouTube(youtube_url)
        stream = yt.streams.filter(only_audio=True).first()
        audio_file_path = stream.download(filename="audio.mp4")

        # Convert to WAV for further processing
        audio_clip = AudioClip.AudioClip(audio_file_path)
        output_audio_path = "audio.wav"
        audio_clip.write_audiofile(output_audio_path)

        print(f"Audio downloaded and saved as {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"Error in download_audio: {e}")
        return None

# Main

if __name__ == "__main__":
    youtube_url = input("Enter YouTube URL: ")
    audio_path = download_audio(youtube_url)
    if audio_path:
        print(f"Downloaded audio file path: {audio_path}")
    else:
        print("Failed to download audio.")


