from config import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PROMISED_DOWNLOAD = 200
PROMISED_UPLOAD = 80

CHROME_DRIVER_PATH = "D:\chromedriver\chromedriver.exe"

service = Service(executable_path=CHROME_DRIVER_PATH)

chrome_options = webdriver.ChromeOptions()
#keep the browser open
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")

class InternetSpeedTwitterBot:
    
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.down = 0
        self.up = 0
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        start_button = self.driver.find_element(By.CLASS_NAME, 'start-text')
        time.sleep(3)
        start_button.click()
        time.sleep(40)
        down_speed = self.driver.find_element(By.CLASS_NAME, 'download-speed').text
        up_speed =  self.driver.find_element(By.CLASS_NAME, 'upload-speed').text
        print(down_speed)
        print(up_speed)
    
    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()