#Flask Backend

from flask import Flask, request, render_template, send_file
import os
from download import download_audio
from process import transcribe_audio, generate_whisper_audio, merge_audio_with_video
from effects import add_asmr_effects

app = Flask(__name__)


# Route for homepage (index page with input form)
@app.route('/')
def index():
    return render_template('index.html')


# Route to process the video
@app.route('/process', methods=['POST'])
def process_video():
    # Get YouTube URL from form
    youtube_url = request.form['youtube_url']
    print(f"Received YouTube URL: {youtube_url}")


    # Step 1: Download audio from YouTube video (returns path to audio file)
    audio_file_path = download_audio(youtube_url)
    print(f"Downloaded audio to: {audio_file_path}")
    if not audio_file_path or not os.path.exists(audio_file_path):
        return "Failed to download audio from YouTube", 400

    # Step 2: Transcribe the audio to text (returns transcript as text)
    transcript = transcribe_audio(audio_file_path)
    print(f"Transcript: {transcript}")
    if not transcript:
        return "Failed to transcribe audio", 400

    # Step 3: Generate whisper-like audio based on transcript
    whisper_audio_path = generate_whisper_audio(transcript)
    print(f"Generated whisper-like audio to: {whisper_audio_path}")
    if not whisper_audio_path:
        return "Failed to generate whisper-like audio", 400

    # Step 4: Add ASMR effects to the whisper-like audio
    rain_audio_path = "asmr_sounds/rain.mp3"  # Path to your rain audio file (update as needed)
    tapping_audio_path = "asmr_sounds/tapping.mp3"  # Path to your tapping audio file (update as needed)
    asmr_audio_path = add_asmr_effects(whisper_audio_path, rain_audio_path, tapping_audio_path)
    print(f"Added ASMR effects to: {asmr_audio_path}")
    if not asmr_audio_path:
        return "Failed to add ASMR effects", 400

    # Step 5: Merge the ASMR-enhanced audio with the original video
    video_file_path = "video.mp4"  # Assuming the video file was also downloaded (or stored somewhere)
    output_file_path = "final_video_with_audio.mp4"
    merged_video_path = merge_audio_with_video(video_file_path, asmr_audio_path, output_file_path)
    print(f"Merged audio with video to: {merged_video_path}")
    if not merged_video_path:
        return "Failed to merge audio with video", 400

    # Return the final video as an attachment
    return send_file(merged_video_path, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)

