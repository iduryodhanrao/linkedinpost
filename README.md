# 🚀 linkedinpost

## 📝 Overview

This project automates the process of generating LinkedIn posts from the latest technology news. It fetches news articles, scrapes their content, summarizes them using Google's Gemini LLM, filters for technology relevance, and publishes the best summary to LinkedIn.

## ✨ Features

- 📰 Fetches news links using [`rapidapi_news.get_news`](src/rapidapi_news.py)
- 🕸️ Scrapes article content via [`webscrap.scrape`](src/webscrap.py)
- 🤖 Summarizes articles using Gemini LLM ([`gemini_summary.summarize_with_gemini`](src/gemini_summary.py))
- 🧠 Filters for technology, innovation, AI, and ML relevance
- 🔗 Publishes selected summary to LinkedIn via [`linkedpublish.py`](src/linkedpublish.py)

## ⚡ Usage

1. 🛡️ Set up your `.env` file with required API keys (Google Gemini, RapidAPI, LinkedIn).
2. 📦 Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. ▶️ Run the main script:
   ```
   python src/app.py
   ```

## 📂 Files

- [`src/app.py`](src/app.py): Main workflow for news fetching, summarization, filtering, and publishing.
- [`src/rapidapi_news.py`](src/rapidapi_news.py): News API integration.
- [`src/webscrap.py`](src/webscrap.py): Web scraping utilities.
- [`src/gemini_summary.py`](src/gemini_summary.py): Gemini LLM summarization.
- [`src/linkedpublish.py`](src/linkedpublish.py): LinkedIn publishing logic.

## 📋 Requirements

See [`requirements.txt`](requirements.txt) for