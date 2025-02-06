# Logos AI - MVP

This project is an MVP (Minimum Viable Product) for **Logos AI**, a Telegram bot that receives audio files (in MP3 format), transcribes the content, and returns a summary with keywords using the **OpenAI API**.

## 📋 Features

- Receive audio files in MP3 format via Telegram.
- Transcribe the audio content using **Whisper**.
- Summarize the transcribed text and extract keywords using the **OpenAI API**.
- Return the summary directly to the user on Telegram.

---

## 🛠️ Technologies Used

- **Python 3.9+**
- **Telegram Bot API** (via `python-telegram-bot`)
- **OpenAI API** (`openai`)
- **Whisper (OpenAI)** for transcription
- **dotenv** for managing environment variables

---

## 📦 Project Structure

```
logos_ai_mvp/
├── accesses/
│   └── secrets.env           # API keys for Telegram and OpenAI
├── audio_processing/
│   └── transcriber.py        # Audio transcription function
├── summarization/
│   └── summarizer.py         # Function to summarize the transcribed text
├── utils/
│   └── downloader.py         # Function to download audio files from Telegram
├── audio_files/              # Directory where received audio files are stored
├── main.py                   # Main file to run the bot
├── README.md                 # This documentation file
├── requirements.txt          # Project dependencies
```

---

## 🔧 Prerequisites

- **Python 3.9+**
- **FFmpeg** (required for transcription with Whisper)
    - **On Windows:** [Download here](https://ffmpeg.org/download.html) and add to PATH.
    - **On Linux:** `sudo apt-get install ffmpeg`
    - **On Mac:** `brew install ffmpeg`

---

## 🚀 Installation and Execution

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/logos_ai_mvp.git
cd logos_ai_mvp
```

### 2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Configure the `.env` file:
Create the **`accesses/secrets.env`** file with the following variables:
```
OPENAI_API_KEY=your_openai_api_key
TELEGRAM_TOKEN=your_telegram_token
```

### 5. Start the bot:
```bash
python main.py
```

---

## 📲 Testing the Bot

1. On Telegram, send the **`/start`** command to the bot.
2. Send an audio file in **MP3** format.
3. The bot will return the transcribed text, the summary, and the keywords.

---

## ⚠️ Security

**Do not share your API keys publicly.** The `.env` file is configured to protect these sensitive details.

---

## 📚 Possible Improvements

- Add support for different languages during transcription.
- Implement options for short, medium, and long summaries.
- Persist transcriptions and summaries in a local database.

---

## 👥 Contribution

Contributions are welcome! Feel free to open issues and submit pull requests.

---

## 🔖 License

This project is licensed under the MIT License.
