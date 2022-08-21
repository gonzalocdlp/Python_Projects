import os
import openai
import authapi
openai.organization = "org-SnuqljBeSr8VdBfdkdiUOGb8"
openai.api_key = authapi.apikey
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
blob=TextBlob(text)
sentiment=blob.sentiment.polarity
completion = openai.Completion.create(engine="ada", prompt="write about a dragon")
print(completion)