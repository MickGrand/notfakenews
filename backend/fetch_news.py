import requests
import os

def fetch_news(query):
    API_KEY = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"
    response = requests.get(url)
    return response.json().get("articles", [])

