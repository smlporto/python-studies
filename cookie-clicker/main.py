from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "D:\chromedriver\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

chrome_options = webdriver.ChromeOptions()
#keep the browser open
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

i = 100
timeout = 300
timeout_start = time.time()

cookie = driver.find_element(By.ID, "cookie")

improvements = driver.find_elements(By.CSS_SELECTOR, "#store div")
improvements_id = [improvement.get_attribute("id") for improvement in improvements]

while time.time() < timeout_start + timeout:
    
    for _ in range(i):
        cookie.click()
        
    for improvement in improvements_id[::-1]:
        try:
            driver.find_element(By.ID, improvement).click()
        except:
            continue
    
    i +=50

cookie_per_second = driver.find_element(By.ID, "cps")
print(cookie_per_second.text)

driver.close()