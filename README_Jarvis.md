
# 🧠 Jarvis - Virtual Voice Assistant

Jarvis is a Python-based virtual voice assistant capable of recognizing voice commands, responding via speech, playing music, opening websites, fetching news, and answering general queries using OpenAI's GPT model. It's a beginner-friendly voice recognition project combining AI with real-world automation.

---

## 🔧 Features

- 🎤 Voice recognition using Google Speech Recognition
- 🗣️ Speech output using Google Text-to-Speech (gTTS) and PyGame
- 🌐 Open websites like Google, YouTube, Instagram, etc.
- 🎵 Play songs from a predefined music library
- 📰 Fetch and read out top news headlines using NewsAPI
- 🤖 AI-based query handling via OpenAI (ChatGPT)
- 🛠️ Wake-word based activation ("Jarvis")

---

## 🧪 Tech Stack

- Python 3.x
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS](https://pypi.org/project/gTTS/)
- [pygame](https://pypi.org/project/pygame/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [OpenAI API](https://platform.openai.com/)
- [NewsAPI](https://newsapi.org/)
- [pyaudio](https://pypi.org/project/PyAudio/) *(for microphone input)*

---

## 🗂️ Project Structure

```
Jarvis/
│
├── main.py         # Main voice assistant logic
├── client.py       # Example usage of OpenAI API (test script)
├── musicLibrary.py # Dictionary storing song names and YouTube URLs
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

### 2. Install Dependencies

Make sure Python 3.x is installed.

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
SpeechRecognition
gTTS
pygame
pyttsx3
requests
openai
pyaudio
```

> Note: If installing `pyaudio` fails, use:
```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🔑 API Keys Setup

1. **OpenAI API Key**  
   Sign up at [OpenAI](https://platform.openai.com/) and generate an API key. Replace the key in `main.py` and `client.py`:
   ```python
   openai.api_key = "your-openai-api-key"
   ```

2. **NewsAPI Key**  
   Get an API key from [https://newsapi.org/](https://newsapi.org/) and insert it in `main.py`:
   ```python
   newsapi = "your-newsapi-key"
   ```

3. **Music Library Setup**  
   Update `musicLibrary.py` with a dictionary like:
   ```python
   music = {
       "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
       "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA"
   }
   ```

---

## ▶️ Usage

Run the assistant:

```bash
python main.py
```

- It listens for the wake word **"Jarvis"**
- On activation, it accepts the next voice command and responds accordingly

---

## 💡 Sample Commands

- "Jarvis" → activates the assistant  
- "Open Google"  
- "Play believer"  
- "What's the news?"  
- "What is coding?" (uses OpenAI)  

---

## ❗ Troubleshooting

- Make sure your microphone works and is not in use by another app.
- If `pyaudio` installation fails, use `pipwin` as mentioned.
- The internet is required for OpenAI, NewsAPI, and Google speech recognition.

---

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and share it.

---

## 🤝 Contribution

Pull requests and suggestions are welcome! Open an issue to discuss improvements.
