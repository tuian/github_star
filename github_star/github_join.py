# coding: utf-8

# 这里是从chrome上抓的注册时的post数据

# utf8:✓
# authenticity_token:OUXAc3ILb6RoAyAMW9NLL1o+8ge5+rFUEeYmbeWZicIDYpVJCbjz+SyLRUq/D5xiAFUU7YXc77NBtakBdom5zw==
# user[login]:jfkfjf
# user[email]:18811130435@qq.com
# user[password]:Leaon9306
# source:form-home

import urllib2, urllib, re
import time

class github_join:

    def __init__(self):
        cookies = urllib2.HTTPCookieProcessor()
        print cookies
        self.opener = urllib2.build_opener(cookies)
        # 请求头
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'), ('Origin', 'https://github.com'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'), ('Accept-Language','zh-CN,zh;q=0.8'), ('Connection', 'keep-alive')]
        # 获取 token
        self.re_auth = re.compile('authenticity_token[^>]+')

    # 注册
    def get_github_join_token(self):
        response = self.opener.open('https://github.com/join')
        html = response.read()
        print u'正在登录join'
        print u'状态码为', response.getcode()
        token = self.re_auth.findall(html)[0][41:-3]
        return token

    def register(self, token, loginname, email, password):
        print 'token:', token
        print 'loginname:', loginname
        print 'email:', email
        print 'password:', password

        # 'source': 'form-join'
        self.formdata = {'utf-8': '✓',
                        'authenticity_token': token, 
                        'user[login]': loginname, 
                        'user[email]': email, 
                        'user[password]': password, 
                        'source': 'form-home'} 
        # print u'formdata:', self.formdata
        data_encoded = urllib.urlencode(self.formdata)
        # print u'data_encoded:', data_encoded
        response = self.opener.open('https://github.com/join', data_encoded)

        print u'正在注册'
        print u'状态码为', response.getcode(), u'转到', response.geturl()

    # 登出
    def get_github_logout_token(self):
        response = self.opener.open('https://github.com/')
        html = response.read()
        token = self.re_auth.findall(html)[0][41:-3]
        return token

    def logout(self, token):
        self.formdata = {'utf-8': '✓', 'authenticity_token': token}
        data_encoded = urllib.urlencode(self.formdata)
        response = self.opener.open('https://github.com/logout', data_encoded)
        print u'正在登出'
        print u'状态码为', response.getcode(), u'转到', response.geturl()


if __name__ == '__main__':
    file_manager = open('username.txt', 'r')
    github_join_manager = github_join()

    for userinfo in file_manager.readlines():

        userinfo_array = userinfo.split(',')

        name = userinfo_array[0]
        password = userinfo_array[1].strip('\n')
        email = name + '@qq.com'

        try:
            signin_token = github_join_manager.get_github_join_token()
            github_join_manager.register(signin_token, name, email, password)
            logout_token = github_join_manager.get_github_logout_token()
            github_join_manager.logout(logout_token)
        except Exception, e:
            print u'注册失败'
        print '*************'
        print '*************'
        time.sleep(1)

    file_manager.close()


