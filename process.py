import whisper
import warnings

# Transcribe audio
def transcribe_audio(audio_file_path):
    try:
        # Suppress warnings
        warnings.filterwarnings("ignore", category=FutureWarning)
        # Load Whisper model
        model = whisper.load_model("base")  # You can use "small", "medium", or "large" models if needed

        # Transcribe the audio
        result = model.transcribe(audio_file_path, fp16=False)

        # Get the transcript text
        transcript = result['text']

        print(f"Transcription complete:\n{transcript}")
        return transcript  # Only return the transcript
    except Exception as e:
        print(f"Error in transcription: {e}")
        return None  # Return None if there's an error


########################################################################################################################



from elevenlabs import save
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
        api_key="sk_1e0d0b2607878573dfbf1e88bbeb09d023a15dd2223b9e9b"
    )


#Generate whisper-style audio
def generate_whisper_audio(transcript):
    try:
        # Generate whisper-style audio
        audio = client.generate(
            text=transcript,
            voice="Brian",
            model="eleven_multilingual_v2",
        )

        output_audio_path = "whisper_audio.mp3"
        save(audio, output_audio_path)

        print(f"Whisper audio saved to {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"Error generating whisper audio: {e}")
        return None


""" # As an alternative to the ElevenLabs API, you can use gTTS to generate whisper-like audio, 
#but it may not be as realistic as the ElevenLabs API.

from gtts import gTTS
import os

def generate_whisper_audio(transcript):
    try:
        # Generate speech using gTTS
        tts = gTTS(text=transcript, lang='pt', slow=False)  # Adjust `lang` for the language of the transcript

        # Save audio to file
        output_audio_path = "whisper_audio.mp3"
        tts.save(output_audio_path)

        print(f"Whisper-like audio saved to {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"Error generating whisper audio with gTTS: {e}")
        return None

"""

########################################################################################################################



import subprocess

def merge_audio_with_video(video_file_path, audio_file_path, output_file_path):
    try:
        # Define the FFmpeg command
        cmd = f'ffmpeg -y -i {audio_file_path} -r 30 -i {video_file_path} -filter:a aresample=async=1 -c:a flac -c:v copy {output_file_path}'

        # Run the FFmpeg command using subprocess
        subprocess.call(cmd, shell=True)

        print(f"Merged video saved to {output_file_path}")
        return output_file_path
    except Exception as e:
        print(f"Error merging audio with video: {e}")
        return None

