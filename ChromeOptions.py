from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("/usr/local/bin/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certification-errors")

driver = webdriver.Chrome(service=ser,options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)

