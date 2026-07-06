# 🎙️ Speech to Text with OpenAI Whisper

A simple Python project that converts Persian speech into text using **OpenAI Whisper**.

## ✨ Features

- Speech-to-Text transcription
- Persian (`fa`) language support
- Save transcription to a text file
- Easy to integrate into automation workflows
- GPU acceleration (CUDA) support

## 🛠️ Tech Stack

- Python
- OpenAI Whisper
- PyTorch
- CUDA (Optional)

## 📂 Project Structure

```
.
├── test.py
├── test.wav
├── output.txt
└── README.md
```

## 🚀 Installation

```bash
pip install openai-whisper
```

## ▶️ Usage

```python
import whisper

model = whisper.load_model("base")

result = model.transcribe(
    "test.wav",
    language="fa"
)

print(result["text"])
```

Run:

```bash
python test.py
```

## 📄 Output

```
سلام، این یک تست برای تبدیل گفتار به متن با استفاده از مدل Whisper است.
```

The transcription is also saved to:

```
output.txt
```

## 💡 Future Plans

- Integration with n8n
- AI Automation workflows
- Telegram Bot
- REST API
- Speaker diarization

## 👨‍💻 Author

**Kaveh**

- LinkedIn: https://www.linkedin.com/in/its-kaveh/
- GitHub: https://github.com/kaveh-a
