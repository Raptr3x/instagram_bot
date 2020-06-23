from pathlib import Path
import platform
from selenium import webdriver


USERNAME = "pc_setup_ideas"
USERNAME_RESUPPLY = "loves_and_fluffs"

if USERNAME == "pc_setup_ideas":
    COOKIES_SELENIUM = [{'domain': '.instagram.com', 'httpOnly': True, 'name': 'urlgen', 'path': '/', 'secure': True, 'value': '"{/"80.110.116.122/": 6830}:1ibtQ4:13bRDQD7qOXIOsPihtpEMuO28O8"'}, {'domain': '.instagram.com', 'httpOnly': False, 'name': 'ds_user_id', 'path': '/', 'secure': True, 'value': '9192513055'}, {'domain': '.instagram.com', 'httpOnly': True, 'name': 'ig_did', 'path': '/', 'secure': True, 'value': '3DD9BF31-BA14-4C8E-99D1-CE25CD95CE2F'}, {'domain': 'www.instagram.com', 'httpOnly': False, 'name': 'ig_cb', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.instagram.com', 'httpOnly': True, 'name': 'rur', 'path': '/', 'secure': True, 'value': 'FTW'}, {'domain': '.instagram.com', 'httpOnly': True, 'name': 'shbts', 'path': '/', 'secure': True, 'value': '1575322787.2666047'}, {'domain': '.instagram.com', 'httpOnly': False, 'name': 'mid', 'path': '/', 'secure': True, 'value': 'XeWEoQAAAAF4zuShuQ0JIFOElFit'}, {'domain': '.instagram.com', 'httpOnly': False, 'name': 'csrftoken', 'path': '/', 'secure': True, 'value': 'aLpoPVH5NUpKztX66v5oq6Hqr8YHQAeZ'}, {'domain': '.instagram.com', 'httpOnly': True, 'name': 'sessionid', 'path': '/', 'secure': True, 'value': '9192513055%3AC0lXYUlZOXc53f%3A22'}, {'domain': '.instagram.com', 'httpOnly': True, 'name': 'shbid', 'path': '/', 'secure': True, 'value': '7777'}]
    COOKIE = '{"uuid": "0b1d8898-0225-11ea-9980-54e1ad37e19a", "device_id": "android-0b1d8899022511ea", "ad_id": "b08a66ff-4ee7-6da9-1999-bdde52b29123", "session_id": "0b1d889a-0225-11ea-a01c-54e1ad37e19a", "cookie": {"__class__": "bytes", "__value__": "gAN9cQBYDgAAAC5pbnN0YWdyYW0uY29tcQF9cQJYAQAAAC9xA31xBChYCQAAAGNzcmZ0b2tlbnEF\nY2h0dHAuY29va2llamFyCkNvb2tpZQpxBimBcQd9cQgoWAcAAAB2ZXJzaW9ucQlLAFgEAAAAbmFt\nZXEKWAkAAABjc3JmdG9rZW5xC1gFAAAAdmFsdWVxDFggAAAAanZ6RVV4aWVVZlA0dElvQlZsNmpz\nd2llN01MQmV0VnBxDVgEAAAAcG9ydHEOTlgOAAAAcG9ydF9zcGVjaWZpZWRxD4lYBgAAAGRvbWFp\nbnEQWA4AAAAuaW5zdGFncmFtLmNvbXERWBAAAABkb21haW5fc3BlY2lmaWVkcRKIWBIAAABkb21h\naW5faW5pdGlhbF9kb3RxE4hYBAAAAHBhdGhxFGgDWA4AAABwYXRoX3NwZWNpZmllZHEViFgGAAAA\nc2VjdXJlcRaIWAcAAABleHBpcmVzcRdKa0SlX1gHAAAAZGlzY2FyZHEYiVgHAAAAY29tbWVudHEZ\nTlgLAAAAY29tbWVudF91cmxxGk5YBwAAAHJmYzIxMDlxG4lYBQAAAF9yZXN0cRx9cR11YlgDAAAA\ncnVycR5oBimBcR99cSAoaAlLAGgKWAMAAABydXJxIWgMWAMAAABQUk5xImgOTmgPiWgQWA4AAAAu\naW5zdGFncmFtLmNvbXEjaBKIaBOIaBRoA2gViGgWiGgXTmgYiGgZTmgaTmgbiWgcfXEkWAgAAABI\ndHRwT25seXElTnN1YlgDAAAAbWlkcSZoBimBcSd9cSgoaAlLAGgKaCZoDFgcAAAAWGNWaVp3QUJB\nQUZHamlYQ1RhdG81ZkdLTmhaa3EpaA5OaA+JaBBYDgAAAC5pbnN0YWdyYW0uY29tcSpoEohoE4ho\nFGgDaBWIaBaIaBdKZ2WRcGgYiWgZTmgaTmgbiWgcfXErdWJYBwAAAGRzX3VzZXJxLGgGKYFxLX1x\nLihoCUsAaApoLGgMWA4AAABwY19zZXR1cF9pZGVhc3EvaA5OaA+JaBBYDgAAAC5pbnN0YWdyYW0u\nY29tcTBoEohoE4hoFGgDaBWIaBaIaBdKawk8XmgYiWgZTmgaTmgbiWgcfXExWAgAAABIdHRwT25s\neXEyTnN1YlgFAAAAc2hiaWRxM2gGKYFxNH1xNShoCUsAaApoM2gMWAQAAAA3Nzc3cTZoDk5oD4lo\nEFgOAAAALmluc3RhZ3JhbS5jb21xN2gSiGgTiGgUaANoFYhoFohoF0rrnM5daBiJaBlOaBpOaBuJ\naBx9cThYCAAAAEh0dHBPbmx5cTlOc3ViWAUAAABzaGJ0c3E6aAYpgXE7fXE8KGgJSwBoCmg6aAxY\nEgAAADE1NzMyMTY4NzQuOTgyNzQzNXE9aA5OaA+JaBBYDgAAAC5pbnN0YWdyYW0uY29tcT5oEoho\nE4hoFGgDaBWIaBaIaBdK65zOXWgYiWgZTmgaTmgbiWgcfXE/WAgAAABIdHRwT25seXFATnN1YlgK\nAAAAZHNfdXNlcl9pZHFBaAYpgXFCfXFDKGgJSwBoCmhBaAxYCgAAADkxOTI1MTMwNTVxRGgOTmgP\niWgQWA4AAAAuaW5zdGFncmFtLmNvbXFFaBKIaBOIaBRoA2gViGgWiGgXSmsJPF5oGIloGU5oGk5o\nG4loHH1xRnViWAYAAAB1cmxnZW5xR2gGKYFxSH1xSShoCUsAaApoR2gMWEAAAAAie1wiMTA5LjI0\nNS4zOC4xNzdcIjogMTU5NTh9OjFpVDNaaToyS3o4ZWVHRDFMNlpUbU9kS0M3aWVkZUlET2cicUpo\nDk5oD4loEFgOAAAALmluc3RhZ3JhbS5jb21xS2gSiGgTiGgUaANoFYhoFohoF05oGIhoGU5oGk5o\nG4loHH1xTFgIAAAASHR0cE9ubHlxTU5zdWJYCQAAAHNlc3Npb25pZHFOaAYpgXFPfXFQKGgJSwBo\nCmhOaAxYIAAAADkxOTI1MTMwNTUlM0FWU1B3dmxsY29hSWFDVCUzQTI4cVFoDk5oD4loEFgOAAAA\nLmluc3RhZ3JhbS5jb21xUmgSiGgTiGgUaANoFYhoFohoF0rrlaZfaBiJaBlOaBpOaBuJaBx9cVNY\nCAAAAEh0dHBPbmx5cVROc3VidXNzLg==\n"}, "created_ts": 1573216875}'
elif USERNAME == "joshua_john655":
    COOKIES_SELENIUM = [{'domain': '.instagram.com', 'httpOnly': True, 'name': 'sessionid', 'path': '/', 'secure': True, 'value': '19552869068%3AFA1nVZyudjkz80%3A10'}, {'domain': '.instagram.com', 'httpOnly': True, 'name': 'shbts', 'path': '/', 'secure': True, 'value': '1575044465.4502423'}, {'domain': '.instagram.com', 'httpOnly': True, 'name': 'rur', 'path': '/', 'secure': True, 'value': 'PRN'}, {'domain': '.instagram.com', 'httpOnly': True, 'name': 'shbid', 'path': '/', 'secure': True, 'value': '10017'}, {'domain': '.instagram.com', 'httpOnly': False, 'name': 'csrftoken', 'path': '/', 'secure': True, 'value': 'DBiMxqTZfuoMzCYDKPRkIVluOq2uASah'}, {'domain': '.instagram.com', 'httpOnly': False, 'name': 'mid', 'path': '/', 'secure': True, 'value': 'XeFFZgAAAAHbZyjqTtVmOHiM_dDY'}, {'domain': '.instagram.com', 'httpOnly': False, 'name': 'ds_user_id', 'path': '/', 'secure': True, 'value': '19552869068'}, {'domain': '.instagram.com', 'httpOnly': True, 'name': 'ig_did', 'path': '/', 'secure': True, 'value': '489735BD-DADE-4A38-845F-477970704763'}, {'domain': '.instagram.com', 'httpOnly': True, 'name': 'urlgen', 'path': '/', 'secure': True, 'value': '"{/"2a02:8388:180:4600:7501:a907:b4af:9e40/": 6830}:1iaj15:wl2eUxn-LF5yCra5RCru6SlsB1o"'}, {'domain': 'www.instagram.com', 'httpOnly': False, 'name': 'ig_cb', 'path': '/', 'secure': False, 'value': '1'}]
    COOKIE = {"uuid": "5b6b7c36-0228-11ea-9c82-54e1ad37e19a", "device_id": "android-5b6b7c37022811ea", "ad_id": "7f9c78ff-654a-57e8-a64c-ee5747387aa3", "session_id": "5b6b7c38-0228-11ea-b945-54e1ad37e19a", "cookie": {"__class__": "bytes", "__value__": "gAN9cQBYDgAAAC5pbnN0YWdyYW0uY29tcQF9cQJYAQAAAC9xA31xBChYCQAAAGNzcmZ0b2tlbnEF\nY2h0dHAuY29va2llamFyCkNvb2tpZQpxBimBcQd9cQgoWAcAAAB2ZXJzaW9ucQlLAFgEAAAAbmFt\nZXEKWAkAAABjc3JmdG9rZW5xC1gFAAAAdmFsdWVxDFggAAAAT2ZZb1BRN3ZMQXpWcXBjSlFGSkx0\nR0o0NzBkTEl0bXFxDVgEAAAAcG9ydHEOTlgOAAAAcG9ydF9zcGVjaWZpZWRxD4lYBgAAAGRvbWFp\nbnEQWA4AAAAuaW5zdGFncmFtLmNvbXERWBAAAABkb21haW5fc3BlY2lmaWVkcRKIWBIAAABkb21h\naW5faW5pdGlhbF9kb3RxE4hYBAAAAHBhdGhxFGgDWA4AAABwYXRoX3NwZWNpZmllZHEViFgGAAAA\nc2VjdXJlcRaIWAcAAABleHBpcmVzcRdK+EmlX1gHAAAAZGlzY2FyZHEYiVgHAAAAY29tbWVudHEZ\nTlgLAAAAY29tbWVudF91cmxxGk5YBwAAAHJmYzIxMDlxG4lYBQAAAF9yZXN0cRx9cR11YlgDAAAA\ncnVycR5oBimBcR99cSAoaAlLAGgKWAMAAABydXJxIWgMWAMAAABQUk5xImgOTmgPiWgQWA4AAAAu\naW5zdGFncmFtLmNvbXEjaBKIaBOIaBRoA2gViGgWiGgXTmgYiGgZTmgaTmgbiWgcfXEkWAgAAABI\ndHRwT25seXElTnN1YlgDAAAAbWlkcSZoBimBcSd9cSgoaAlLAGgKaCZoDFgcAAAAWGNWbjlnQUJB\nQUZCdmNCNUxyX3hCMHpQSUxtdnEpaA5OaA+JaBBYDgAAAC5pbnN0YWdyYW0uY29tcSpoEohoE4ho\nFGgDaBWIaBaIaBdK9mqRcGgYiWgZTmgaTmgbiWgcfXErdWJYBwAAAGRzX3VzZXJxLGgGKYFxLX1x\nLihoCUsAaApoLGgMWA4AAABqb3NodWFfam9objY1NXEvaA5OaA+JaBBYDgAAAC5pbnN0YWdyYW0u\nY29tcTBoEohoE4hoFGgDaBWIaBaIaBdK+A48XmgYiWgZTmgaTmgbiWgcfXExWAgAAABIdHRwT25s\neXEyTnN1YlgFAAAAc2hiaWRxM2gGKYFxNH1xNShoCUsAaApoM2gMWAUAAAAxMDAxN3E2aA5OaA+J\naBBYDgAAAC5pbnN0YWdyYW0uY29tcTdoEohoE4hoFGgDaBWIaBaIaBdKeKLOXWgYiWgZTmgaTmgb\niWgcfXE4WAgAAABIdHRwT25seXE5TnN1YlgFAAAAc2hidHNxOmgGKYFxO31xPChoCUsAaApoOmgM\nWBEAAAAxNTczMjE4Mjk1Ljc0NDQ3OXE9aA5OaA+JaBBYDgAAAC5pbnN0YWdyYW0uY29tcT5oEoho\nE4hoFGgDaBWIaBaIaBdKeKLOXWgYiWgZTmgaTmgbiWgcfXE/WAgAAABIdHRwT25seXFATnN1YlgK\nAAAAZHNfdXNlcl9pZHFBaAYpgXFCfXFDKGgJSwBoCmhBaAxYCwAAADE5NTUyODY5MDY4cURoDk5o\nD4loEFgOAAAALmluc3RhZ3JhbS5jb21xRWgSiGgTiGgUaANoFYhoFohoF0r4DjxeaBiJaBlOaBpO\naBuJaBx9cUZ1YlgJAAAAc2Vzc2lvbmlkcUdoBimBcUh9cUkoaAlLAGgKaEdoDFggAAAAMTk1NTI4\nNjkwNjglM0FnRWkzazl0V1A4VUc5QyUzQTdxSmgOTmgPiWgQWA4AAAAuaW5zdGFncmFtLmNvbXFL\naBKIaBOIaBRoA2gViGgWiGgXSnibpl9oGIloGU5oGk5oG4loHH1xTFgIAAAASHR0cE9ubHlxTU5z\ndWJ1c3Mu\n"}, "created_ts": 1573218296}
else:
    print("unknown username")
    exit()

INSTA_LOGIN_URL = "https://www.instagram.com/accounts/login/"

INSTA_FEED_URL = "https://www.instagram.com/"

USER_AGENT = "Mozilla/5.0 (Linux; Android 8.1; EML-L29 Build/HUAWEIEML-L29; xx-xx) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36"

ROOT_IMAGE_STORAGE = Path(Path.cwd()/"root_images")

IMAGE_QUARANTINE = ROOT_IMAGE_STORAGE / "quarantine"

IMAGE_STORAGE = ROOT_IMAGE_STORAGE / "future_images"

SUBMISSION_STORAGE = ROOT_IMAGE_STORAGE / "submissions"

REDFLAG_KEYWORDS = ["giveaway", "free", "check", "you", "follow", "me", "best", "mouse", "mousepad", "keyboard", "pc", "computer", "laptop", "only", "money", "get", "%"]

RESUPPLY_TRESHOLD = 10 #threshold for resupplying

_platf = platform.system()
if _platf=="Linux":
    CHROMEDRIVER_PATH = Path("/usr/lib/chromium-browser/chromedriver")
elif _platf=="Windows":
    CHROMEDRIVER_PATH = Path("D:/Programiranje/Python_projects/bots/pc_setup_ideas-final/selenium_scripts/chromedriver.exe")
else:
    print(f"{_platf} is not a suported OS")

MENU = '''
********************************************************
*``````````INSTAGRAM`PC_SETUP_IDEAS`BOT````````````````*
*``````````````````````````````````````````````````````*
*``````````````````````````````````````````````````````*
*``````````````````````````````````````````````````````*
*``@pc_setup_ideas`````````````````````````````````````*
*``Version:4.0``````````Bogdan`Caleta`Ivkovic`(c)`2018`*
********************************************************
Posted:{allPosts}

Up-time: {upTime} hrs

Time of the last post: {lastPost}
Next post at: {nextPost}
'''

#ostavicu ovo ovde kao spomenik na sopstvenu glupost i razlog zasto treba citati dokumentaciju
#POST_SHELL_CODE = 'instapy -u {} -p {} -f "{}/'+IMAGE_STORAGE+'/{}/{}" -t "{} @pc_setup_ideas | tags:{} post from {}"'

MIN_WAIT = 21000.0

MAX_WAIT = 22200.0

EMAIL  = "pc.setup.ideas@gmail.com"

IMAP_URL = "imap.gmail.com"
