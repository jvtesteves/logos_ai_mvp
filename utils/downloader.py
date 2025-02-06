import os
from telegram import Update

async def download_file(update: Update) -> str:
    # Retrieve the audio file sent by the user
    audio_file = await update.message.audio.get_file()

    # Define the path where the file will be saved
    file_path = "audio_files/received_audio.mp3"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Download the audio file
    await audio_file.download_to_drive(file_path)
    print(f"Audio successfully downloaded: {file_path}")
    return file_path
