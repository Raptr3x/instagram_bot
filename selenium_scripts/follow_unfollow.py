from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException, ElementNotVisibleException
import post_selenium as post

import sys
sys.path.append("../") #constants are folder up

import constants as con, time
import pyautogui as auto
from getpass import getpass

"""
Tasks:

    login()
    list people from hashtags
    follow x amount and add to db
    wait y time (in days)
    unfollow people from db
"""
