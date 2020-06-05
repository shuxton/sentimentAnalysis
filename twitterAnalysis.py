import GetOldTweets3 as got


def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Karnataka exam')\
        .setSince("2019-08-01")\
        .setUntil("2021-05-30")\
        .setMaxTweets(10)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]
    print(text_tweets)


get_tweets()
