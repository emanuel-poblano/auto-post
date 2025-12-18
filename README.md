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
