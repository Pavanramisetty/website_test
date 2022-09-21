from selenium import webdriver
import selenium
import chromedriver_binary


class BaseConfig:
    browser = webdriver.Chrome(executable_path=r"C:\\Users\\Lithik\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome()

    def __init__(self, url=None, uname=None, password=None):
        self.url = url
        self.uname = uname
        self.password = password

    def login(self):
        driver.get("www.python.org")


if "__name__" == __main__:
    site = BaseConfig()
    site.login()
