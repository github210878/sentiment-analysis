from textblob import TextBlob

# Function to analyze sentiment and return a label
def get_sentiment(text):
    # Create a TextBlob object
    analysis = TextBlob(text)

    # Check polarity to determine sentiment
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Input text from the user
text = input("Enter a text string: ")

# Get the sentiment label
sentiment = get_sentiment(text)

# Output the sentiment
print(f"The sentiment of the text is: {sentiment}")
 