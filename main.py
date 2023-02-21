import time
import images
import os
import check
import notify
import atexit
from datetime import datetime, timedelta
from getpass import getpass
import constants as con
from pathlib import Path, PureWindowsPath
from database import Database
from test_post_data import show_data
import ai

def main():
	check.prepare_image_storage()
	root = con.ROOT_IMAGE_STORAGE

	db = Database()

	#getting passwords to log in
	if Path("passwords.txt").exists():
		with open("passwords.txt", "r") as f:
			passwords = f.read().split(",")
		password_resupply = passwords[0]
		password = passwords[1]
	else:
		password_resupply = getpass(f"Resupply:\nEnter your @{con.USERNAME_RESUPPLY} password: ")
		password = getpass(f"Post:\nEnter your @{con.USERNAME} password: ")


	while 1:
		wait_time = db.get_wait_time()

		allPosts=0
		startTime=time.time()

		#0) Check if image count below threshold, this one is bad, should check in each folder, not just future_images
		if images.count_images()<con.RESUPPLY_TRESHOLD:
			images.get_new_images(password_resupply) #steps a to c


		#1) Select a random image from future_images
		path = images.get_image()
		folder = (path.parts)[-2] #should return folder


		#2) Get random description and random 25 hashtags from db
		# caption = db.get_caption()
		caption = ai.get_caption()
		caption = caption + f"taken from: @{folder}"


		#3) Post image to Instagram, use show_data(path, caption) to see post in console
		if(images.post_image(image_url, caption)):
			#prepare data for printing
			allPosts+=1
			lastPost=datetime.now()
		else:
			print('Posting failed, need to try again later')
			wait_time = 3600
		
		upTime=round((time.time() - startTime)/3600, 4)
		nextPost=lastPost + timedelta(seconds=wait_time)

		#4) Print bot data and wait selected amount of time
		print(con.MENU.format(
							allPosts=allPosts,
							upTime=upTime,
							lastPost=lastPost.strftime('%H:%M:%S'),
							nextPost=nextPost.strftime('%H:%M:%S')))

		time.sleep(wait_time)

def send_notification():
	notify.pushbullet_message("Warning!", "Instagram bot has stopped!")

atexit.register(send_notification)

if __name__ == "__main__":
	main()

	#test
	# notify.pushbullet_message("Test", "This is a test message!")