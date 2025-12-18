# main.py
import random
from poster.twitter import post_to_twitter


with open("content/posts.txt") as f:
    posts = f.readlines()

post_to_twitter(random.choice(posts).strip())

print("Tweet posted successfully.")
