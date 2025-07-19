import requests
import json
import os
from dotenv import load_dotenv 

load_dotenv()
rapidapi_key = os.getenv("rapidapi_key")

url = "https://real-time-news-data.p.rapidapi.com/topic-news-by-section"

def get_news(topic="TECHNOLOGY",websitelimit=2):
    querystring = {"topic":topic,"section":"CAQiSkNCQVNNUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVENJT0NBUWFDZ29JTDIwdk1ETnliSFFxQ2hJSUwyMHZNRE55YkhRb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVENnQVABUAE","limit":websitelimit,"country":"US","lang":"en"}

    headers = {
        "x-rapidapi-key": rapidapi_key,
        "x-rapidapi-host": "real-time-news-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

if __name__ == "__main__":
    news_data = get_news("SCIENCE",1)
    # Print the news data
    for article in news_data["data"]:
        print(f"- Title: {article['title']}")
        print(f"  Link: {article['link']}")
        print("\n" + "-"*50 + "\n")