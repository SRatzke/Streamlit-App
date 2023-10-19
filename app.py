import streamlit as st
import pdfplumber
from io import BytesIO

# Pfad zu deinem Bild
image_path = ".\Cognizant_Social_Logo.jpg"

# Bild anzeigen
st.image(image_path, use_column_width=True)

st.title('PDF Text Extractor')

uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        total_pages = len(pdf.pages)
        st.write(f"Total Pages: {total_pages}")

        page = st.number_input(label="Enter Page Number", min_value=1, max_value=total_pages, step=1)

        if st.button("Extract Text"):
            page_object = pdf.pages[page - 1]
            text = page_object.extract_text()
            st.text_area("Text", text, height=500)