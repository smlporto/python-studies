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
        self.down = float(down_speed)
        self.up = float(up_speed)
    
    def tweet_at_provider(self):
        if self.down < PROMISED_DOWNLOAD or self.up < PROMISED_UPLOAD:
            self.driver.get("https://www.twitter.com")
            time.sleep(2)
            sign_in_button = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a/div/span/span')
            sign_in_button.click()
            time.sleep(3)
            
            username_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            username_input.send_keys(TWITTER_USERNAME)
            
            next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
            next_button.click()
            time.sleep(2)
            
            password_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_input.send_keys(TWITTER_PASSWORD)
            
            log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
            log_in_button.click()
            time.sleep(5)
            
            tweet_input = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
            tweet_input.send_keys(f"Why my internet is {self.down}/{self.up} Mb/s if I am paying for {PROMISED_DOWNLOAD}/{PROMISED_UPLOAD} Mb/s??")
            
            tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
            tweet_button.click()
            time.sleep(5)
            
            self.driver.quit() 
        
        else:
            print("Everything is OK!")
            self.driver.quit()
        

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()