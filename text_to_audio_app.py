import streamlit as st
from gtts import gTTS
def main():

    def text_to_audio(text):
        tts = gTTS(text)
        audio_path = "output.mp3"
        tts.save(audio_path)
        return audio_path

    st.title("Text-to-Audio")

    text = st.text_input("Enter Text")
    if st.button("Generate Audio"):
        audio_path = text_to_audio(text)
        st.audio(audio_path, format="audio/mp3")
        st.download_button("Download Audio", audio_path, file_name="output.mp3")
