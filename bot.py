import tweepy

apiKey = "kqiTGL4vhvk2t0lH46OdOlXRp"
apiSecretKey = "enyyDKXNPt3nwwyEEPirq94lGpDSkENdRtmLJiCdHKjF2YHNY5"

apiAccessToken = "1343749282499854338-egzvNHmwrm9i0Y3o73z3L3usvIq7Kb"
apiSecretAccessToken = "ffJon9xD1C8tKaJfhYozdSRfyqVg1X8X8tp6lF9MPWz3b"

# twtAcc @OffTheSenzu
myAccId = "3408914651"
# other twt accs
accIDs = ["2347264625", "3161785697", "2880135280", "1140429843689070592", "831740071627874304"]


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        tweet = self.reversify(status.text)
        b = True

        if status.user.screen_name in tweet:
            b = False

        if b:
            print(status.user.screen_name + " tweeted: " + status.text)
            print("bot replied with: " + tweet)
            api.update_status(status=('@' + status.user.screen_name + " " + tweet), in_reply_to_status_id=status.id)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

    @staticmethod
    def reversify(inp):
        return inp[::-1]


auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
auth.set_access_token(apiAccessToken, apiSecretAccessToken)
api = tweepy.API(auth, wait_on_rate_limit=True)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(follow=accIDs)
