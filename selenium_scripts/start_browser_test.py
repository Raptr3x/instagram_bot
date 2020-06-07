import sys
sys.path.append("C:\\instagram_bot\\bot")
import constants as con
from selenium import webdriver
from selenium.webdriver.chrome.options import *


driver_path = "C:\\instagram_bot\\bot\\chromedriver.exe"
user_agent = con.USER_AGENT
url_login = con.INSTA_LOGIN_URL
cookies = con.COOKIES_SELENIUM

_options = Options()
_options.add_argument("--log-level=1")
#_options.add_argument("--silent")
#_options.add_argument("--headless")
_options.add_argument("--no-sandbox")
#_options.add_argument("--disable-logging")
_options.add_argument("--mute-audio")
_options.add_argument('--user-agent='+user_agent)

driver = webdriver.Chrome(executable_path=driver_path, options=_options)

driver.get(url_login)
for c in cookies:
    driver.add_cookie(c)
driver.get(url_login)
