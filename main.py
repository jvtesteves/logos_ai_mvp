import openai
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
from utils.downloader import download_file
from audio_processing.transcriber import transcribe_audio
from summarization.summarizer import generate_summary

# Load tokens from the .env file
load_dotenv(dotenv_path="accesses/secrets.env")
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! Send an MP3 audio file for me to transcribe and summarize.\n"
        "You can choose the size of the summary using the following commands:\n"
        "/summary_short - For a short summary\n"
        "/summary_medium - For a medium summary\n"
        "/summary_long - For a long summary"
    )

async def set_summary_size(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Set the summary size based on the command
    command = update.message.text.lower()
    if "/summary_short" in command:
        context.user_data["summary_size"] = "short"
        await update.message.reply_text("Summary size set to **short**.")
    elif "/summary_medium" in command:
        context.user_data["summary_size"] = "medium"
        await update.message.reply_text("Summary size set to **medium**.")
    elif "/summary_long" in command:
        context.user_data["summary_size"] = "long"
        await update.message.reply_text("Summary size set to **long**.")

async def receive_audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Step 1: Download the audio file
    file_path = await download_file(update)
    await update.message.reply_text(f"Audio received and saved as {file_path}. Transcribing the audio...")

    try:
        # Step 2: Transcribe the audio
        transcribed_text = transcribe_audio(file_path)
        await update.message.reply_text("Transcription completed successfully.")

        # Step 3: Check the user-selected summary size or default to medium
        summary_size = context.user_data.get("summary_size", "medium")
        await update.message.reply_text(f"Generating a {summary_size} summary...")

        # Step 4: Generate the summary
        summary_with_keywords = generate_summary(transcribed_text, summary_size)

        # Step 5: Send the summary and keywords
        await update.message.reply_text(f"**Summary:**\n{summary_with_keywords}", parse_mode="Markdown")

    except Exception as e:
        await update.message.reply_text("An error occurred during the process. Please try again.")
        print(f"Error: {e}")

def main():
    # Initialize the bot using the new structure
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Initial command
    application.add_handler(CommandHandler("start", start))

    # Commands to select summary size
    application.add_handler(CommandHandler("summary_short", set_summary_size))
    application.add_handler(CommandHandler("summary_medium", set_summary_size))
    application.add_handler(CommandHandler("summary_long", set_summary_size))

    # Handler for audio files sent by the user
    application.add_handler(MessageHandler(filters.AUDIO, receive_audio))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
