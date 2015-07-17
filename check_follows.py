# Import all of the necessary modules
import os
import sys
import tweepy
import pygame
import credentials # <---- Be sure to put your Twitter application's credentials here

# Tweepy OAuth (Authentication)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initiate the Tweepy API class
api = tweepy.API(auth)

# Making sure we have entered a username argument
try
	username = sys.argv[0]
except Exception:
	print "Don't forget to supply a username!"
	exit(0)

# Tweepy calls the get_user Twitter API call
me = api.get_user(username);

# This is the number of our followers (in string form)
followers = me.followers_count

# Open up a file for caching the username's followers
file_ = open('followers/' + username + '.txt', 'r+')

# How many followers did we have the last time we checked?
old_count = file_.read(10)

# If we have more followers:
if int(followers) > int(old_count):
	# Show it on the terminal screen
	print "New Follower!"
	# Play the including mp3 file
	pygame.mixer.init()
	pygame.mixer.music.load("yay.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue

# Overwrite the old amount of followers with the new amount
file_.seek(0)
file_.truncate()
file_.write(str(followers))
file_.close()
