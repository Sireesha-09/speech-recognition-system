import speech_recognition as sr
from pydub import AudioSegment

# Load audio file
audio = AudioSegment.from_wav("audio.wav")

# Split into 20-second chunks
chunk_length_ms = 20000

recognizer = sr.Recognizer()

full_text = ""

print("\nProcessing Audio...\n")

for i in range(0, len(audio), chunk_length_ms):

    chunk = audio[i:i + chunk_length_ms]

    chunk_filename = f"chunk_{i}.wav"

    chunk.export(chunk_filename, format="wav")

    with sr.AudioFile(chunk_filename) as source:

        audio_listened = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_listened)

            start_time = i // 1000
            end_time = (i + chunk_length_ms) // 1000

            output = f"[{start_time}s - {end_time}s] {text}"

            print(output)

            full_text += output + "\n"

        except sr.UnknownValueError:
            print("Could not understand chunk")

        except sr.RequestError as e:
            print("API Error:", e)

# Save transcription
with open("transcription.txt", "w") as file:
    file.write(full_text)

print("\n========== FINAL TRANSCRIPTION ==========\n")
print(full_text)

print("\nTranscription saved to transcription.txt")