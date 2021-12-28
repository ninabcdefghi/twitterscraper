import snscrape.modules.twitter as sntwitter
import csv
import pandas as pd
from nltk.tokenize import TweetTokenizer

tokenizer = TweetTokenizer()

def scrape_users(users, zeitraum):
    for user in users:

        tweets_list = [['date', 'id', 'text', 'username']]
        
        conditions = 'from:{} {}'.format(user, zeitraum)

        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(conditions).get_items()): #declare a username 
            tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username]) #declare the attributes to be returned
        
        print(tweets_list)
        tweets_df = pd.DataFrame(tweets_list, columns=['date', 'id', 'text', 'username'])

        tweets_df["tokenized_text"] = tokenizer.tokenize(tweets_df["text"])

        # add to csv
        tweets_df.to_csv('csvtesttt.csv', mode='a', header=False)

def main():
    users = ["OlafScholz", "jensspahn", "c_lindner", "SWagenknecht"]
    zeitraum = "since:2017-10-24 until:2017-10-27" # 2021
    scrape_users(users, zeitraum)


main()