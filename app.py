import streamlit as st
def main():
    st.title("ML Utility Tool")

    page = st.radio("Select a Feature", [
        "Text-to-Audio", "Audio-to-Text"
    ])

    if page == "Text-to-Audio":
        from text_to_audio_app import main
        main()
    elif page == "Audio-to-Text":
        from audio_to_text_app import main
        main()

    
if __name__ == "__main__":
    main()
