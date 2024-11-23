from download import download_audio

import whisper

import whisper

def transcribe_audio(audio_file_path):
    try:
        # Load Whisper model
        model = whisper.load_model("base")  # You can use "small", "medium", or "large" models if needed

        # Transcribe the audio
        result = model.transcribe(audio_file_path)

        # Get the transcript text
        transcript = result['text']

        print(f"Transcription complete:\n{transcript}")
        return transcript  # Only return the transcript
    except Exception as e:
        print(f"Error in transcription: {e}")
        return None  # Return None if there's an error


# Main
if __name__ == "__main__":

    # Part 1: Download audio from YouTube video
    youtube_url = input("Enter YouTube URL: ")
    audio_path = download_audio(youtube_url)
    if audio_path:
        print(f"Downloaded audio file path: {audio_path}")
    else:
        print("Failed to download audio.")

    # Part 2: Transcribe audio to text
    transcript = transcribe_audio(audio_path)
    if transcript:
        print(f"Transcription saved as {transcript}")
    else:
        print("Failed to transcribe audio.")