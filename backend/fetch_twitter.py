import requests
import os

def fetch_tweets(query):
    API_KEY = os.getenv("TWITTER_API_KEY")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=10"
    response = requests.get(url, headers=headers)
    return response.json().get("data", [])

