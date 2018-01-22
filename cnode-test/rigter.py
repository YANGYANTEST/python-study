'''
CNode url= http://118.31.19.120:3000/
注册邮件不会发
远程链接到数据库改数据
作业要求：1、测试用例，用代码注释的方法；2、至少用三个测试用例 3、加分：把测试用例放到csv或者excel 文件里读取
备注：读取csv文件中的测试用例信息的相关代码在 “2018-01-18.py 文件”
'''

#版本code v0.0.1
from selenium import webdriver
import time

test_data=[
    ['xiaoming','123456','123456','xm@1234.com'],
    ['','123456','123456','xm@1234.com'],
    ['xiaoming','','123456','xm@1234.com'],
    ['xiaoming','123456','','xm@1234.com']
]

drvier = webdriver.Chrome()

def regitser(username,passwd,repasswd,email):

    # 打开Node注册页面
    drvier.get("http://118.31.19.120:3000/")
    # 注册 register
    registerXpath = "/html/body/div[1]/div/div/ul/li[5]/a"
    registerLink = drvier.find_element_by_xpath(registerXpath)
    registerLink.click()

    # 输入用户名
    usermaneinput = "loginname"
    username_input_area = drvier.find_element_by_id(usermaneinput)
    username_input_area.send_keys(username)

    # 输入密码
    pwdinput = "pass"
    pwd = drvier.find_element_by_id(pwdinput)
    pwd.send_keys(passwd)

    # 输入确认密码
    repwdinput = "re_pass"
    repwd = drvier.find_element_by_id(repwdinput)
    repwd.send_keys(repasswd)

    # 输入邮箱地址
    emailinput = "email"
    email_area = drvier.find_element_by_id(emailinput)
    email_area.send_keys(email)

    # 点击注册按钮
    registerBot = "span-primary"
    rigerterbtn = drvier.find_element_by_class_name("span-primary")
    rigerterbtn.click()

    # time.sleep(6)

    # tipmsg = drvier.find_element_by_class_name('alert alert-error').text()

    # print(tipmsg)


for x in range(len(test_data)):
    regitser(test_data[x][0],test_data[x][1],test_data[x][2],test_data[x][3])


drvier.quit()
