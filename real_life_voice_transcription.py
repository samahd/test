import streamlit as st
import speech_recognition as sr

def transcribe_audio():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        st.write("Listening...")

        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        st.write("Transcription:")
        st.write(text)
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand audio.")
    except sr.RequestError as e:
        st.write(f"Could not request results from Google Speech Recognition service; {e}")

def main():
    st.title("Real-time Voice Transcription App")

    st.write("Click on the button below and start speaking to get the transcription.")

    if st.button("Start Transcription"):
        transcribe_audio()

if __name__ == "__main__":
    main()
