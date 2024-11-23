from pytubefix import YouTube
from moviepy import AudioFileClip

# Download audio from YouTube video
def download_audio(youtube_url):
    try:
        # Download YouTube video as audio-only
        yt = YouTube(youtube_url)
        stream = yt.streams.get_audio_only()
        audio_file_path = stream.download(filename="video.mp4")

        # Convert to WAV for further processing
        audio_clip = AudioFileClip(audio_file_path)
        output_audio_path = "audio.wav"
        audio_clip.write_audiofile(output_audio_path)

        print(f"Audio downloaded and saved as {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"Error in download_audio: {e}")
        return None