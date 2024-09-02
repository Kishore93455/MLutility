def main():
    import speech_recognition as sr
    import streamlit as st
    
    def audio_to_text(audio_file):
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio)

    st.title("Audio-to-Text")

    audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3"])
    if audio_file is not None:
        st.audio(audio_file, format="audio/mp3")
        if st.button("Convert to Text"):
            text = audio_to_text(audio_file)
            st.write(text)

