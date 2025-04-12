import streamlit as st
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import warnings

# Ignore all warnings
warnings.filterwarnings('ignore')

def get_video_info(youtube_url):
    try:
        ydl_opts = {'quiet': True, 'skip_download': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=False)
            return {
                'title': info_dict.get('title', 'No Title'),
                'description': info_dict.get('description', 'No Description'),
                'id': info_dict.get('id', None)
            }
    except Exception as e:
        st.error(f"Error getting video info: {e}")
        return None

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([entry['text'] for entry in transcript_list])
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None

def generate_summary(transcript, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash-lite')
    
    prompt = f"""Please provide a comprehensive summary of the following video transcript:
    
    {transcript}
    
    Summary should include main points, key arguments, and important details. Keep it structured and concise."""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating summary: {e}")
        return None

# Streamlit UI
st.title("🎥 YouTube Video Summarizer")
st.markdown("### Powered by Google Gemini")

with st.sidebar:
    st.header("Configuration")
    GOOGLE_API_KEY = st.text_input('Enter Gemini API Key:', type='password')
    st.markdown("[Get Gemini API Key](https://aistudio.google.com/app/apikey)")

youtube_url = st.text_input('Enter YouTube Video URL:', '', help="Paste any YouTube video URL here")

if st.button('Generate Summary'):
    if not GOOGLE_API_KEY:
        st.warning('🔑 Please enter your Gemini API key!')
        st.stop()
    
    if not youtube_url.startswith('https://'):
        st.warning('⚠️ Please enter a valid YouTube URL')
        st.stop()
    
    with st.spinner('📡 Fetching video information...'):
        video_info = get_video_info(youtube_url)
        if not video_info or not video_info['id']:
            st.error('❌ Failed to retrieve video information')
            st.stop()
        
        st.subheader(video_info['title'])
        st.caption("Video ID: " + video_info['id'])
    
    with st.spinner('📝 Extracting transcript...'):
        transcript = get_transcript(video_info['id'])
        if not transcript:
            st.error('❌ No transcript available for this video')
            st.stop()
    
    with st.spinner('🧠 Generating summary with Gemini...'):
        summary = generate_summary(transcript, GOOGLE_API_KEY)
        if not summary:
            st.stop()
        
        st.subheader("📄 Video Summary")
        st.markdown(summary)
        
        with st.expander("View Transcript"):
            st.write(transcript)
        
        with st.expander("View Video Details"):
            st.write(f"**Title:** {video_info['title']}")
            st.write(f"**Description:** {video_info['description']}")