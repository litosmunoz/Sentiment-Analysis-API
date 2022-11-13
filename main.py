from tokenize import Name
from flask import Flask, request, jsonify
import random
import tools.sql_queries as esecuele
import json
import pandas as pd
from os import name
import markdown.extensions.fenced_code
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import statistics as st
from wordcloud import wordcloud
import spacy

app = Flask(__name__)

# GET: render markdown
@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template

# Get everything: SQL
@app.route("/all")
def all_tweets ():
    print("These are all the tweets from the database:")
    return jsonify(esecuele.get_everything())

# Get average likes and retweets
@app.route("/average")
def average():
    return jsonify(esecuele.get_average())

# Get summary stats (3 dictionaries):
## 1. Tweets per month
## 2. Likes per Month
## 3. Retweets per month
@app.route("/summary")
def summary_stats():
    tweets_per_month = esecuele.get_tweets_per_month()
    likes_per_month = esecuele.get_likes_per_month()
    retweets_per_month = esecuele.get_retweets_per_month()
    result = {
        "Tweets per month": tweets_per_month,
        "Likes per month": likes_per_month,
        "Retweets per month": retweets_per_month
    }
    return jsonify(result)    

# Get polarity score for one random tweet
@app.route("/sentiment/random")
def get_sentiment_one_random():
    df = esecuele.get_random_tweet()
    nltk.downloader.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()

    def sa(x):
        try:
            return sia.polarity_scores(x)
        except:
            return x

    df["polarity_score"] = df["Tweets"].apply(sa)

    return jsonify(df.to_dict(orient='records'))

# POST a new entry into the DB 
@app.route("/post", methods=['POST'])
def insert_row ():
    my_params = request.args
    print(my_params)
    day_ = my_params["day_"]
    month_ = my_params["month_"]
    year_= my_params["year_"]
    Tweets = my_params["Tweets"]
    Likes = my_params["Likes"]
    Retweets = my_params["Retweets"]
    
    esecuele.insert_one_row(day_, month_, year_, Tweets, Likes, Retweets)
    return f"Query succesfully inserted"

#this will check that the name is the main
if __name__ == '__main__': 
    app.run(port=9000, debug=True)