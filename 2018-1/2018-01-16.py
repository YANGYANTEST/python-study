"""
selenium 定位元素
"""
# find_element_by_id
from selenium import webdriver

driver =  webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("http://www.baidu.com")

# driver.find_element_by_id('kw').send_keys("hello world")
# driver.find_element_by_name('wd').send_keys('1234')
# driver.find_element_by_xpath('//*[@id="u1"]/a[1]').click()

# driver.find_element_by_link_text('地图').click()
# driver.find_element_by_partial_link_text('图').click()
# driver.find_element_by_class_name('s_ipt').send_keys("abc")
driver.find_element_by_css_selector('#kw').send_keys('bcd')