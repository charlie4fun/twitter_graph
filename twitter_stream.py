import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = "i2MOcYvFUBYyV2VLstIxQWFox"
consumer_secret = "3snc68OiPRMACizWvkz7O8GHoHZGqrTnsC8WPC8QLvRtA0OIfS"
access_token= "748433808584695808-4dwGAIBSd6MNRKqseVx6YU5L6Zz7Zty"
access_secret = "9EKE0xI9uustkbxlQV14tZe2J7V1zf7TvZ3QXqPlL1B2J"

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)

api = tweepy.API(auth)

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['kereta', 'mobil', 'gerbong', 'gerobak', 'oto', 'wagon', 'pedati'])