🎤 AI Speech Recognition System

A complete AI-powered Speech-to-Text desktop application built using Python.
It supports audio file transcription, real-time microphone input, modern GUI, theme switching, PDF export, and EXE conversion.

🚀 Features

🎧 Speech-to-text from audio files
🎤 Real-time microphone recognition
🧠 Pre-trained Google Speech Recognition API
📂 Long audio support using chunk processing
🖥️ Modern GUI using CustomTkinter
🌗 Dark / Light theme toggle
📄 Export transcription to .txt
📑 Export transcription to .pdf
💻 Convert into installable .exe application

🛠️ Technologies Used

Python 3.10+
SpeechRecognition
Pydub
CustomTkinter
fpdf
FFmpeg
PyInstaller

📁 Project Structure

speech_recognition_system/
│
├── gui_app.py              # Main application (RUN THIS)
├── audio.wav               # Sample audio file
├── output.txt              # Transcription output
├── speech_report.pdf       # PDF report output
├── temp.wav                # Temporary chunk file
├── requirements.txt        # Dependencies
├── README.md               # Documentation
│
├── screenshots/            # Add project images here
├── dist/                   # EXE output (after build)
├── build/                  # PyInstaller build files

⚙️ Installation Guide

1️⃣ Clone Repository
git remote add origin https://github.com/Sireesha-09/speech-recognition-system.git
cd speech-recognition-system
2️⃣ Install Dependencies
pip install SpeechRecognition
pip install pydub
pip install pyaudio
pip install customtkinter
pip install fpdf
3️⃣ Install FFmpeg (IMPORTANT)

Download FFmpeg:

FFmpeg Download

Steps:

Extract ZIP
Copy bin folder path
Add to system PATH
Restart terminal
▶️ How to Run Project
Run GUI Application
python gui_app.py
Run Microphone Feature (inside GUI)

Click:
👉 🎤 Microphone Input button

Run Audio File Transcription

Click:
👉 Upload Audio & Transcribe button

💻 Convert into Desktop App (.EXE)
Step 1 — Install PyInstaller
pip install pyinstaller
Step 2 — Build EXE
pyinstaller --onefile --windowed gui_app.py
Output File
dist/gui_app.exe

Now your project becomes a downloadable software application.

🎯 How It Works
User uploads audio file OR uses microphone
Audio is split into chunks for accuracy
Each chunk is processed using Google Speech API
Text is combined into final transcription
Output is shown in GUI
Results saved as:
.txt file
.pdf report

📌 Example Output
Hello everyone welcome to speech recognition system
This project converts speech into text using AI

🌗 UI Features
Dark Mode (default)
Light Mode toggle button
Clean modern interface
Large text display window

🧠 Key Learnings
Speech recognition using AI APIs
Audio processing & chunking
GUI development in Python
File handling (TXT & PDF)
Real-world AI application design
Desktop software packaging

📈 Future Enhancements
🌍 Multi-language transcription
🧠 AI summarization of speech
👤 Speaker identification
☁️ Web deployment (Flask)
📱 Mobile app version
🔐 Cloud storage integration
🏆 Resume Highlights

✔ Built AI Speech Recognition System using Python
✔ Implemented real-time and file-based speech-to-text conversion
✔ Designed modern GUI with dark/light theme support
✔ Integrated audio chunking for long audio processing
✔ Generated downloadable PDF reports
✔ Converted application into standalone EXE software

⚠️ Important Notes

Audio must be in .wav format (PCM 16-bit recommended)
FFmpeg must be installed for audio processing
Internet required for Google Speech API

👨‍💻 Author-Sireesha Gorantla

Internship Project — Speech Recognition System (AI + Python)
Developed as part of CODTECH Internship Task
