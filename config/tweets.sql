drop database if exists tweets; 
create database tweets;
use tweets;
drop table if exists elon_tweets; 

create table elon_tweets
(day_ int, 
month_ int, 
year_ int, 
Tweets text, 
Likes int, 
Retweets int); 

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/elon_tweets.csv'
	INTO TABLE elon_tweets
		FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\r\n'
        IGNORE 1 ROWS;
        
select * from elon_tweets;                
SELECT month, sum(Retweets) AS 'rt'
    FROM elon_tweets
    GROUP BY month
    ORDER BY month ASC ;
    
SELECT month, sum(Likes) AS 'Likes'
    FROM elon_tweets
    GROUP BY month
    ORDER BY month ASC ;
    
select count(*)
from elon_tweets