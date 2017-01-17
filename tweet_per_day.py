import tweepy
import csv
import sys
from collections import Counter
from collections import OrderedDict


consumer_key = "xyz"
consumer_secret = "xyz"

access_token = "xyz"
access_token_secret = "xyz"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())
#print api.home_timeline()
public_tweets = api.user_timeline(id='OfficeOfRG',count='200')
#print(public_tweets)
i=1
datetime = []
for tweets in public_tweets:
    #print(tweets)
    datetime.append(tweets['created_at'][4:10]+ " " +tweets['created_at'][26:] )
counts = Counter(datetime)
datetime = dict(counts)

print(datetime)

with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)       
    writer.writerow(['date', 'frequency'])

with open('dict.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in datetime.items():        
        writer.writerow([key, value])
       
csv.field_size_limit(sys.maxsize)
csv.writer(open('data.tsv', 'w+'), delimiter="\t").writerows(csv.reader(open('dict.csv')))
