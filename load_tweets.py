import json
import pandas

tweets_data = []
tweets_file = open('twitter_data.txt')
for line in tweets_file:
    try:
        tweet_data = json.loads(line)
        tweets_data.append(tweet_data)
    except json.decoder.JSONDecodeError:
        continue

tweets = pandas.DataFrame()
tweets['friends'] = [tweet['user']['friends'] for tweet in tweets_data]
tweets['friends'].max()
