from pydub import AudioSegment

def add_asmr_effects(input_audio_path, rain_audio_path="rain.mp3", tapping_audio_path="tapping.mp3"):
    try:
        # Load the main audio
        audio = AudioSegment.from_file(input_audio_path)

        # Load the rain and tapping audio files
        rain_audio = AudioSegment.from_file(rain_audio_path)
        tapping_audio = AudioSegment.from_file(tapping_audio_path)

        # Adjust the duration of rain and tapping audio to match the main audio
        def match_duration(effect_audio, target_duration):
            loops = target_duration // len(effect_audio) + 1
            effect_audio = (effect_audio * loops)[:target_duration]  # Loop and trim
            return effect_audio

        rain_audio = match_duration(rain_audio, len(audio))
        tapping_audio = match_duration(tapping_audio, len(audio))

        # Adjust the volume levels
        tapping_audio = tapping_audio + 12  # Increase tapping volume by 12 dB

        # Overlay rain and tapping onto the main audio
        combined_audio = audio.overlay(rain_audio).overlay(tapping_audio)

        # Save the ASMR-enhanced audio
        output_audio_path = "asmr_audio.wav"
        combined_audio.export(output_audio_path, format="wav")

        print(f"ASMR effects added and saved as {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"Error in add_asmr_effects: {e}")
        return None
