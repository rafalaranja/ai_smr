from process import transcribe_audio, generate_whisper_audio
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

# Main
if __name__ == "__main__":
    # Part 1: Upload a video file locally
    video_file_path = input("Enter the path to the video file: ")

    if not os.path.exists(video_file_path):
        print("The provided file path does not exist.")
    else:
        # Convert video file to audio
        audio_file_path = video_file_path.replace(".mp4", ".wav")  # Assuming input is MP4

        try:
            print("Extracting audio from the video...")
            video_clip = VideoFileClip(video_file_path)
            video_clip.audio.write_audiofile(audio_file_path)
            print(f"Audio extracted and saved as: {audio_file_path}")
        except Exception as e:
            print(f"Error extracting audio: {e}")
            exit()

        # Part 2: Transcribe audio to text
        transcript = transcribe_audio(audio_file_path)
        if transcript:
            # Save the transcript to a file
            transcript_file_path = video_file_path.replace(".mp4", "_transcript.txt")
            try:
                with open(transcript_file_path, "w", encoding="utf-8") as file:
                    file.write(transcript)
                print(f"Transcription saved to file: {transcript_file_path}")
            except Exception as e:
                print(f"Error saving transcription to file: {e}")

            # Part 3: Generate whisper-like audio
            generate_whisper_audio(transcript)  # Generate whisper-style audio from the transcript

        else:
            print("Failed to transcribe audio.")
