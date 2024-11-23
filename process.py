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

# api_key : sk_a082c25a00c3c6e00f030a864c1a6688ca47efadcf306e06

from elevenlabs import save
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
        api_key="sk_a082c25a00c3c6e00f030a864c1a6688ca47efadcf306e06"  # Defaults to ELEVEN_API_KEY
    )


#Generate whisper-style audio
def generate_whisper_audio(transcript):
    try:
        # Generate whisper-style audio
        audio = client.generate(
            text=transcript,
            voice="Brian",
            model="eleven_multilingual_v2"
        )

        output_audio_path = "whisper_audio.mp3"
        save(audio, output_audio_path)

        print(f"Whisper audio saved to {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"Error generating whisper audio: {e}")
        return None
