### NotFakeNews Project - Twitter & News Bias Analyzer

#### 📌 Overview
This project fetches trending news and tweets, analyzes political bias, and provides counterarguments using AI.

---

## 🛠️ Tech Stack:
- **Backend:** FastAPI (Python)
- **Frontend:** React (Veltrix UI)
- **AI Processing:** OpenAI GPT-4o
- **Database:** PostgreSQL (for caching results)

---

## 📂 Project Structure:
```
notfakenews/
│── backend/          # FastAPI backend
│   ├── main.py       # Main API logic
│   ├── fetch_twitter.py  # Twitter data fetcher (API & scraping)
│   ├── fetch_news.py  # NewsAPI integration
│   ├── analyze_ai.py  # AI processing (bias detection & summaries)
│   ├── database.py    # Database storage (PostgreSQL)
│── frontend/         # React (Veltrix UI)
│   ├── src/
│   │   ├── App.js    # Main frontend logic
│   │   ├── components/
│   ├── public/
│── scripts/          # Automation scripts
│   ├── git-auto-push.sh  # Auto GitHub push script
│── .env.example      # Example environment variables
│── README.md         # Project documentation
```

---

## 🚀 Setup Instructions

### 1️⃣ Install Dependencies
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd ../frontend
npm install
```

### 2️⃣ Set Up API Keys
Create a `.env` file inside `backend/` with:
```
TWITTER_API_KEY=your_twitter_api_key
NEWS_API_KEY=your_news_api_key
OPENAI_API_KEY=your_openai_api_key
```

### 3️⃣ Run the Project
```bash
# Start Backend (FastAPI)
cd backend
uvicorn main:app --reload

# Start Frontend (React)
cd ../frontend
npm start
```

---

## 🧪 Testing the MVP
Once everything is running:
- Open `http://localhost:3000/` to access the UI.
- Use the search bar to fetch **Twitter & news articles**.
- View **AI-generated bias detection & counterarguments**.

---

## 🔥 Next Steps
✅ **Deploy to a test server (Vercel/Render)**
✅ **Optimize AI speed (reduce API costs)**
✅ **Improve UI (real-time updates)**
✅ **Scale up Twitter data fetching (if upgrading API)**

🚀 **Let me know once you've uploaded this to GitHub!** 🔥

# NotFakeNews
