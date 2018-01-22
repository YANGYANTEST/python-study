
driver =  webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("http://www.baidu.com")

searchInput = driver.find_element_by_id('kw')

searchInput.send_keys("helloworld")

driver.quit()