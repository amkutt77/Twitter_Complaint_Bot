from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class twitter():

    def __init__(self):
        self.chrome_driver_path = "PATH TO CHROME DRIVER"
        self.ser = Service(executable_path=self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.ser)
        self.driver.maximize_window()
        self.driver.get("https://twitter.com/")
        # twitter login
        self.pw = "XXX"
        self.user2 = "XXX"
        self.user = "XXX"


    def twitter_login_button(self):

        # twitter has different home page login styles...
        try:
            element_present = EC.element_to_be_clickable((By.CSS_SELECTOR, "[href = '/login']"))
            WebDriverWait(self.driver, 5).until(element_present)
            print("twitter login button found!")
        except TimeoutException:
            print("Can't find twitter login button.")
            return False

        try:
            element_present = EC.element_to_be_clickable((By.CSS_SELECTOR, "span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0"))
            WebDriverWait(self.driver, 5).until(element_present)
            print("twitter login button found!")
        except TimeoutException:
            print("Can't find twitter login button.")
            return False

        

        login_button = self.driver.find_element(By.CSS_SELECTOR, value = "[href = '/login']").click()

    def twitter_login_process(self):

        # enter in username
        try:
            element_present = EC.visibility_of_element_located((By.NAME, "text"))
            WebDriverWait(self.driver, 15).until(element_present)
            print("username input found!")
        except TimeoutException:
            print("username input not found.")
            return False

        enter_username = self.driver.find_element(By.NAME, value = "text")
        enter_username.send_keys(self.user)

        # after entering in username, hit the next button
        try:
            element_present = EC.visibility_of_element_located((By.CSS_SELECTOR, "div.css-901oao.r-1awozwy.r-jwli3a"))
            WebDriverWait(self.driver, 5).until(element_present)
            print("next button found!")
        except TimeoutException:
            print("next button not found.")
            return False

        next_button = self.driver.find_element(By.CSS_SELECTOR, value = "div.css-901oao.r-1awozwy.r-jwli3a").click()

        # enter in password
        try:
            element_present = EC.visibility_of_element_located((By.NAME, "password"))
            WebDriverWait(self.driver, 15).until(element_present)
            print("pw input found!")
        except TimeoutException:
            print("pw input not found.")
            return False

        enter_pw = self.driver.find_element(By.NAME, value = "password")
        enter_pw.send_keys(self.pw)

        # hit the login button
        login_button = self.driver.find_element(by = By.CSS_SELECTOR, value = "div.css-901oao.r-1awozwy.r-jwli3a").click()


    def tweet(self,speed_data):
        download_speed = speed_data["download_speed"]
        upload_speed = speed_data["upload_speed"]
        message = f"Hey Internet Provider, why is my internet speed down {download_speed}down/{upload_speed}up when I pay for 150down/10up"

        # type in tweet message
        try:
            element_present = EC.visibility_of_element_located((By.CSS_SELECTOR, "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr"))
            WebDriverWait(self.driver, 15).until(element_present)
            print("tweet input found!")
        except TimeoutException:
            print("tweet input not found.")
            return False

        type_out_tweet = self.driver.find_element(by = By.CSS_SELECTOR, value = "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        type_out_tweet.send_keys(message)
        
        # hit the send tweet button
        try:
            element_present = EC.element_to_be_clickable((By.CSS_SELECTOR, "div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf"))
            WebDriverWait(self.driver, 10).until(element_present)
            print("twitter login button found!")
        except TimeoutException:
            print("Can't find twitter login button.")
            return False

        send_tweet = self.driver.find_element(By.CSS_SELECTOR, value = "div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf").click()
