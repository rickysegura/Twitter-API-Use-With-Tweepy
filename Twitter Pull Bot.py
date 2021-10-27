# Twitter Follow Bot
# Developer: Ricky Segura
# GitHub @ rickysegura

# Imports
import tweepy

# Project Initialization
consumer_key = ""
consumer_secret = ""

key = ""
secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

# Create list of people I am following
FOLLOWERS = api.get_friends(screen_name="SpaceX")

# Search Function
def create_web():
  for x in range(3):
    print("Their Follower: [" + str(x) + "] " + FOLLOWERS[x].name)
    INCEPTION = api.get_followers(screen_name=FOLLOWERS[x].screen_name)
    for i in range(3):
      print("\tTheir Follower\'s follower: [" + str(i) + "] " + INCEPTION[i].name)

create_web()