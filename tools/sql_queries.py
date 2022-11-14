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

def get_all_tweets():
    query = (f"""SELECT count(Tweets) as 'Total Tweets' FROM elon_tweets""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_tweets_per_month(): 
    query = (f"""SELECT month_, COUNT(Tweets) AS 'Tweets'
    FROM elon_tweets
    GROUP BY month_
    ORDER BY STR_TO_DATE(CONCAT(year_, month_, day_), '%%Y %%M %%d');""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_likes_per_month():
    query = (f"""SELECT month_, SUM(Likes) AS 'Likes'
    FROM elon_tweets
    GROUP BY month_
    ORDER BY STR_TO_DATE(CONCAT(year_, month_, day_), '%%Y %%M %%d');""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_retweets_per_month():
    query = (f"""SELECT month_, SUM(Retweets) AS 'Retweets'
    FROM elon_tweets
    GROUP BY month_
    ORDER BY STR_TO_DATE(CONCAT(year_, month_, day_), '%%Y %%M %%d');""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')
    
def get_random_tweet():
    query = (f"""SELECT Tweets FROM elon_tweets""")
    df=pd.read_sql_query(query,con=engine)
    index = random.choice(range(0, 2268))
    return df.iloc[[index]]        

def get_sentiment_for_top10_liked_tweets(): 
    query = (f"""SELECT Tweets FROM elon_tweets order by Likes DESC LIMIT 10;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## POST
def insert_one_row (day_, month_, year_, Tweets, Likes, Retweets):
    query = f"""INSERT INTO elon_tweets
     (day_, month_, year_, Tweets, Likes, Retweets) 
        VALUES ('{day_}', '{month_}', '{year_}', '{Tweets}', '{Likes}', '{Retweets}');
    """
    engine.execute(query)
    return f"Correctly introduced!"
