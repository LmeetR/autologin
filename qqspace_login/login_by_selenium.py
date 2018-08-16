import time
import requests
from selenium import webdriver


def sele2req_cookie(cookies):
    cookie_dict = dict()
    for cookie in cookies:
        cookie_dict[cookie['name']] = cookie['value']
    return cookie_dict


def login(url1, url2):
    login_name = input('请输入QQ号\n')
    login_password = input('请输入QQ密码\n')

    url = url1 + login_name + url2

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    # 默认是用二维码登录的，需要点击切换成账号密码的方式
    login_type = driver.find_element_by_id('switcher_plogin')

    login_type.click()

    # 输入账号和密码
    username = driver.find_element_by_id('u')
    username.clear()
    password = driver.find_element_by_id('p')
    password.clear()
    username.send_keys(login_name)
    password.send_keys(login_password)

    # 点击登录
    submit = driver.find_element_by_id('login_button')
    submit.click()
    time.sleep(5)

    # 得到所有的cookies
    cookies = driver.get_cookies()
    driver.close()
    return cookies


if __name__ == '__main__':
    # 这个地方是通过观察html代码得到的，因为我先前通过find方法定位switch始终提示我没有这个元素，那么我就猜想它肯定是被隐藏或者嵌套在别的
    # frame中了

    # 这里面需要替换一个qq号
    login_url1 = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=http%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=http%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone%26specifyurl%3Dhttp%253A%252F%252Fuser.qzone.qq.com%252F'
    login_url2 = '&pt_qr_app=%E6%89%8B%E6%9C%BAQQ%E7%A9%BA%E9%97%B4&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=http%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'
    }
    cookies = login(login_url1, login_url2)

    # 验证cookie是否正确
    # 如果cookie不是有效的，那么主页应该是无法看到内容的
    myspace = 'http://user.qzone.qq.com/176907518'

    # 把selenium的cookie => dict
    req_cookies = sele2req_cookie(cookies)

    # 请求你自己的主页，加入cookie 和 header
    content = requests.get(myspace, headers=headers, cookies=req_cookies)
    print(content.text)
