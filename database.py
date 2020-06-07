import sqlite3
import os
import random
from datetime import datetime
from PIL import Image

class Database:


    def __init__(self):
        """
        Initializes the database
        """
        self.conn  = sqlite3.connect("settings.db")
        self.c = self.conn.cursor()


    def close_database(self):
        """
        Commits and closes the database
        Requires instance of self.conn object to be passed
        """
        self.conn.commit()
        self.conn.exit()


    def get_resupply_targets(self):
        return self.c.execute("SELECT username FROM dataTargets").fetchall()


    def store_image_hash(self, image_path, hash):
        """
        Stores image hash in the database to be used for hash checks later on
        """
        self.c.execute("INSERT INTO imageHashes VALUES(?,?,?)", (image_path.name, str(hash), datetime.now()))
        self.conn.commit()


    def get_caption(self):
        
        """
        Pulls a caption and 25 hashtags from database

        Image owner username (img folder name) should be added to the end of return value!

        Returns a str which is a formated caption + hashtags
        """

        #I know it's not the fastest way but it's a really small table
        caption = self.c.execute("SELECT caption FROM captions ORDER BY random() LIMIT 1").fetchone()[0]
        
        shitstorm = self.c.execute("SELECT hashtag FROM hashtags ORDER BY random() LIMIT 25").fetchall()
        
        #casting that multidimensional tuple-list shitstorm into something less cancerous
        hashtags = ' '.join(i[0] for i in shitstorm)

        text = f"{caption}\r\n|tags:\n{hashtags}\r\n"

        return text

    def get_image_hashes(self):
        """
        Returns db cursor
        """
        self.c.execute("SELECT image_name, image_hash FROM imageHashes")
        
        if not self.c:
            log.info("No hashes to compare with")
            return None
        
        return self.c


    def get_wait_time(self):
        """
        Pulls min and max waiting time from database
        
        Returns random int between min and max wait time
        """
        time = self.c.execute("SELECT * FROM wait_time").fetchone()
        
        return random.randint(time[0], time[1])


if __name__ == "__main__":
    db = Database()
    caption = db.get_caption()
    wait_time = db.get_wait_time()
    dataTargets = db.get_resupply_targets()
    print(caption,"\n",wait_time,"\n",dataTargets)
    