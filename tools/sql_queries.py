from config.sql_connection import engine
import pandas as pd
import random

## GET
def get_everything ():
    query = f"""SELECT * FROM elon_tweets;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_average ():
    query = f"""SELECT AVG(Likes), AVG(Retweets) 
    FROM elon_tweets;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def insert_one_row (day, month, year, Cleaned_Tweets, Retweets, Likes):
    query = f"""INSERT INTO elon_tweets
     (day, month, year, Cleaned_Tweets, Retweets, Likes) 
        VALUES ('{day}''{month}''{year}', '{Cleaned_Tweets}', '{Retweets}', '{Likes}');
    """
    engine.execute(query)
    return f"Correctly introduced!"
