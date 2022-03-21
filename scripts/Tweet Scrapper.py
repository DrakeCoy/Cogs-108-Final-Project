# Script Author: Martin Beck
# Medium Article Follow-Along: https://medium.com/better-programming/how-to-scrape-tweets-with-snscrape-90124ed006af

# Pip install the command below if you don't have the development version of snscrape 
# !pip install git+https://github.com/JustAnotherArchivist/snscrape.git

# Run the below command if you don't already have Pandas
# !pip install pandas

# Imports
import os
import pandas as pd

# Below are two ways of scraping using CLI commands.
# Comment or uncomment as you need. If you currently run the script as is it will scrape both queries
# then output two different csv files.

# Query by username
# Setting variables to be used in format string command below
tweet_count = 10000
username = "jack"

# Using OS library to call CLI commands in Python
os.system("snscrape --jsonl --max-results {} twitter-search 'from:{}'> user-tweets.json".format(tweet_count, username))

# Reads the json generated from the CLI command above and creates a pandas dataframe
tweets_df1 = pd.read_json('user-tweets.json', lines=True)

# Displays first 5 entries from dataframe
# tweets_df1.head()

# Export dataframe into a CSV
tweets_df1.to_csv('user-tweets.csv', sep=',', index=False)
