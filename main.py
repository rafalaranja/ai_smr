from download import download_audio
from process import transcribe_audio, generate_whisper_audio
import os

# Main
if __name__ == "__main__":
    # Part 1: Input YouTube video URL
    youtube_url = input("Enter the YouTube video URL: ")

    # Download audio from YouTube video
    audio_file_path = download_audio(youtube_url)

    if audio_file_path and os.path.exists(audio_file_path):
        # Part 2: Transcribe audio to text
        transcript = transcribe_audio(audio_file_path)
        if transcript:
            # Save the transcript to a file
            transcript_file_path = "transcript.txt"  # Save in the current directory
            try:
                with open(transcript_file_path, "w", encoding="utf-8") as file:
                    file.write(transcript)
                print(f"Transcription saved to file: {transcript_file_path}")
            except Exception as e:
                print(f"Error saving transcription to file: {e}")

            # Part 3: Generate whisper-like audio
            whisper_audio_path = generate_whisper_audio(transcript)
            if whisper_audio_path:
                print(f"Whisper-like audio generated and saved at: {whisper_audio_path}")
            else:
                print("Failed to generate whisper-like audio.")
        else:
            print("Failed to transcribe audio.")
    else:
        print("Failed to download audio from YouTube.")
