import tweepy
import upsidedown
import json

# INPUT INFORMATION IN 'config.json' IN ORDER TO HAVE THE BOT PROPERLY WORKING

# loading config file
with open("config.json", "r") as f:
    config = json.load(f)

# twitter auth stuff
apiKey = config["apiKey"]
apiSecretKey = config["apiSecretKey"]
apiAccessToken = config["apiAccessToken"]
apiSecretAccessToken = config["apiSecretAccessToken"]

# accounts to follow (refer to config comments)
accIDs = config["accIDs"]


# Tweepy stuff
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        tweet = "@" + status.user.screen_name + " " + self.reversify(status.text)
        b = True

        if api.auth.get_username() in tweet:
            b = False

        if b:
            print(status.user.screen_name + " tweeted: " + status.text)
            print("bot replied with: " + tweet)
            api.update_status(status=tweet, in_reply_to_status_id=status.id)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

    @staticmethod
    def reversify(inp):
        return upsidedown.transform(inp)


# main
if not (apiKey == "key1" or
        apiSecretKey == "key2" or
        apiAccessToken == "token1" or
        apiSecretAccessToken == "token2"):

    auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
    auth.set_access_token(apiAccessToken, apiSecretAccessToken)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(follow=accIDs)

else:
    print("Invalid config file")
