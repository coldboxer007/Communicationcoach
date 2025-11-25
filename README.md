# 🗣️ Communication Coach

**Communication Coach** is an AI-powered web application designed to analyze student self-introductions and provide a comprehensive, rubric-based score (0-100). It helps users improve their speaking skills by evaluating content, speech rate, grammar, clarity, and engagement.

## 🚀 Key Features

### 🧠 Dual-Engine Architecture
The app features two distinct scoring engines to balance accuracy, privacy, and accessibility:

1.  **Gemini AI (Cloud Mode)**
    *   **Powered by**: Google Gemini Flash Lite model.
    *   **Capabilities**: Deep semantic understanding, flow analysis, and nuanced grammar checking.
    *   **Best for**: High-accuracy feedback and logical structure evaluation.

2.  **Local ML (Offline Mode)**
    *   **Powered by**: OpenAI Whisper, Sentence Transformers, LanguageTool, and VADER.
    *   **Capabilities**: Runs entirely on your device. Calculates speech rate, detects filler words, and performs keyword matching without sending data to the cloud.
    *   **Best for**: Privacy-conscious users and offline environments.

### 📊 Strict Rubric Scoring
The app evaluates speeches based on a structured 100-point rubric:
*   **Content (40pts)**: Checks for salutations, required keywords (Name, Age, Hobbies, etc.), and logical flow.
*   **Speech Rate (10pts)**: Measures Words Per Minute (WPM) against an ideal range (111-140 WPM).
*   **Grammar (20pts)**: Analyzes grammatical errors and vocabulary diversity (Type-Token Ratio).
*   **Clarity (15pts)**: Detects and penalizes excessive filler words (um, uh, like).
*   **Engagement (15pts)**: Analyzes sentiment positivity to gauge speaker enthusiasm.

### 🎨 Interactive Dashboard
*   **Spider Chart**: Visualizes performance across all 5 categories.
*   **Comparison Charts**: Benchmarks user scores against "Ideal" scores.
*   **Transcript Analysis**: Highlights keywords in **Green** and filler words in **Red**.

## 🛠️ Tech Stack

*   **Frontend**: [Streamlit](https://streamlit.io/)
*   **Audio Processing**: [OpenAI Whisper](https://github.com/openai/whisper), FFmpeg
*   **NLP & ML**:
    *   `sentence-transformers` (Semantic Similarity)
    *   `vaderSentiment` (Sentiment Analysis)
    *   `language-tool-python` (Grammar Checking)
*   **LLM Integration**: Google Generative AI SDK (`google-generativeai`)
*   **Visualization**: Plotly

## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/coldboxer007/Communicationcoach.git
    cd Communicationcoach
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: You also need `ffmpeg` installed on your system for audio processing.*

3.  **Run the app**:
    ```bash
    streamlit run app.py
    ```

## 📂 Project Structure

```
├── app.py                 # Main Streamlit application entry point
├── engines/
│   ├── cloud_engine.py    # Logic for Google Gemini integration
│   └── local_engine.py    # Logic for local ML processing (Whisper, VADER, etc.)
├── utils/
│   ├── rubric.py          # Definitions of scoring rules and constants
│   └── visuals.py         # Helper functions for Plotly charts and HTML highlighting
├── requirements.txt       # Python dependencies
└── packages.txt           # System dependencies for deployment
```

## ☁️ Deployment

This app is ready for **Streamlit Community Cloud**.
1.  Push your code to GitHub.
2.  Connect your repo on [share.streamlit.io](https://share.streamlit.io/).
3.  The `packages.txt` file ensures FFmpeg and Java are installed automatically.

---
*Built for the Advanced Agentic Coding Case Study.*
