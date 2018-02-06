import tweepy
from PIL import Image
from PIL import ImageFile

from secrets import consumer_key, consumer_secret, access_token, access_secret

ImageFile.LOAD_TRUNCATED_IMAGES = True

# create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


class BotStreamer(tweepy.StreamListener):
    """create a class inheriting from the tweepy StreamListener."""

    # Called when a new status arrives which is passed down from the on_data method of
    # StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id

        if 'media' in status.entities:
            for image in status.entities['media']:
                tweet_image(image['media_url'], username, status_id)


myStreamListener = BotStreamer()

# Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['#image'])


# # construct the API instance
# api = tweepy.API(auth)
#
# # public_tweets = api.home_timeline()
# # for tweet in public_tweets:
# #     print(tweet.text)
# user = api.get_user('leighmichaelfor')
# for friend in user.friends():
#     print(friend.screen_name)
