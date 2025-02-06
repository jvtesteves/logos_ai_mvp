import openai
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
from utils.downloader import baixar_arquivo
from audio_processing.transcriber import transcrever_audio
from summarization.summarizer import gerar_resumo

# Load tokens from the .env file
load_dotenv(dotenv_path="accesses/secrets.env")
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! Send an MP3 audio file for me to transcribe and summarize.")

async def receive_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Download the audio file
    file_path = await baixar_arquivo(update)
    await update.message.reply_text(f"Audio received and saved as {file_path}. Transcribing...")

    # Transcribe the audio
    transcribed_text = transcrever_audio(file_path)
    await update.message.reply_text("Transcription completed. Generating the summary...")

    # Generate the summary and keywords using the OpenAI API
    summary = gerar_resumo(transcribed_text)
    await update.message.reply_text(f"Here is the summary and keywords:\n\n{summary}")

def main():
    # Initialize the bot using the new structure
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Initial command
    application.add_handler(CommandHandler("start", start))

    # Handler for audio files sent by the user
    application.add_handler(MessageHandler(filters.AUDIO, receive_file))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
