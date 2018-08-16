import time
from selenium import webdriver
from pprint import pprint


def login(name, passwd):
    url = 'https://pan.baidu.com/'

    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    driver.maximize_window()
    driver.get(url)
    print('开始登录')

    time.sleep(5)

    chg_field = driver.find_element_by_id('TANGRAM__PSP_4__footerULoginBtn')
    chg_field.click()

    name_field = driver.find_element_by_id('TANGRAM__PSP_4__userName')
    name_field.send_keys(name)
    passwd_field = driver.find_element_by_id('TANGRAM__PSP_4__password')
    passwd_field.send_keys(passwd)
    login_button = driver.find_element_by_id('TANGRAM__PSP_4__submit')
    login_button.click()
    time.sleep(20)
    return driver.get_cookies()


if __name__ == '__main__':
    login_name = input('请输入你的登录账号:\n')
    login_passwd = input('请输入你的登录密码:\n')
    cookies = login(login_name, login_passwd)

    pprint(cookies)
