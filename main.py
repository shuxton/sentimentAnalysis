import string
from collections import Counter
import matplotlib.pyplot as plt
import GetOldTweets3 as got
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('karnataka exam')\
        .setSince("2020-05-30")\
        .setUntil("2021-05-30")\
        .setMaxTweets(1000)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets


text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length):
    text = text_tweets[i][0]+" "+text


#text = open('read.txt', encoding="utf-8").read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
tokenized_words = word_tokenize(cleaned_text, "english")


final_words = []
for word in tokenized_words:
    if word not in stopwords.words("english"):
        final_words.append(word)


emotion_list = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(
            ",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)


w = Counter(emotion_list)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)


sentiment_analyse(cleaned_text)


fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
