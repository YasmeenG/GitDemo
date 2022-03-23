from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(by=By.LINK_TEXT, value="Click Here").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
text = driver.find_element(by=By.CSS_SELECTOR, value="div[class='example'] h3").text
assert "New Window" == text

driver.close()
driver.switch_to.window(driver.window_handles[0])

text1 = driver.find_element(by=By.TAG_NAME, value="h3").text
assert "Opening a new window" == text1



