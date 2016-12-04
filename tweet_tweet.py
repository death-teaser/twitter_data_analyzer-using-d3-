import tweepy
import csv
import sys

consumer_key = "cOkexDviXh1SjdLxjjexgnvh4"
consumer_secret = "GF7e6YYb5dr3g9yhI17rfkU47XmbhWI8tiKi1mMPkmHZhYqMlO"

access_token = "788648645985873921-7BcDx5lFjSDnHS0ACHQHK2N4qixdNJH"
access_token_secret = "fMx4ifSoCkXKwCBwAUAsUh1gdU6YNB7uVHXIjmE4gDQA1"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#print api.home_timeline()
#public_tweets = api.update_status(status="Hello frnds")

print("Enter the handle of user")
abc = input()


print("Enter total no of topic ,with u want to create graph (max 10)(you can enter max 10 name per topic):")
word0=[]
word1=[]
word2=[]
word3=[]
word4=[]
word5=[]
word6=[]
word7=[]
word8=[]
word9=[]
topic = int(input())
i=1
print("How many word u want to insert in topic"+str(i))
i=i+1
total=int(input())
for j in range(0,total):
                        word=input()
                        word0.append(word)
            
if topic > 1:
                        
                        print("How many word u want to insert in topic"+str(i))
                        i=i+1
                        total=int(input())
                        for j in range(0,total):
                                                word=input()
                                                word1.append(word)
if topic > 2:
                        
                        print("How many word u want to insert in topic"+str(i))
                        i=i+1
                        total=int(input())
                        for j in range(0,total):                        
                                                word=input()
                                                word2.append(word)
if topic > 3:            
                        print("How many word u want to insert in topic"+str(i))
                        i=i+1
                        total=int(input())
                        for j in range(0,total):                        
                                                word=input()
                                                word3.append(word)                        
if topic > 4:            
                        print("How many word u want to insert in topic"+str(i))
                        i=i+1
                        total=int(input())
                        for j in range(0,total):                        
                                                word=input()
                                                word4.append(word)
if topic > 5:            
                        print("How many word u want to insert in topic"+str(i))
                        i=i+1
                        total=int(input())
                        for j in range(0,total):                        
                                                word=input()
                                                word5.append(word)
if topic > 6:            
                        print("How many word u want to insert in topic"+str(i))
                        i=i+1
                        total=int(input())
                        for j in range(0,total):                        
                                                word=input()
                                                word6.append(word)
if topic > 7:            
                        print("How many word u want to insert in topic"+str(i))
                        i=i+1
                        total=int(input())
                        for j in range(0,total):                        
                                                word=input()
                                                word7.append(word)
if topic > 8:            
                        print("How many word u want to insert in topic"+str(i))
                        i=i+1
                        total=int(input())
                        for j in range(0,total):                       
                                                word=input()
                                                word8.append(word)
if topic > 9:            
                        print("How many word u want to insert in topic"+str(i))
                        total=int(input())
                        for j in range(0,total):                        
                                                word=input()
                                                word9.append(word)
                                                
                                                
public_tweets = api.user_timeline(id=str(abc),count='200')

data=[]
for tweet in public_tweets:        
                        data.append(tweet.text)
                        
                        
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
k=0
l=0
for tweets in data:
                        for j in word0:
                                                if j in tweets:
                                                                        a=a+1
                                                                        break
                        if topic > 1:                        
                                                for j in word1:
                                                                        if j in tweets:
                                                                                                b=b+1
                                                                                                break
                        if topic > 2:
                                                for j in word2:
                                                                        if j in tweets:
                                                                                                c=c+1
                                                                                                break
                        if topic > 3:
                                                for j in word3:
                                                                        if j in tweets:
                                                                                                d=d+1
                                                                                                break
                        if topic > 4:
                                                for j in word4:
                                                                        if j in tweets:
                                                                                                e=e+1
                                                                                                break
                        if topic > 5:
                                                for j in word5:
                                                                        if j in tweets:
                                                                                                f=f+1
                                                                                                break
                        if topic > 6:                        
                                                for j in word6:
                                                                        if j in tweets:
                                                                                                g=g+1
                                                                                                break
                        if topic > 7:
                                                for j in word7:
                                                                        if j in tweets:
                                                                                                h=h+1
                                                                                                break
                        if topic > 8:
                                                for j in word8:
                                                                        if j in tweets:
                                                                                                k=k+1
                                                                                                break
                        if topic > 9:
                                                for j in word9:
                                                                        if j in tweets:
                                                                                                l=l+1
                                                                                                break                                                                         
toCSV=[]
A={'topic':word0[0],'frequency':a}
toCSV.append(A)
if topic > 1:                        
                        B={'topic':word1[0],'frequency':b}
                        toCSV.append(B)
if topic > 2:                        
                        C={'topic':word2[0],'frequency':c}
                        toCSV.append(C)
if topic > 3:
                        D={'topic':word3[0],'frequency':d}
                        toCSV.append(D)
if topic > 4:
                        E={'topic':word4[0],'frequency':e}
                        toCSV.append(E)
if topic > 5:
                        F={'topic':word5[0],'frequency':f}
                        toCSV.append(F)
if topic > 6:
                        G={'topic':word6[0],'frequency':g}
                        toCSV.append(G)
if topic > 7:
                        H={'topic':word7[0],'frequency':h}
                        toCSV.append(H)
if topic > 8:
                        K={'topic':word8[0],'frequency':k}
                        toCSV.append(K)
if topic > 9:
                        L={'topic':word9[0],'frequency':l}
                        toCSV.append(L)


print(toCSV)

keys = toCSV[0].keys()
with open('names.csv', 'w') as output_file:
                        
                        dict_writer = csv.DictWriter(output_file, keys)
                        dict_writer.writeheader()
                        dict_writer.writerows(toCSV)


csv.field_size_limit(sys.maxsize)
csv.writer(open('data.tsv', 'w+'), delimiter="\t").writerows(csv.reader(open('names.csv')))


''''word1 =["pm","मोदी","narendra","modi","primeminister","PM","पीएम","Modi","प्रधानमंत्री","Prime Minister","नरेंद्र"]
word2 = ["bjp","BJP"]
word3=["सूट","suit"]
word4=["demonitization","scam","demonetization","Demonetisation"]
word5=["कालाधन","black"]
data=[]'''


    