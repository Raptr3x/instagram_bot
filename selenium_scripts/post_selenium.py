"""
Since there were some changes with the Instagram private API, instapy-cli won't be working in foreseeable future.
This script will be a temporary replacement for instapy-cli.
Due to Instagram API problems, this script will be using Selenium.
"""
import sys
sys.path.append(r"D:\Programiranje\Python_projects\bots\pc_setup_ideas-final")
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException, ElementNotVisibleException
import constants as con
import time
import pyautogui as auto
from getpass import getpass
from pathlib import Path

class Post_with_selenium:
    """
    Posts image to Instagram with Selenium
    
    Expected args:
        - image_path
        - caption
        - password (if not given, required to be entered by user)
 
    """
    def __init__(self, image_path, caption, password=False):
        self._username = con.USERNAME
        self._password = password if password else getpass(f"Please enter password for @{self._username} --> ")
        self._cookies = con.COOKIES_SELENIUM
        self._image_path = image_path
        self._caption = caption
        # self.main()
    
    def close_popups(self, xpath):
        for i in range(5):
            time.sleep(3)
            self._driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
            try:
                self._driver.find_element_by_xpath(xpath).click()
                break
            except:
                pass
    
    def check_connection(self):
        try:
            for i in range(10):
                main_msg = self._driver.find_element_by_xpath('//*[@id="main-message"]/h1/span')
                if main_msg == "This site can’t be reached":
                    print("Connection failed, refreshing")
                    self._driver.refresh()
                    time.sleep(10)
                else:
                    break
            return 0
        except NoSuchElementException:
            print("Couldn't find main msg so connection must be stable")
    
    def login(self):
        """
        From: https://github.com/Haffz/Python-Instagram-Bot/blob/master/instaLike.py
        """
        driver = con.CHROMEDRIVER_PATH
        driver.get("https://www.instagram.com/accounts/login")
        time.sleep(2)
        user_name_elem = driver.find_element_by_name('username')
        user_name_elem.clear()
        user_name_elem.send_keys(self._username)
        passworword_elem = driver.find_element_by_name('password')
        passworword_elem.clear()
        passworword_elem.send_keys(self._password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def main(self):
        
        #create self._driver object
        self._driver_path = con.CHROMEDRIVER_PATH

        self._url_login = con.INSTA_LOGIN_URL
        self._user_agent = con.USER_AGENT

        #logging in
        _options = Options()
        _options.add_argument("--log-level=1")
        #_options.add_argument("--silent")
        #_options.add_argument("--headless")
        _options.add_argument("--no-sandbox")
        #_options.add_argument("--disable-logging")
        _options.add_argument("--mute-audio")
        _options.add_argument("--start-maximized")
        _options.add_argument('--user-agent='+self._user_agent)
        self._driver = webdriver.Chrome(executable_path=self._driver_path,options=_options)
        self._driver.get(self._url_login)

        self.check_connection()
        try:
            for c in self._cookies:
                self._driver.add_cookie(c)
            self._driver.get(self._url_login)
            self.check_connection()
        except WebDriverException:
            print("Login with cookies failed")
            #enter login info, cookies didn't work
            self.login()
            try:
                self._driver.find_element_by_xpath("//button[contains(text(), 'Save Info')]").click()
                time.sleep(5)
            except:
                #no save info screen
                pass
            all_cookies = self._driver.get_cookies()
            with open("last_login_cookies.txt", "w") as f:
                f.write(str(all_cookies))
        try:
            #skip "this was me check"
            self.check_connection()
            time.sleep(3)
            self._driver.find_element_by_xpath("//button[contains(text(), 'This was me')]").click()
            time.sleep(3)
        except NoSuchElementException:
            pass
        #close pop-ups
        cookies = self._driver.get_cookies()
        print("logged in")
        self.check_connection()
        #self.close_popups("//*[@id='react-root']/section/main/div/button")
        self.close_popups("//button[contains(text(), 'Cancel')]") #cancel adding instagram to homescreen
                           #/html/body/div[4]/div/div/div[3]/button[2]
                           
                           #/html/body/div[4]/div/div/div[3]/button[2]
        self.check_connection()
        self.close_popups("//button[contains(text(), 'Not Now')]") #not now to turn on notifications
        #upload image
        try:
            self.check_connection()
            self._driver.find_element_by_xpath("//div[@role='menuitem']").click()
        except ElementNotVisibleException:
            #sometimes a popup blocks a post button on the bottom
            self.check_connection()
            self.close_popups("/html/body/div[4]/div/div[2]/div/div[5]/button")
        print(self._image_path)
        auto.typewrite(str(self._image_path))
        time.sleep(10)
        auto.press('enter')
        time.sleep(3)
        self.check_connection()
        self._driver.find_element_by_xpath("//button[contains(text(), 'Next')]").click() #old xpath for Next "//*[@id='react-root']/section/div[1]/header/div/div[2]/button"
        time.sleep(3)
        self.check_connection()
        self._driver.find_element_by_tag_name("textarea").send_keys(self._caption) #old xpath for textarea '//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea'
        time.sleep(3)
        self.check_connection()
        self._driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click() #old xpath for Done "//*[@id='react-root']/section/div[1]/header/div/div[2]/button"
        time.sleep(4)
        self._driver.close()
        
        

if __name__ == "__main__":
    print("Runing as test")
    p = Post_with_selenium(Path("C:/Users/bogda/OneDrive/Desktop/rest/bot_windows/test.jpg"), "Final testing")