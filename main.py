from download import download_audio
from process import transcribe_audio, generate_whisper_audio, merge_audio_with_video
from effects import add_asmr_effects
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

                # Part 4: Add ASMR effects to the whisper-like audio
                rain_audio_path = "rain.mp3"  # Path to your rain audio file
                tapping_audio_path = "tapping.mp3"  # Path to your tapping audio file
                asmr_audio_path = add_asmr_effects(whisper_audio_path, rain_audio_path, tapping_audio_path)
                if asmr_audio_path:
                    print(f"ASMR-enhanced audio saved at: {asmr_audio_path}")

                    # Part 5: Merge the ASMR-enhanced audio back with the original video
                    video_file_path = "video.mp4.m4a"  # Path to the downloaded video
                    output_file_path = "final_video_with_audio.mp4"

                    merged_video_path = merge_audio_with_video(video_file_path, asmr_audio_path, output_file_path)
                    if merged_video_path:
                        print(f"Final video saved to {merged_video_path}")
                    else:
                        print("Failed to merge audio with video.")
                else:
                    print("Failed to add ASMR effects.")
            else:
                print("Failed to generate whisper-like audio.")
        else:
            print("Failed to transcribe audio.")
    else:
        print("Failed to download audio from YouTube.")
