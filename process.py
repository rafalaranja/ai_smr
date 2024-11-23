from moviepy import VideoFileClip, AudioFileClip

def merge_audio_with_video(video_file_path, audio_file_path, output_file_path):
    try:
        # Load video and audio
        video = VideoFileClip(video_file_path)
        audio = AudioFileClip(audio_file_path)

        # Check if FPS is valid
        fps = video.fps if video.fps else 24  # Default to 24 if FPS is None or invalid

        # Set the new audio to the video
        video_with_audio = video.set_audio(audio)

        # Write the final video to the output file
        video_with_audio.write_videofile(output_file_path, codec="libx264", audio_codec="aac", fps=fps)

        print(f"Merged video saved to {output_file_path}")
        return output_file_path
    except Exception as e:
        print(f"Error merging audio with video: {e}")
        return None
