
from fastapi import FastAPI
from fetch_twitter import fetch_tweets
from fetch_news import fetch_news
from analyze_ai import analyze_text

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to NotFakeNews API"}

@app.get("/search")
def search(q: str):
    tweets = fetch_tweets(q)
    news = fetch_news(q)
    analyzed_tweets = [analyze_text(tweet) for tweet in tweets]
    analyzed_news = [analyze_text(article) for article in news]
    return {"tweets": analyzed_tweets, "news": analyzed_news}
### Backend Code for NotFakeNews (FastAPI)

#### 📌 Overview
This is the backend for the NotFakeNews project. It fetches trending news and tweets, analyzes political bias, 
and provides counterarguments using AI.

---

## 📂 Project Structure:
```
backend/
│── main.py       # Main API logic (FastAPI server)
│── fetch_twitter.py  # Twitter data fetcher (API & scraping)
│── fetch_news.py  # NewsAPI integration
│── analyze_ai.py  # AI processing (bias detection & summaries)
│── database.py    # Database storage (PostgreSQL)
│── requirements.txt  # Python dependencies
│── .env.example      # Example environment variables
│── models/         # Database models (if needed)
│── routers/        # API route handlers (if needed)
```

---

## 📜 `main.py` (FastAPI Server)
```python
from fastapi import FastAPI
from fetch_twitter import fetch_tweets
from fetch_news import fetch_news
from analyze_ai import analyze_text

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to NotFakeNews API"}

@app.get("/search")
def search(q: str):
    tweets = fetch_tweets(q)
    news = fetch_news(q)
    analyzed_tweets = [analyze_text(tweet) for tweet in tweets]
    analyzed_news = [analyze_text(article) for article in news]
    return {"tweets": analyzed_tweets, "news": analyzed_news}
```

---

## 📜 `fetch_twitter.py` (Twitter API Scraper)
```python
import requests
import os

def fetch_tweets(query):
    API_KEY = os.getenv("TWITTER_API_KEY")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=10"
    response = requests.get(url, headers=headers)
    return response.json().get("data", [])
```

---

## 📜 `fetch_news.py` (NewsAPI Fetcher)
```python
import requests
import os

def fetch_news(query):
    API_KEY = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"
    response = requests.get(url)
    return response.json().get("articles", [])
```

---

## 📜 `analyze_ai.py` (AI Bias Analysis & Counterarguments)
```python
import openai
import os

def analyze_text(text):
    API_KEY = os.getenv("OPENAI_API_KEY")
    openai.api_key = API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Analyze the political bias of the following text and generate a 
counterargument."},
            {"role": "user", "content": text}
        ]
    )
    return response["choices"][0]["message"]["content"]
```

---

## 📜 `.env.example` (Example API Keys Setup)
```
TWITTER_API_KEY=your_twitter_api_key
NEWS_API_KEY=your_news_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

## **🚀 Setup Instructions**

### 1️⃣ Install Dependencies
```bash
cd backend
python3 -m pip install -r requirements.txt --user
```

### 2️⃣ Create Your `.env` File
```bash
cd backend
nano .env
```
**Paste this inside and replace with actual API keys:**
```
TWITTER_API_KEY=your_twitter_api_key
NEWS_API_KEY=your_news_api_key
OPENAI_API_KEY=your_openai_api_key
```
**Save and exit (`CTRL + X`, `Y`, `Enter`).**

### 3️⃣ Run the Backend
```bash
uvicorn main:app --reload
```
✅ **API should now be running at `http://127.0.0.1:8000`**

---

## **🔥 Next Steps**
✅ **Test the API using `/search?q=your_topic`**
✅ **Ensure AI bias detection and counterarguments work**
✅ **Deploy to a test server after local testing**

🚀 **Once you've updated this on GitHub, let me know!** 🔥
≈
