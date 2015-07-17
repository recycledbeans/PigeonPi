import tweepy
import os
import pygame
import credentials
import sys

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try
	username = sys.argv[0]
except Exception:
	print "Don't forget to supply a username!"
	exit(0)

me = api.get_user(username);

followers = me.followers_count

file_ = open('followers/' + username + '.txt', 'r+')

old_count = file_.read(10)

if int(followers) > int(old_count):
	print "New Follower!"
	pygame.mixer.init()
	pygame.mixer.music.load("yay.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue

file_.seek(0)
file_.truncate()
file_.write(str(followers))
file_.close()
