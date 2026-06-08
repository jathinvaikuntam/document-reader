import streamlit as st
from google import genai
from dotenv import load_dotenv
from PIL import Image
from prompts import PROMPTS
import os



load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ GEMINI_API_KEY not found")
    st.stop()

client = genai.Client(api_key=API_KEY)



def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()



st.set_page_config(
    page_title="Smart Document Reader",
    page_icon="📄",
    layout="wide"
)



with st.sidebar:

    st.title("ℹ️ About")

    st.write("""
    Smart Document Reader

    Upload an image and let
    Gemini Vision analyze it.

    Modes:
    - Handwritten Notes
    - Business Card
    - Receipt
    - Whiteboard
    """)



st.title("📄 Smart Document Reader")
# st.markdown(
#     '<div class="main-title">📄 Smart Document Reader</div>',
#     unsafe_allow_html=True
# )



mode = st.radio(
    "Handwritten Notes" \
    "Business Card" \
    "Receipt" \
    "Whiteboard",
    list(PROMPTS.keys())
)



uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"],
    max_upload_size=5
)

MAX_FILE_SIZE_MB = 5
if uploaded_file is not None:
    file_size_mb = uploaded_file.size / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        st.error(f"❌ File size exceeds {MAX_FILE_SIZE_MB} MB limit.")
        st.stop()



if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

    if st.button("🚀 Process Image"):

        try:

            prompt = PROMPTS[mode]

            with st.spinner("Analyzing image..."):

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        prompt,
                        image
                    ]
                )

                result = response.text

            with col2:
                st.subheader("📌 Result")
                st.markdown(result)

            st.download_button(
                label="⬇️ Download Markdown",
                data=result,
                file_name="output.md",
                mime="text/markdown"
            )

        except Exception as e:
            st.error(f"❌ {e}")

else:
    st.info("📤 Upload an image to begin.")