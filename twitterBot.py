## Creating variables for authenticators
""" Example
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
"""
auth = tweepy.OAuthHandler("8d4if6rL9Pd7vTHQVA5cfUznw", 
    "ItAW8M7JYVbQre5xR5mnusT4neU9zyGVgZ8gyGS6iRAdTg9oJA")
auth.set_access_token("1139324033135235073-WEjfJxT267HJFAzFg7u7OUFbuWc2yG", 
    "3JCfbVs6uFmUdwmXdwCsR1cOMTA51Q9IzkCdSBnw8xOGo")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

## Test Tweet
api.update_status("Test tweet from Tweepy Python")
api.update_status("#90sBabyFollowTrain 1⃣ Follow me✔ 2⃣ I follow u 3. get rich bitches!!")


### Methods for user timelines

## Prints author and text of the last tweets in your home timeline:

timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")



## Searches users using a filter criteria, fetches username, user description, user location, and 20 most recent twitter followers
    
