import whisper

def transcribe_audio(file_path: str) -> str:
    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio
    result = model.transcribe(file_path)

    print("Transcription completed.")
    return result['text']
