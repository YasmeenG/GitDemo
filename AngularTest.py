from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=ser)

driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.find_element(by=By.NAME, value="name").send_keys("Rahul")
driver.find_element(by=By.CSS_SELECTOR, value="input[name='name']").send_keys("Rahul")
driver.find_element(by=By.NAME, value="email").send_keys("yk@gmail.com")

driver.find_element(by=By.ID, value="exampleCheck1").click()

# select class helps to handle dropdown options
# dropdown = Select(driver.find_element(by=By.ID, value="exampleFormControlSelect1"))
# dropdown.select_by_visible_text("Female")
# dropdown.select_by_index(0)

driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
message = driver.find_element(by=By.CLASS_NAME, value="alert-success").text

assert "success" in message
# [class*= 'alert-success'] for partial css selector
# //*contains(@class,’alert-success’)]  for partial xpath selector

