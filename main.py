import time
import images
import os
from datetime import datetime, timedelta
from getpass import getpass
import constants as con
from pathlib import Path, PureWindowsPath
from database import Database
from test_post_data import show_data

"""
0) Check if image count below threshold, if true:
	a) Populate quarantine directory
	b) Perform checks on downloaded image:
		I) Check image hash if similar has been posted
		II) Check image for human face
		III) Check image for red flag keywords (We don't want to pull advertisement images)
		IV) If at least one check is true, image is deleted
	c) Hash images that remained and move them to future_images directory
1) Select a random image from future_images
2) Get random description and random 25 hashtags from db
3) Post image to Instagram
4) Print bot data and wait selected amount of time, go to 0)
"""

db = Database()
wait_time = db.get_wait_time()
allPosts=0
startTime=time.time()
password = getpass("Enter your password: ")
root = con.ROOT_IMAGE_STORAGE
resupply_threshold = 10 #threshold for resupplying

while 1:
	#0) Check if image count below threshold
	if len(os.listdir(root/"future_images"))<resupply_threshold:
		images.get_new_images(password) #steps a to c


	#1) Select a random image from future_images
	path = images.get_image()
	folder = (path.parts)[-2] #should return folder


	#2) Get random description and random 25 hashtags from db
	caption = db.get_caption()
	caption = caption + f"taken from: @{folder}"


	#3) Post image to Instagram
	show_data(path, caption)


	#prepare data for printing
	allPosts+=1
	upTime=round((time.time() - startTime)/3600, 4)
	lastPost=datetime.now()
	nextPost=lastPost + timedelta(seconds=wait_time)

	#4) Print bot data and wait selected amount of time
	print(con.MENU.format(
						allPosts=allPosts,
						upTime=upTime,
						lastPost=lastPost.strftime('%H:%M:%S'),
						nextPost=nextPost.strftime('%H:%M:%S')))

	time.sleep(wait_time)
