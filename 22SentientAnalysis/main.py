import os
import openai
openai.organization = "org-SnuqljBeSr8VdBfdkdiUOGb8"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
from newspaper import Article
from textblob import TextBlob
from requests import request, Request
url='https://www.reddit.com/r/webdev/comments/2e0r3y/why_do_we_hate_godaddy/'
article=Article(url)
article.download()
article.parse()
article.nlp()
text=article.summary
print(text)
blob=TextBlob(text)
sentiment=blob.sentiment.polarity
print (sentiment)
