import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://login.anjuke.com/login/form")
time.sleep(10)
driver.switch_to.frame("iframeLoginIfm")
driver.implicitly_wait(5)
driver.find_element_by_id('phoneIpt').send_keys('15221629532')
time.sleep(8)
driver.find_element_by_xpath('//*[@id="smsCheckboxLabel"]/span[1]').click()
driver.find_element_by_id('smsSubmitBtn').click()