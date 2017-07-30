import requests
from bs4 import BeautifulSoup


class V2ex():
    login_url = 'https://www.v2ex.com/signin'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        session = requests.Session()
        session.headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
            'referer': V2ex.login_url
        }
        self.session = session

    def get_key(self):
        response = self.session.get(V2ex.login_url)

        soup = BeautifulSoup(response.text, 'html.parser')
        userkey = soup.find(
            'input', attrs={'type': 'text', 'class': 'sl'})['name']
        passkey = soup.find(
            'input', attrs={'type': 'password', 'class': 'sl'})['name']
        once = soup.find('input', attrs={'type': 'hidden', 'name': 'once'})[
            'value']
        return userkey, passkey, once

    def get_balance(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        silver, copper = soup.find(class_='fr', id='money').get_text().split()
        return silver, copper

    def login(self):
        userkey, passkey, once = self.get_key()

        data = {
            userkey: self.username,
            passkey: self.password,
            'once': once,
            'next': '/'
        }
        response = self.session.post(V2ex.login_url, data=data)
        silver, copper = self.get_balance(response.text)
        print(f'登录成功\n\n你的银币数为: {silver}\n你的铜币数为: {copper}')


# 输入用户名及密码
username = ''
password = ''
v = V2ex(username, password)
v.login()
