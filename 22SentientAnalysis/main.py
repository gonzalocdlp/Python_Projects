import os
import openai
import authapi
from flask import Flask, render_template, requests, flash
app= Flask(__name__)
@app.route("/business")
def index():
    return render_template(index.html)
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
business="photography business in florida"
keywords="Miami, portrait shoots, wedding shoots."
completion = openai.Completion.create(engine="text-curie-001", prompt=f"write a long description with a call to action about a {business} . Write it using the keywords {keywords} the name of the business is Miami Profile and it's owned by Gonzalo Casas", max_tokens=20)
print(completion['choices'][0]['text'])

