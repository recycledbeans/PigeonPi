import tweepy
import os
import pygame

consumer_key = 'ENTERYOURCONSUMERKEY'
consumer_secret = 'ENTERYOURCONSUMERSECRET'
access_token = 'ENTERYOURACCESSTOKEN'
access_token_secret = 'ENTERYOURACCESSTOKENSECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

me = api.get_user('@recycledbeans');

followers = me.followers_count

file_ = open('current_followers.txt', 'r+')

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
