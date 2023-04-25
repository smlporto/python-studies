from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\chromedriver\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

chrome_options = webdriver.ChromeOptions()
#keep the browser open
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Teste")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Email")

email = driver.find_element(By.NAME, "email")
email.send_keys("testeemail@gmail.com")

email.send_keys(Keys.ENTER)


