from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

alertVariable = "Option5"
ser = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=ser)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(by=By.ID, value="name").send_keys(alertVariable)
driver.find_element(by=By.ID, value="alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert alertVariable in alertText
alert.accept()
#alert.dismiss()


