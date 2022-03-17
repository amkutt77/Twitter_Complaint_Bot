from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class speedTest():

    def __init__(self):
        self.chrome_driver_path = "PATH TO CHROME DRIVER"
        self.ser = Service(executable_path=self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.ser)
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")

    def click_speed_test(self):
        # click the speed test button
        try:
            element_present = EC.element_to_be_clickable((By.CSS_SELECTOR, "span.start-text"))
            WebDriverWait(self.driver, 20).until(element_present)
            print("speed test button found!")
        except TimeoutException:
            print("Can't find speed test button.")
            return False

        go_button = self.driver.find_element(by = By.CSS_SELECTOR, value="span.start-text")
        go_button.click()
        return True


    def get_speed_data(self):

        # once go button is clicked, it will take some time for the speed test to run. Once it finishes running, there should be a result id.
        # once that result id is present, then we should go and try to scrape the speed data
        try:
            element_present = EC.visibility_of_element_located((By.CSS_SELECTOR, "div.result-data [href *= '/result/']")) # this is to locate the result id, it's a link.
            WebDriverWait(self.driver, 60).until(element_present)
            print("speed data is ready!")
        except TimeoutException:
            print("loading took too much time. No speed data available")
            return False
        

        # get the download and upload speed
        download_speed = self.driver.find_element(by = By.CSS_SELECTOR, value="span.result-data-large.number.result-data-value.download-speed").text
        upload_speed = self.driver.find_element(by = By.CSS_SELECTOR, value = "span.result-data-large.number.result-data-value.upload-speed").text
        speed_data = {
            "download_speed": float(download_speed),
            "upload_speed": float(upload_speed)
        }
        self.driver.quit() # close out speed test window
        return speed_data



