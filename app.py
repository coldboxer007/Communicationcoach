import streamlit as st
import os
import tempfile
from engines.local_engine import process_local
from engines.cloud_engine import process_cloud
from utils.visuals import create_spider_chart, create_bar_chart, highlight_text

st.set_page_config(page_title="Communication Coach", layout="wide")

def save_uploaded_file(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return None

# Sidebar
st.sidebar.title("Configuration")
engine_mode = st.sidebar.radio("Scoring Engine", ["Gemini AI (Cloud)", "Local ML (Offline)"])

api_key = ""
if engine_mode == "Gemini AI (Cloud)":
    api_key = st.sidebar.text_input("Gemini API Key", type="password")
    if not api_key:
        st.sidebar.warning("Please enter your Gemini API Key.")

st.title("🗣️ Communication Coach")
st.markdown("Upload your self-introduction audio or paste text to get a rubric-based score.")

# Input Area
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Upload Audio (MP3/WAV)", type=["mp3", "wav"])
with col2:
    text_input = st.text_area("Or Paste Transcript Here", height=150)

if st.button("Analyze"):
    if not uploaded_file and not text_input:
        st.error("Please provide audio or text input.")
    else:
        with st.spinner(f"Analyzing using {engine_mode}..."):
            # Save audio if present
            audio_path = None
            if uploaded_file:
                audio_path = save_uploaded_file(uploaded_file)
            
            # Process
            result = {}
            if engine_mode == "Gemini AI (Cloud)":
                result = process_cloud(audio_path, text_input, api_key)
            else:
                result = process_local(audio_path, text_input)
            
            # Cleanup temp file
            if audio_path and os.path.exists(audio_path):
                os.remove(audio_path)
                
            # Display Results
            if "error" in result:
                st.error(result["error"])
            else:
                # Top: Overall Score
                st.header(f"Overall Score: {result.get('overall_score', 0)}/100")
                
                # Spider Chart
                scores = result.get("category_scores", {})
                fig_spider = create_spider_chart(scores)
                st.plotly_chart(fig_spider, use_container_width=True)
                
                # Middle: Category Columns
                cols = st.columns(5)
                categories = ["Content", "Speech", "Grammar", "Clarity", "Engagement"]
                for i, cat in enumerate(categories):
                    with cols[i]:
                        st.metric(cat, f"{scores.get(cat, 0)}")
                
                # Visuals: Bar Chart
                st.subheader("Score Comparison")
                fig_bar = create_bar_chart(scores)
                st.plotly_chart(fig_bar, use_container_width=True)
                
                # Transcript with Highlights
                st.subheader("Transcript Analysis")
                transcript = result.get("transcript", "")
                fillers = result.get("fillers_found", [])
                keywords = result.get("keywords_found", [])
                
                if transcript:
                    highlighted_html = highlight_text(transcript, fillers, keywords)
                    st.markdown(highlighted_html, unsafe_allow_html=True)
                    st.caption("Green: Keywords | Red: Filler Words")
                
                # Bottom: Detailed Feedback
                st.subheader("Detailed Feedback")
                feedback = result.get("feedback", {})
                for cat in categories:
                    with st.expander(f"{cat} Feedback"):
                        st.write(feedback.get(cat, "No feedback available."))

