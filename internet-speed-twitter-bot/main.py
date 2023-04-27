from config import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
        self.up = 0
        self.down = 0
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
    
    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()