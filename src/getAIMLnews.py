import google.generativeai as genai
from google.generativeai import types # Import types for Tool and GoogleSearch
from dotenv import load_dotenv
import os
import datetime
import requests

# --- Configuration & Setup ---
load_dotenv()
# Configure the Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def check_link_validity(url):
    """
    Checks if a given URL returns a 200 OK status.
    """
    try:
        # Using a HEAD request is efficient as it only fetches headers
        response = requests.head(url, timeout=5)
        # Check for 2xx status codes (200 OK, 201 Created, etc.)
        return 200 <= response.status_code < 300
    except requests.exceptions.RequestException as e:
        # print(f"Error checking link {url}: {e}") # For debugging invalid links
        return False
    
# --- New Function: Summarize with Gemini API ---
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

if __name__ == "__main__":
    # Get today's date in a friendly format for the prompt
    today_date = datetime.date.today().strftime("%B %d, %Y")
    this_month = datetime.date.today().strftime("%B, %Y")
    today = datetime.date.today()
    one_week_ago = (today - datetime.timedelta(days=7)).strftime("%B %d, %Y")
    today_str = today.strftime("%B %d, %Y")
    print(this_month)

    prompt=f"get 1 top AI/ML news and Summarize it for the technical content only. Do not add any words related to timeline"
    guardrails = f" for a personalized linked-in post in 2-3 concise sentences with the icons in the post and the reference link at bottom. Do not include any introductory phrases or headers or words like 'Here's a summary...' focus on the news that is genuine, true and has a valid link"
    prompttext = prompt + guardrails
    print(prompttext)
    t= summarize_with_gemini(prompttext)
    print(t)
