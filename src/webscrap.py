import requests
from bs4 import BeautifulSoup

def scrape(url: str) -> str:
    """
    Scrapes the content of a given URL and summarizes it using Gemini-Flash.
    Returns:
        str: A summary of the website content, or an error message.
    """
    try:
        # Step 1: Fetch the content of the URL
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

        # Step 2: Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract readable text. You might need to refine this based on the website structure.
        # This example tries to get text from common content tags.
        text_content_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'li', 'span'])
        article_text = ' '.join([element.get_text(separator=' ', strip=True) for element in text_content_elements])

        # Basic clean-up: remove excessive whitespace
        article_text = ' '.join(article_text.split())

        if not article_text:
            return "Could not extract significant text content from the URL."

        return article_text

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    #url_to_scrape = input("Enter the URL to summarize: ")
    summary = scrape("https://apnews.com/article/russia-internet-cellphone-disruptions-ukraine-war-9644b7147d661a8e0809465afffb452f")
    print("\n--- Summary ---")
    print(summary)
