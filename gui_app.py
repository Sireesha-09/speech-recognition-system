import customtkinter as ctk
import speech_recognition as sr
from tkinter import filedialog
from pydub import AudioSegment
from fpdf import FPDF

# ---------------- THEME ----------------
current_mode = "dark"

def toggle_theme():
    global current_mode

    if current_mode == "dark":
        ctk.set_appearance_mode("light")
        current_mode = "light"
    else:
        ctk.set_appearance_mode("dark")
        current_mode = "dark"

# ---------------- APP SETUP ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("AI Speech Recognition System")
app.geometry("850x600")

# Title
title = ctk.CTkLabel(app, text="AI Speech Recognition System", font=("Arial", 22, "bold"))
title.pack(pady=10)

# Output box
output_box = ctk.CTkTextbox(app, width=800, height=350)
output_box.pack(pady=10)

# ---------------- TRANSCRIBE AUDIO FILE ----------------
def transcribe():

    file_path = filedialog.askopenfilename()

    recognizer = sr.Recognizer()

    try:
        audio = AudioSegment.from_wav(file_path)

        chunk_size = 20000  # 20 seconds
        full_text = ""

        output_box.delete("1.0", "end")

        for i in range(0, len(audio), chunk_size):

            chunk = audio[i:i + chunk_size]
            chunk.export("temp.wav", format="wav")

            with sr.AudioFile("temp.wav") as source:
                audio_data = recognizer.record(source)

                try:
                    text = recognizer.recognize_google(audio_data)

                    full_text += text + " "

                    output_box.insert("end", text + "\n")

                except sr.UnknownValueError:
                    output_box.insert("end", "[Could not understand]\n")

        # Save TXT
        with open("output.txt", "w") as f:
            f.write(full_text)

        # Save PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, full_text)
        pdf.output("speech_report.pdf")

        output_box.insert("end", "\n✅ Saved TXT and PDF successfully!\n")

    except Exception as e:
        output_box.insert("end", str(e))

# ---------------- MICROPHONE INPUT ----------------
def mic_input():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        output_box.insert("end", "\n🎤 Listening...\n")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)

            output_box.insert("end", "\nYou said: " + text + "\n")

        except sr.UnknownValueError:
            output_box.insert("end", "\n❌ Could not understand audio\n")

        except sr.RequestError:
            output_box.insert("end", "\n❌ API Error\n")

# ---------------- BUTTONS ----------------
btn1 = ctk.CTkButton(app, text="📂 Upload Audio & Transcribe", command=transcribe)
btn1.pack(pady=5)

btn2 = ctk.CTkButton(app, text="🎤 Microphone Input", command=mic_input)
btn2.pack(pady=5)

btn3 = ctk.CTkButton(app, text="🌗 Toggle Dark/Light Mode", command=toggle_theme)
btn3.pack(pady=5)

app.mainloop()