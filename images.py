from getpass import getpass
from pathlib import Path, PurePath
from database import Database
from datetime import datetime
import constants as con
import logging as log
import os
import check
import shutil
import random

log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)

"""
Used to work with images as in select image, get new images, post images, etc
"""

def count_images():
    count = 0
    for storage in os.listdir(con.ROOT_IMAGE_STORAGE):
        for profile in os.listdir(str(con.ROOT_IMAGE_STORAGE/storage)):
            for file in os.listdir(str(con.ROOT_IMAGE_STORAGE/storage/profile)):
                if (con.ROOT_IMAGE_STORAGE/storage/profile/file).is_file():
                    count+=1
    
    return count

def get_image():
    """
    Returns Path of selected image and folder name
    """
    folder = random.choice([folder for folder in con.IMAGE_STORAGE.iterdir()])
    return random.choice([img for img in folder.iterdir()])


def _is_new_dir_needed(profile):
    profile_folder = con.IMAGE_QUARANTINE/profile
    if not profile_folder.exists():
        Path.mkdir(profile_folder)


def get_new_images(password):
    """
    a) Populate quarantine directory
    b) Perform checks on downloaded image:
        I) Check image hash if similar has been posted
        II) Check image for human face
        III) Check image for red flag keywords (We don't want to pull advertisement images)
        IV) If at least one check is true, image is deleted
    c) Hash image after passing I) check - done in chec.py file
    """
    
    db = Database()
    
    profiles = db.get_resupply_targets() #returns list of touples

    quarantine = con.IMAGE_QUARANTINE

    #a) Populate quarantine directory
    for p in profiles:
        profile = p[0]        
        
        _is_new_dir_needed(profile)
        
        save_path = str(quarantine/profile)
        
        os.system(f'instaloader --login {con.USERNAME_RESUPPLY} --password {password} --no-metadata-json --no-captions --fast-update --no-profile-pic --dirname-pattern="{save_path}" {profile}')

        #b) Perform checks on downloaded images

        img_ls = [img for img in (quarantine/profile).iterdir()]
        
        for img in img_ls:
            img_path = img.resolve() # aabsolute path but still windwosPath obj, has to be casted to string
            if not check.check_hash(img_path) or not check.check_4_face(img_path) or not check.check_4_text(img_path):
                os.remove(img_path)
        
        shutil.move(str(con.IMAGE_QUARANTINE/profile), str(con.IMAGE_STORAGE/profile))

        log.info(f"Moved {profile} images to future_images")

def post_image(link,caption):
    '''
    Takes in link, caption, other vals are in constants and posts the img to Instagram
    Uses facebook graph api
    '''
    
    url = con.GRAPH_URL + con.INSTA_ACC_ID + '/media'

    param = dict()
    param['access_token'] = con.ACCESS_TOKEN
    param['caption'] = caption
    param['image_url'] = link
    
    response = requests.post(url, params=param)
    try:
        creation_id = response.json()['id'] # Should return a dict id:id_val if it fails, break func
    except Exception as e:
        print(e)
        return -1

    post_url = con.GRAPH_URL + con.INSTA_ACC_ID + '/media_publish'

    post_param = dict()
    post_param['access_token'] = con.ACCESS_TOKEN
    post_param['creation_id'] = creation_id

    response = requests.post(post_url,params=post_param)
    print(response.json())
    if(response.status_code!='200'):
        return -1
    else:
        return 0


if __name__ == "__main__":
    # passw = getpass("password: ")
    # get_new_images(passw)
    print(count_images())