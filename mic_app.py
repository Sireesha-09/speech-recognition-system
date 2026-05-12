import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak something...")

    recognizer.adjust_for_ambient_noise(source)

    audio = recognizer.listen(source)

    print("⏳ Recognizing...")

    try:
        text = recognizer.recognize_google(audio)

        print("\n📝 You said:")
        print(text)

        # Save to file
        with open("mic_output.txt", "w") as f:
            f.write(text)

        print("\n✅ Saved to mic_output.txt")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")

    except sr.RequestError:
        print("❌ Internet/API error")