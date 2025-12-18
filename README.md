# Auto Social Media Poster

A Python-based automation tool to **schedule and post content on Twitter/X**.  
This project demonstrates **API integration, OAuth authentication, scheduling, and automation**, making it a strong portfolio project for Python developers and automation enthusiasts.

---

## 🔹 Features

- Post text tweets automatically using **Twitter/X API**  
- OAuth 1.0a user authentication for secure posting  
- Schedule posts at specific times using Python's `schedule` module  
- Load multiple posts from a `.txt` file and rotate them randomly  
- Logging of successful and failed posts  
- Easily extendable to other platforms (Instagram, LinkedIn, etc.)  

---

## 🔹 Tech Stack

- Python 3.x  
- [requests](https://pypi.org/project/requests/)  
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  
- [schedule](https://pypi.org/project/schedule/)  

---

## 🔹 Project Structure

```bash
auto-post/
├── main.py              # Main script to post tweets
├── scheduler.py         # Optional script for scheduled posting
├── config.py            # Loads API keys from .env
├── poster/
│   ├── __init__.py
│   └── twitter.py       # Handles posting to Twitter/X
├── content/
│   ├── posts.txt        # Sample post content
│   └── images/          # Optional for future media posts
├── logs/
│   └── post.log         # Log file for tracking posts
├── .env                 # Environment variables (API keys)
└── requirements.txt     # Python dependencies
```

--

## 🔹 Setup & Installation

- Clone repository 

```bash
git clone https://github.com/yourusername/auto-post.git
cd auto-post
```
- Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Create .env with your social media credentials: 

```bash
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_SECRET=your_access_secret
```

- Add content to ```content/posts.txt``` (one post per line)

## 🔹 Usage

- Post a single tweet

```bash
python main.py
```

- Schedule posts
- Edit ```scheduler.py```

```bash
import schedule
import time
from poster.twitter import post_to_twitter

def job():
    post_to_twitter("Scheduled tweet from Python bot 🤖")

schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

- Run:

```bash
python scheduler.py
```

## 🔹 Logging

- Successful and failed posts are recorded in ```logs/post.log```
- Use logging to track errors, retries, or API issues

## 🔹 Future Improvements

- Add AI-generated captions using OpenAI API
- Extend to Instagram, LinkedIn, or TikTok
- Add media upload support (images/videos)
- Build a dashboard for scheduling and analytics

## 🔹 License

MIT License © Emanuel Poblano