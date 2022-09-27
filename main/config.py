from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def login(site, uname=None, password=None, self=None):
    if site is not None:
        browser = webdriver.Firefox()
    try:
        browser.get(site)
        ulogin = browser.find_element(By.ID, "email")
        pwd = browser.find_element(By.ID, "pass")
        ulogin.send_keys(uname)
        pwd.send_keys(password)
        time.sleep(60)
        browser.find_element(By.NAME, "login").click()
    except Exception as e:
        print(e.args)
    finally:
        time.sleep(5)
        browser.quit()



url = "https://www.fcebook.com"
login(url)
