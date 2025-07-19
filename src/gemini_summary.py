import google.generativeai as genai
from google.generativeai import types # Import types for Tool and GoogleSearch
from dotenv import load_dotenv
import os
load_dotenv()
# Configure the Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def summarize_with_gemini(prompttext):
    """Calls the Gemini API to get a high-quality summary."""
    if not GOOGLE_API_KEY:
        return "ERROR: GOOGLE_API_KEY not found. Please check your .env file."
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompttext) 
        return response.text.strip()
    except Exception as e:
        print(f"   - ❌ Gemini API Error: {e}")
        return "Could not generate summary due to an API error."

if __name__=="__main__":
    x= summarize_with_gemini("get me latest news")
    print(x)