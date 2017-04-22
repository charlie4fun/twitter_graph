import tweepy

consumer_key = "i2MOcYvFUBYyV2VLstIxQWFox"
consumer_secret = "3snc68OiPRMACizWvkz7O8GHoHZGqrTnsC8WPC8QLvRtA0OIfS"

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)

api = tweepy.API(auth)

results = api.search(q="mobil", count=101)

print(len(results))