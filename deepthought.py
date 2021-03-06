import random
import tweepy

from auth import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)

# Create tweepy API

def create_api():

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)


# Get LAST_N_TWEETS from timeline so that quotes aren't posted more than once in succession

def get_timeline_history(client, LAST_N_TWEETS):

    tweets = client.user_timeline(id = client.me().id, count = LAST_N_TWEETS, tweet_mode="extended")
    return [tweet.full_text for tweet in tweets]


# Read quotes in from a .txt file and prettyfy

def get_quotes(fname, parser):
    quotes = []
    
    with open(fname, 'r') as file:      
        quotes = [parser(line.rstrip()) for line in file]
            
    return quotes     


# Return a random quote to tweet from list of quotes

def get_random(quotes):
    
    random.shuffle(quotes)
    quote = quotes[random.randint(0, len(quotes) - 1)]
    return(quote)

  



