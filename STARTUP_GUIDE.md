# Communication Coach - Startup Guide

Welcome to the **Communication Coach** application! This guide will help you set up, run, and troubleshoot the app.

## 📋 Prerequisites

- **Python 3.8+** installed on your system.
- **Git** installed.
- **Google Gemini API Key** (for Cloud Mode). [Get one here](https://aistudio.google.com/app/apikey).
- *(Optional)* **Java** (required for Grammar Checking in Local Mode).

## 🚀 Quick Start

### 1. Clone/Open the Repository
Ensure you are in the project directory:
```bash
cd /path/to/project
```

### 2. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Launch the Streamlit dashboard:
```bash
streamlit run app.py
```
The app should open automatically in your browser at `http://localhost:8501`.

## ⚙️ Configuration

### Dual-Engine Modes
The app has two modes selectable in the sidebar:

1.  **Gemini AI (Cloud)**
    -   **Requires**: API Key.
    -   **Pros**: High accuracy, detailed semantic feedback, checks flow and logic.
    -   **Cons**: Requires internet, data sent to cloud.

2.  **Local ML (Offline)**
    -   **Requires**: No internet (after initial model download).
    -   **Pros**: Private, free.
    -   **Cons**: Heavier on system resources.
    -   **Note**: On the first run, it will download models (~1GB) for Whisper and Sentence Transformers.

## 🛠️ Troubleshooting

### Common Issues

**1. "Segmentation Fault" or App Crash**
-   **Cause**: Conflict with `sentence-transformers` or `tokenizers` on some Mac systems.
-   **Fix**: The app automatically falls back to **String Matching** if the ML model fails. You don't need to do anything, but keyword matching will be less "smart" (exact matches only).

**2. "Java missing" / Grammar Check Skipped**
-   **Cause**: `language-tool-python` needs Java to run the local server.
-   **Fix**: Install Java (e.g., `brew install java` on Mac) or rely on the Cloud Engine for grammar checks.

**3. Audio Upload Error**
-   **Cause**: File format not supported.
-   **Fix**: Ensure you upload standard `.mp3` or `.wav` files.

## 📞 Support
If you encounter persistent issues, check the terminal output for error logs.
