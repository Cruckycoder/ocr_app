import streamlit as st
from PIL import Image
import pytesseract
import numpy as np

# Streamlit app
def app():
    st.title("OCR App")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "bmp"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Extract Text"):
            try:
                text = pytesseract.image_to_string(image)
                st.success("Text extracted successfully!")
                st.write(text)
                st.markdown(f"```\n{text}\n```")
                st.button("Copy to Clipboard", on_click=copy_to_clipboard, args=(text,))
            except Exception as e:
                st.error(f"Error: {e}")

def copy_to_clipboard(text):
    # Copy text to clipboard
    pass

if __name__ == "__main__":
    app()
