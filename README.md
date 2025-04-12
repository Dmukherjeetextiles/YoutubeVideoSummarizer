# 🎥 YouTube Video Summarizer with Gemini

A simple web application built with Streamlit that allows you to generate concise summaries of YouTube videos using Google's Gemini AI model.

[[Streamlit App](Screenshot youtube.png)](https://youtubevideosummarizergemini.streamlit.app/)

**Live demo:** [https://youtubevideosummarizergemini.streamlit.app/](https://youtubevideosummarizergemini.streamlit.app/)



## ✨ Features

*   **Fetch Video Details:** Retrieves video title and description using `yt-dlp`.
*   **Transcript Extraction:** Extracts the video's transcript using `youtube-transcript-api`.
*   **AI-Powered Summarization:** Uses the Google Gemini API (`gemini-2.0-flash-lite` model) to generate a comprehensive summary of the transcript.
*   **User-Friendly Interface:** Simple Streamlit interface for easy interaction.
*   **View Details:** Option to view the full transcript and original video description.
*   **API Key Input:** Securely input your Google Gemini API key via the sidebar.

## 🛠️ Technology Stack

*   **Language:** Python 3
*   **Web Framework:** Streamlit
*   **Video Info:** yt-dlp
*   **Transcript:** youtube-transcript-api
*   **AI Model:** Google Gemini API (via `google-generativeai`)

## ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Dmukherjeetextiles/YoutubeVideoSummarizer.git
    cd YoutubeVideoSummarizer
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv utube
    source venv/bin/activate  # On Windows use `utube\Scripts\python.exe`
    ```

3.  **Install dependencies:**
    pip install the following content:
    ```txt
    streamlit
    yt-dlp
    youtube-transcript-api
    google-generativeai
    ```
    Or install them from the requirements.txt:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Get a Google Gemini API Key:**
    *   You need an API key from Google AI Studio to use the summarization feature.
    *   Visit [Google AI Studio](https://aistudio.google.com/app/apikey) to create your key.

## ▶️ How to Run

1.  **Run the Streamlit application:**
    
    ```bash
    streamlit run yt.py
    ```

2.  **Use the App:**
    *   The application will open in your web browser.
    *   Enter your Google Gemini API Key in the sidebar input field.
    *   Paste the full URL of the YouTube video you want to summarize into the main input field.
    *   Click the "Generate Summary" button.
    *   Wait for the app to fetch the video info, extract the transcript, and generate the summary.
    *   The video title and summary will be displayed. You can expand sections to view the full transcript and video details.

## 📝 Configuration

*   **Google Gemini API Key:** This is required for the summarization functionality. The app prompts you to enter it in the sidebar. It is not stored persistently.


## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
