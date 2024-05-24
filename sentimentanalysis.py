import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Test the code on a sample text
text = input("Input a text (string) from user for sentiment analysis : ")
score = sia.polarity_scores(text)

# Print the sentiment score
print("Polarity Scores are: \n")
print(score)