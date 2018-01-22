
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
# driver.get("file:///E:/train/python-study/html-bootstrap/2017-12-27.html")
driver.maximize_window()
print("title is ",driver.title)
# assert '百度一下' in driver.title
driver.refresh()
time.sleep(5)
# baidu=driver.find_element_by_tag_name('a')
# baidu.click()
tieba=driver.find_element_by_link_text("贴吧")
tieba.click()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()

