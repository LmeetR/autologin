import time
from selenium import webdriver


def login():
    # input 是系统内置的函数，从控制台输入账号密码
    acount_num = input('请输入账号:\n')
    passwd_str = input('请输入密码:\n')

    #
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    url = 'http://mail.163.com/'
    driver.get(url)
    time.sleep(5)

    # 163登陆框是使用iframe进行嵌套的，所以需要先切换到该iframe
    driver.switch_to.frame('x-URS-iframe')

    # 找到 input标签
    acount = driver.find_element_by_name('email')
    acount.clear()
    # 模拟输入一个 账户信息
    acount.send_keys(acount_num)

    passwd = driver.find_element_by_name('password')
    passwd.clear()
    passwd.send_keys(passwd_str)

    time.sleep(3)

    # 找到登录按钮
    click_button = driver.find_element_by_id('dologin')

    # 触发点击
    click_button.click()
    time.sleep(5)

    cur_cookies = driver.get_cookies()[0]
    return cur_cookies


if __name__ == '__main__':
    _cookies = login()

    print(_cookies)
