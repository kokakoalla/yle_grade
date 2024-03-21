import requests # pip install requests
from bs4 import BeautifulSoup
from textblob import TextBlob

resource = requests.get("https://yle.fi/uutiset")
soup = BeautifulSoup(resource.content, "html.parser")

headlines = soup.find_all("h3")

news_data = []

for headline in headlines:
    news_text = headline.text
    print("News headline:", news_text)


    analysis = TextBlob(news_text)
    sentiment = analysis.sentiment.polarity


    if sentiment > 0:
        sentiment_label = "Positive"
    elif sentiment < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    news_data.append({"title": news_text, "grade": sentiment_label})

    print("Key:", sentiment_label)
    print('\n')

print("done")


