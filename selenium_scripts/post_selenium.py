import sys
sys.path.append(r"D:\Programiranje\Python_projects\bots\pc_setup_ideas-final")
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException, ElementNotVisibleException
import constants as con
import time
import logging as log
import pyautogui as auto
from getpass import getpass
from pathlib import Path


log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)


def _wait(wtime=5):
    log.info(f"Waiting {wtime} to make sure everything loads")
    time.sleep(wtime)
    log.info(f"{wtime} seconds has passed, continuing")


def _remove_popup_using(driver, xpath=0, link_text=0):
    _wait()
    try:
        if link_text:
            driver.find_element_by_link_text(text).click()
        elif xpath:
            driver.find_element_by_xpath(xpath).click()
        else:
            log.warning("please only define either xpath or link_text.")
            return 1


        log.info("Removed popup")
    except Exception as ಠ_ಠ:
        log.warning(ಠ_ಠ)


def _remove_popups(driver):
    """
    Whenever there is a popup blocking post button, usually it's one of these.

    If there is a new one, just call _remove_popup_using() and pass in
    xpath or link text of popup button you need clicked.
    """
    _remove_popup_using(driver, link_text="Not Now")
    _remove_popup_using(driver, "//button[contains(text(), 'Save Info')]")
    _remove_popup_using(driver, "//button[contains(text(), 'This was me')]")
    _remove_popup_using(driver, "//button[contains(text(), 'Not Now')]")
    _remove_popup_using(driver, "//button[contains(text(), 'Cancel')]")
    _remove_popup_using(driver, "/html/body/div[4]/div/div[2]/div/div[5]/button")

def get_driver():
    user_agent = con.USER_AGENT
    
    driver_path = con.CHROMEDRIVER_PATH

    options = Options()
    # options.add_argument("--log-level=1")
    #options.add_argument("--silent")
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-logging")
    options.add_argument("--mute-audio")
    options.add_argument("--start-maximized")
    options.add_argument('--user-agent='+user_agent)

    return webdriver.Chrome(executable_path=driver_path,options=options)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(con.INSTA_LOGIN_URL)

    def login(self, username, password):
        log.info("On login page now")
        _wait()
        log.info("Entering username")
        self.driver.find_element_by_name('username').send_keys(username)
        log.info("Entering password")
        self.driver.find_element_by_name('password').send_keys(password)
        log.info("Trying to log in")
        self.driver.find_element_by_name('password').send_keys(Keys.RETURN)
        _wait()


class FeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(con.INSTA_FEED_URL)

    def goto_post(self):
        log.info("On feed page now")
        _wait()
        unable = 1
        while unable:
            try:
                #try to go to upload page but it probably won't work immediately
                log.info("Trying to click post image button")

                self.driver.find_element_by_xpath("//div[@role='menuitem']").click()
                unable=0
            except Exception as ಠ_ಠ:
                log.warning(f"Unable to click, error:\n{ಠ_ಠ}")
                _remove_popups(self.driver)


class PostMediaPage:
    def __init__(self, driver):
        self.driver = driver
    
    def postMedia(self, image_path, caption):
        _wait()
        
        #upload image
        auto.typewrite(str(image_path))
        auto.press('enter')
        
        #go next
        self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]").click()

        _wait()

        #enter caption
        self.driver.find_element_by_tag_name("textarea").send_keys(caption)

        #share media
        self.driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()
        
        _wait()

        #close browser
        self.driver.close()


if __name__ == "__main__":
    log.info("Runing as test")


    with open("passwords.txt", "r") as f:
        ps = f.read()
        password = ps.split(",")[0]


    driver = get_driver()

    loginPage = LoginPage(driver)
    loginPage.login(con.USERNAME_RESUPPLY, password)

    feed = FeedPage(driver)
    feed.goto_post()

    postPage = PostMediaPage(driver)
    postPage.postMedia(r"../test_img.jpg", "testing")