"""

This is a Twitter bot. It can tweet, favorite, follow, read trending,
and update profile details. The code is run in console. Python is
run within console. Delete all non-functional code before running.

Requirements are to have a Twitter developer account. They're easy to get.
Tutorial used: https://realpython.com/twitter-bot-python-tweepy/

Last Updated 14 Jun 2019

"""

## Set-up

cd A:\Users\gabee\python-virtual-environments # These should be changed to a local directory
py -m venv env

""" Not working. Supposed to activate virtual envr, but not important right now. Seems to run sometimes??
If virtual env is running, have to run pip installs for virtualenv, tweepy and time
.\env\Scripts\activate
"""

pip install tweepy
pip install virtualenv

py
import tweepy
import virtualenv
import time


## Creating variables for authenticators
# Use own auth keys if not running G&C's bot
auth = tweepy.OAuthHandler("8d4if6rL9Pd7vTHQVA5cfUznw",
    "ItAW8M7JYVbQre5xR5mnusT4neU9zyGVgZ8gyGS6iRAdTg9oJA")
auth.set_access_token("1139324033135235073-WEjfJxT267HJFAzFg7u7OUFbuWc2yG",
    "3JCfbVs6uFmUdwmXdwCsR1cOMTA51Q9IzkCdSBnw8xOGo")

api = tweepy.API(auth)

## Tests connection to twitter api
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

## Unnecessary Test Tweet
api.update_status("Watch out world, @MjGanaden is doing big things!! #GodIsGood #FirstFollowerLuv")


## Prints author and text of the last tweets in your home timeline:

timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

## Searches users using a filter criteria, fetches username, user description, user location, and 20 most recent twitter followers
user = api.get_user("bootybootyusa")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)

## Follows username
api.create_friendship("@bootybootyusa") # Replace "realpython" with twitter handle

## Use while loop with time.sleep to
while True:
    time.sleep(10) # Argument is in seconds. 60 = 1 min, 3600 = 1 hr, 86400 = 1 day

## Reads current trends with geographical location Argument
trends_result = api.trends_place(1) # 1 is world
for trend in trends_result[0]["trends"]:
    print(trend["name"])
