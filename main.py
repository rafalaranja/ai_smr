from download import download_audio

# Main
if __name__ == "__main__":
    youtube_url = input("Enter YouTube URL: ")
    audio_path = download_audio(youtube_url)
    if audio_path:
        print(f"Downloaded audio file path: {audio_path}")
    else:
        print("Failed to download audio.")