from selenium import webdriver
import chromedriver_binary





class BaseConfig:
    # browser = webdriver.Chrome(executable_path=r"C:\\Users\\Lithik\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # driver = webdriver.Chrome()

    def __init__(self, driver=None):
        if driver != None:
            self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get()


url = "https://www.fcebook.com"
BaseConfig.login(url)


'''from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("you@email.com")
password.send_keys("yourpassword")
# Step 4) Click Login
submit.click()'''