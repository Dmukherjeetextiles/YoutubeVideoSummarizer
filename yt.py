import yt_dlp
import google.generativeai as genai
from IPython.display import Markdown
import streamlit as st
import pandas as pd




def get_youtube_video_summary(youtube_url):
    try:
        # Create a YouTube object using yt_dlp
        ydl = yt_dlp.YoutubeDL()
        info_dict = ydl.extract_info(youtube_url, download=False)

        # Extract relevant information
        video_title = info_dict.get('title', 'No Title')
        video_description = info_dict.get('description', 'No Description')

        # Print or return the summary
        video_summary = f'''Title: {video_title}\n
                            Description: {video_description}'''
        return video_summary
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
st.title("Youtube Video Summarizer")
st.header("A Gemini Application by Debrup Mukherjee")
GOOGLE_API_KEY = st.text_input('GEMINI Secret Key Here', '')
# Configure the client library by providing your API key.
genai.configure(api_key=GOOGLE_API_KEY)
# Set up the model
generation_config = {
  "temperature": 0.8,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
youtube_url = st.text_input('Youtube URL Here', '')
video_summary = get_youtube_video_summary(youtube_url)
if st.button('Run'):
    user_input = f'summarize the video script {video_summary}.' #@param {isTemplate: true}
    # Call the model and print the response.
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
    chat = model.start_chat(history=[])
    # Send the input file and the prompt to the model
    response = chat.send_message(user_input)
    # Save the response in a variable
    result_parts = response.parts 

    # Extract the text content from the result_parts
    result = " ".join(part.text.strip() for part in result_parts)

    if video_summary:
        st.write('Summary: \n', result)
        st.write('\n', video_summary)
    else:
        st.write("Failed to retrieve video summary.")
