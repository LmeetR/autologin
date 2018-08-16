# tested on ubuntu15.04
import time
from selenium import webdriver
from pprint import pprint


def login(login_url, login_name, login_passwd):
    driver = webdriver.Chrome()
    driver.get(login_url)
    time.sleep(5)

    # 找到这个tab页，模拟点击
    login_tab_right = driver.find_element_by_class_name('login-tab-r')
    login_tab_right.click()

    # 找到login / password
    account = driver.find_element_by_id('loginname')
    password = driver.find_element_by_id('nloginpwd')

    # 找到提交按钮
    submit = driver.find_element_by_id('loginsubmit')

    account.clear()
    password.clear()

    # 发送字符串 到 input 控件中
    account.send_keys(login_name)
    password.send_keys(login_passwd)

    submit.click()
    time.sleep(5)

    jd_cookies = driver.get_cookies()
    driver.close()
    return jd_cookies


if __name__ == '__main__':
    url = 'https://passport.jd.com/new/login.aspx'
    name = input('请输入用户名:\n')
    password = input('请输入密码:\n')
    cookies = login(url, name, password)
    pprint(cookies)
