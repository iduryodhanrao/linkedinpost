import requests
import json
import os
from dotenv import load_dotenv 
from getAIMLnews import summarize_with_gemini

# --- Configuration ---
# OPENID/OAUTH 2.0 BEARER TOKEN HERE
load_dotenv()
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
LINKEDIN_AUTHOR_URN = os.getenv("LINKEDIN_AUTHOR")

# THE TEXT YOU WANT TO POST
#POST_TEXT = """🚀✨🤖 Just catching up on the latest AI breakthroughs, and Anthropic's new **Claude 3.5 Sonnet** is truly impressive! This model sets new benchmarks for speed, cost-efficiency, and multimodal understanding, especially for complex coding and analysis tasks. It feels like a significant leap forward in making advanced AI more accessible and practical for everyday applications.
#AI #MachineLearning #ClaudeAI #TechNews
#**Reference:** [https://www.anthropic.com/news/claude-3-5-sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)
#"""

# --- LinkedIn API Endpoints ---
USER_INFO_URL = "https://api.linkedin.com/v2/userinfo"
UGC_POSTS_URL = "https://api.linkedin.com/v2/ugcPosts"

# --- Step 1: Get your Person URN ---
def get_person_urn(token):
    """
    Fetches the user's unique person URN required for posting.
    This uses the OpenID Connect userinfo endpoint.
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(USER_INFO_URL, headers=headers)
    
    if response.status_code == 200:
        user_info = response.json()
        person_urn = user_info.get("sub") # 'sub' claim contains the URN
        print(f"✅ Successfully fetched Person URN: {person_urn}")
        return person_urn
    else:
        print(f"❌ Error fetching user info: {response.status_code}")
        print(f"   Response: {response.text}")
        return None

# --- Step 2: Create the LinkedIn Post ---
def create_text_post(token, person_urn, text):
    """
    Creates a simple text post on LinkedIn using the UGC (User-Generated Content) API.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0" # Required by LinkedIn API
    }
    
    post_data = {
        "author": "urn:li:person:"+person_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            # You can change visibility to "CONNECTIONS"
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    response = requests.post(UGC_POSTS_URL, headers=headers, data=json.dumps(post_data))
    
    if response.status_code == 201: # 201 Created indicates success
        print("🎉 Post was successfully created on LinkedIn!")
        post_id = response.json().get('id')
        print(f"   Post ID: {post_id}")
    else:
        print(f"❌ Failed to create post: {response.status_code}")
        print(f"   Response: {response.text}")


# --- Main Execution ---
if __name__ == "__main__":
    if LINKEDIN_ACCESS_TOKEN == "YOUR_ACCESS_TOKEN":
        print("🛑 Please update the ACCESS_TOKEN variable in the script.")
    else:
        # Get the person URN first
        author_urn = get_person_urn(LINKEDIN_ACCESS_TOKEN)
        print(author_urn)
        
        # If we got the URN, proceed to create the post
        if author_urn:
            prompt=f"get one latest AI-ML top or breaking news from this week and Summarize it"
            guardrails = f" for a personalized linked-in post in 2-3 concise sentences with the icons in the post and the reference link at bottom.Do not include any introductory phrases or headers like 'Here's a summary..."
            prompttext = prompt + guardrails
            POST_TEXT= summarize_with_gemini(prompttext)
            print(POST_TEXT)
            create_text_post(LINKEDIN_ACCESS_TOKEN, author_urn, POST_TEXT)
        