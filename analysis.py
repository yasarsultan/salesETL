from nltk.sentiment import SentimentIntensityAnalyzer

def sentiment_scoring(text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(str(text))
    return scores['neg'], scores['neu'], scores['pos'], scores['compound']