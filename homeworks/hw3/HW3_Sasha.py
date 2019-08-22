# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:20:44 2019

@author: degte
"""
import datetime 
import tweepy
import imp
import sys
import time
import csv

twitter = imp.load_source('twit', '/Users/degte/Desktop/classes/2_year/Python/Twitter/start_twitter.py')
api = twitter.client

## This code initially was a draft and at some point when I got lost (it was messy)
## I created the one which crushed. So there are just basic structure and ideas.

# The code I found here https://psylica.com/blog/2017/May/03/listing-twitter-followers-tweepy.html
# while I was trying to recollect what I had done befor Spyder crushed
# It works, but it is not mine. I have questions about how it works

#users = tweepy.Cursor(api.followers, screen_name="WUSTL").items()
#HEADER = ['Screenname']
#def processing_loop(csvfile):
#    csv_writer = csv.writer(csvfile)
#    csv_writer.writerow(HEADER)
#
#    while True:
#        try:
#            user = next(users)
#        except tweepy.TweepError:
#            time.sleep(60*20)
#            user = next(users)
#        except StopIteration:
#            break
#        csv_writer.writerow([user.screen_name])
#        csv_writer.writerow([user.followers_count])
#        csv_writer.writerow([user.statuses_count])
#        csvfile.flush()
#        time.sleep(5)
#with open('results.csv', 'w') as csvfile:
#    processing_loop(csvfile)

#I tried to modify it but it breaks
#    with open('results.csv', 'w') as f:
#        w = csv.DictWriter(f, fieldnames = ("nick", "followers", "tweets"))
#        w.writeheader()
#        users = tweepy.Cursor(api.followers, screen_name="WUSTL").items()
#        wustl_followers_data = []
#        while True:
#            try:
#                user = next(users)
#            except tweepy.TweepError:
#                time.sleep(60*15)
#                user = next(users)
#            except StopIteration:
#                break
#            wustl_followers_data["nick"] = user.screen_name
#            wustl_followers_data["followers"] = user.followers_count
#            wustl_followers_data["tweets"] = user.statuses_count
#            time.sleep(5)
#            w.writerow(wustl_followers_data)

#HEre is something what reminds my initial code. It does not work

wustl_followers = []
for item in tweepy.Cursor(api.followers_ids, 'WUSTL').items():
	try: 
        wustl_followers.append(item)
    except tweepy.RateLimitError: 
        pass
        sys.sleep(15*60)
        wustl_followers.append(item)

wustl_followers_info = []

for i in wustl_followers: 
    try: 
        someone = api.get_user('i')
        wustl_followers_info ["name"] = someone.screen_name
        wustl_followers_info ["followers"] = someone.followers_count
        wustl_followers_info ["statuses"] = someone.statuses_count
    except tweepy.RateLimitError: 
        pass
        sys.sleep(15*60)
        someone = api.get_user('i')
        wustl_followers_info ["name"] = someone.screen_name
        wustl_followers_info ["followers"] = someone.followers_count
        wustl_followers_info ["statuses"] = someone.statuses_count

# Question 1 - answer
sorted(wustl_followers_info, key=followers.__getitem__, reverse=True)

# Question 2 - answer
sorted(wustl_followers_info, key=statuses.__getitem__, reverse=True)
    

#Genereal things for questions 3 and 4
    
wustl_follows = []
wustl_follows_info = []

for item in tweepy.Cursor(api.friends_ids, 'WUSTL').items():
	try: 
        wustl_follows.append(item)
    except tweepy.RateLimitError: 
        pass
        sys.sleep(15*60)
        wustl_follows.append(item)

for i in wustl_follows: 
    try: 
        someone = api.get_user('i')
        wustl_follows_info ["name"] = someone.screen_name
        wustl_follows_info ["followers"] = someone.followers_count
        wustl_follows_info ["statuses"] = someone.statuses_count
    except tweepy.RateLimitError: 
        pass
        sys.sleep(15*60)
        someone = api.get_user('i')
        wustl_follows_info ["name"] = someone.screen_name
        wustl_follows_info ["followers"] = someone.followers_count
        wustl_follows_info ["statuses"] = someone.statuses_count

#Question 3
sorted(wustl_follows_info, key=followers.__getitem__, reverse=True))
    
#Question 4
layman = []
expert = []
celebrity = []

for i in wustl_follows_info:
    if wustl_follows_info ["followers"] < 100:
        layman.append(i)
    elif wustl_follows_info ["followers"] > 100 and wustl_follows_info ["followers"] < 1000:
        expert.append(i)
    else:
        celebrity.append(i)

sorted(layman, key=statuses.__getitem__, reverse=True)
sorted(expert, key=statuses.__getitem__, reverse=True)
sorted(celebrity, key=statuses.__getitem__, reverse=True)

## Questions 5 

wustlps_followers = []
wustlps_followers_data = []
for item in tweepy.Cursor(api.followers_ids, 'WUSTLPoliSci').items():
	try: 
        wustlps_followers.append(item)
        try: 
            for item in tweepy.Cursor(api.followers_ids, item).items():
            wustlps_followers.append(item)
        except tweepy.RateLimitError: 
            pass
            sys.sleep(15*60)
            wustlps_followers.append(item)
    except tweepy.RateLimitError: 
        pass
        sys.sleep(15*60)
        wustlps_followers.append(item)
        
for i in wustlps_followers: 
    try: 
        someone = api.get_user('i')
        wustlps_followers_data ["name"] = someone.screen_name
        wustlps_followers_data ["statuses"] = someone.statuses_count
    except tweepy.RateLimitError: 
        pass
        sys.sleep(15*60)
        someone = api.get_user('i')
        wustlps_followers_data ["name"] = someone.screen_name
        wustlps_followers_data ["statuses"] = someone.statuses_count

sorted(wustlps_followers_data, key=statuses.__getitem__, reverse=True)
         
#Question6

wustlps_follows = []
wustlps_follows_data = []
for item in tweepy.Cursor(api.friends_ids, 'WUSTLPoliSci').items():
	try: 
        wustlps_follows.append(item)
        try: 
            for item in tweepy.Cursor(api.friends_ids, item).items():
            wustlps_follows.append(item)
        except tweepy.RateLimitError: 
            pass
            sys.sleep(15*60)
            wustlps_follows.append(item)
    except tweepy.RateLimitError: 
        pass
        sys.sleep(15*60)
        wustlps_follows.append(item)
        
for i in wustlps_follows: 
    try: 
        someone = api.get_user('i')
        wustlps_follows_data ["name"] = someone.screen_name
        wustlps_follows_data ["statuses"] = someone.statuses_count
    except tweepy.RateLimitError: 
        pass
        sys.sleep(15*60)
        someone = api.get_user('i')
        wustlps_follows_data ["name"] = someone.screen_name
        wustlps_follows_data ["statuses"] = someone.statuses_count

sorted(wustlps_follows_data, key=statuses.__getitem__, reverse=True)

