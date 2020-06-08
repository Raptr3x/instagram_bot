# instagram_bot
Bot that runs @pc_setup_ideas page on instagram

### Main workflow
```
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
```