


import os
import csv
import time
from selenium import webdriver




driver=webdriver.Chrome()
driver.get("http://118.31.19.120:3000")
driver.find_element_by_link_text('注册').click()
time.sleep(3)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="loginname"]').send_Keys(content[1])


with open('nodejs.csv',newline='') as csvfile:#此方法:当文件不用时会自动关闭文件
  csvReader = csv.reader(csvfile)
  for content in csvReader:
    # print(content)
    
