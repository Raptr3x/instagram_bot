import platform
import os
import imghdr
from database import Database
from PIL import Image
import pytesseract
import constants as con
import numpy as np
import cv2
import logging as log
from pathlib import Path

log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)

def prepare_image_storage():
    storage_list = [con.ROOT_IMAGE_STORAGE, con.IMAGE_QUARANTINE, con.IMAGE_STORAGE, con.SUBMISSION_STORAGE]

    for folder in storage_list:
        if not folder.exists():
            Path.mkdir(folder)

def _is_image(image_path):
    """
    Checks if a file is jpg

    All files that will be downloaded are jpg or mp4
    """
    if image_path.suffix==".jpg":
        return True
    return False

def diff(h1, h2):
    return sum([bin(int(a, 16) ^ int(b, 16)).count('1') for a, b in zip(h1, h2)])


def dhash(image, hash_size = 8):
    # scaling and grayscaling
    image = image.convert('L').resize((hash_size + 1, hash_size), Image.ANTIALIAS)
    pixels = list(image.getdata())

    # calculate differences
    diff_map = []
    for row in range(hash_size):
        for col in range(hash_size):
            diff_map.append(image.getpixel((col, row)) > image.getpixel((col + 1, row)))
    # build hex string
    return hex(sum(2**i*b for i, b in enumerate(reversed(diff_map))))[2:-1]


def check_hash(image_path):
    """
    Checks if image hasn't been posted before by comparing image hash with hashes from database
    """
    #throws OSError if file is not an image
    if _is_image(image_path):

        img = Image.open(image_path)
        hash = dhash(img)

        db = Database()
        cursor = db.get_image_hashes() 
        
        for row in cursor: # row index 0=image name, 1=image hash, 2=post date and time
            dif = diff(hash, row[1])
            if diff(hash, row[1])<15:
                log.info("Similar image has been posted")
                return False

        log.info("Similar image hasn't been posted")
        #adding hash to db, even if it fails other tests, it will be there so it will fail this one again next time
        db.store_image_hash(image_path, hash)
        return True
    
    log.info("Filetype is not supported for hashcheck")
    return False


def check_4_text(image_path):
    """
    Checks for keywords in image
    Returns True for images that don't have any unwanted words in them
    Returns False for images that have them
    """

    if platform.system() == "Windows":
        pytesseract.pytesseract.tesseract_cmd = "D:\\installed_software\\Tesseract-OCR\\tesseract.exe"

    image_text = pytesseract.image_to_string(Image.open(str(image_path)), config='').split()
    image_text = [word.lower() for word in image_text]

    for word in con.REDFLAG_KEYWORDS:
        if word in image_text:
            log.info("Redflag keyword found")
            return False
    return True

def check_4_face(image_path):
    """
    uses haar-wavelet transform to detect faces in images
    """
    image_path = str(image_path)
    face_file_path = Path("face_recognition_files")
    face_cascade = cv2.CascadeClassifier(str(face_file_path/"haarcascade_frontalface_default.xml"))
    eye_cascade = cv2.CascadeClassifier(str(face_file_path/"haarcascade_eye.xml"))

    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #I'll keep it there so I can check in future what was recognized in case it was a mistake
        roi_gray = gray[y:y-int((y + h) * 0.7), x:x+w]
        roi_color = img[y:y-int((y + h) * 0.7), x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            log.info("Face found in the image")
            return False

    return True


if __name__ == "__main__":
    image_path = Path("test_img.jpg")
    log.info(check_4_face(image_path))
    log.info(check_4_text(image_path))
    log.info(check_hash(image_path))
