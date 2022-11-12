from tokenize import Name
from flask import Flask, request, jsonify
import random
import tools.sql_queries as sql 
import json
import pandas as pd
from os import name
import markdown.extensions.fenced_code
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import statistics as st

app = Flask(__name__)

# GET: render markdown
@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template

# Get everything: SQL
@app.route("/all")
def all_reviews ():
    print("These are all the tweets from the database:")
    return jsonify(sql.get_everything())




if __name__ == '__main__': 
    app.run(port=9000, debug=True)