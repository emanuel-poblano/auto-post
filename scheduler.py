# scheduler.py
import schedule
import time
from poster.twitter import post_to_twitter

def job():
    post_to_twitter("Scheduled tweet from Python ⏰")

schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
