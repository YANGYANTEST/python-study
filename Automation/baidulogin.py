from selenium import webdriver
import time

driver = webdriver.Chrome()
# 导航到百度
url ="https://www.baidu.com"
driver.get(url)

# 点击登录 按钮
loginXpath = '//*[@id="u1"]/a[7]'
loginlink = driver.find_element_by_xpath(loginXpath)
loginlink.click()


time.sleep(6)

# 点击用户名登录
usernameXpath = '//*[@id="TANGRAM__PSP_10__footerULoginBtn"]'
usernamelink = driver.find_element_by_xpath(usernameXpath)
usernamelink.click()

# 输入用户名 和密码
phoneXpath='//*[@id="TANGRAM__PSP_10__userName"]'
passwdXpath='//*[@id="TANGRAM__PSP_10__password"]'

phoneinput = driver.find_element_by_xpath(phoneXpath)
passwdInput = driver.find_element_by_xpath(passwdXpath)

phoneinput.send_keys('13500001111')
passwdInput.send_keys('xxxxxx')


# 点击登录按钮

loginBtnXpath = '//*[@id="TANGRAM__PSP_10__submit"]'
loginBtn = driver.find_element_by_xpath(loginBtnXpath)
loginBtn.click()