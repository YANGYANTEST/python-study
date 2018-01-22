"""
处理 iframe 和 alert 窗口
"""

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver =  webdriver.Chrome(executable_path="./chromedriver.exe")

# driver.get("https://login.anjuke.com/login/form")

# driver.switch_to_frame('iframeLoginIfm')

# driver.find_element_by_id('phoneIpt').send_keys('13455556666')
# driver.find_element_by_id('smsIpt').send_keys('1234')

driver.get('file:///D:/tranning/04/python-study/2018-01/alert.html')

driver.find_element_by_tag_name('button').click()

Alert(driver).accept()