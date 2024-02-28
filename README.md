# YoutubeVideoSummarizer
This is a simple Youtube URL to video summarizer that use Gemini for the summarization. Use your own API Key which you can find at https://aistudio.google.com/app/apikey

This Python script utilizes the yt_dlp library to extract information from a YouTube video and a Gemini AI model to generate a summary of the video script. The script is integrated into a Streamlit web application for easy user interaction.

# Prerequisites
Ensure you have the necessary Python libraries installed. You can install them using:

'''
pip install yt-dlp google.generativeai IPython streamlit pandas

pip install -r requirements.txt
'''
# Usage
Run the Streamlit app using the following command in your terminal:

'''
streamlit run yt.py
'''
* Input your GEMINI Secret Key in the provided text box.
* Enter the YouTube URL of the video you want to summarize.
* Click the "Run" button to initiate the summarization process.

# Code Overview
The get_youtube_video_summary function extracts the title and description of a YouTube video.
The Streamlit UI allows the user to input the GEMINI Secret Key and the YouTube URL.
The Gemini AI model is configured, and safety settings are defined.
The user's input is processed, and the Gemini AI model generates a summary.
The result is displayed on the Streamlit app.

# Dependencies
* yt_dlp for YouTube data extraction.
* google.generativeai for the Gemini AI model.
* streamlit for creating the web application.
* pandas for data manipulation.
# Disclaimer
Ensure compliance with the terms of service of YouTube and Gemini AI when using this tool.
# Note
This tool is designed for internal use within your company.
Feel free to customize and enhance the code according to your specific requirements.
