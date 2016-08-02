# coding: utf-8

import urllib2, urllib, re
import time

class github_star:

    def __init__(self):
        cookies = urllib2.HTTPCookieProcessor()
        print cookies
        self.opener = urllib2.build_opener(cookies)
        # 请求头
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'), ('Origin', 'https://github.com'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'), ('Accept-Language','zh-CN,zh;q=0.8'), ('Connection', 'keep-alive')]
        # 获取 token
        self.re_auth = re.compile('authenticity_token[^>]+')

    # 登入登出
    def get_github_login_token(self):
        response = self.opener.open('https://github.com/login/')
        html = response.read()
        token = self.re_auth.findall(html)[0][41:-3]
        return token

    def login(self, token, username, password):
        self.formdata = {'commit': 'Sign in', 'utf-8': '✓', 'authenticity_token': token, 'login': username, 'password': password}
        data_encoded = urllib.urlencode(self.formdata)
        response = self.opener.open('https://github.com/session', data_encoded)
        print u'正在登录', username

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

    # star
    def star(self, username, repository_name):
        url = 'https://github.com/' + username + '/' + repository_name + '/'
        print url
        response = self.opener.open(url)
        html = response.read()
        # print html
        # token = self.re_auth.findall(html)[3][41:-3]
        token = self.re_auth.findall(html)[2][41:-3]
        print 'token', token
        formdata = {'utf-8': '✓', 'authenticity_token': token}
        data_encoded = urllib.urlencode(formdata)
        response = self.opener.open(url + 'star', data_encoded)
        print u'状态码为', response.getcode(), u'转到', response.geturl()

def run_star(username, repository_name, num):
    file_manager = open('username.txt', 'r')
    github_star_manager = github_star()

    if num > file_manager.readlines():
        num = file_manager.readlines()
    elif num <= 0:
        print r'num can\'t less than 0'
        return

    i = 0
    for userinfo in file_manager.readlines():
        i ++
        userinfo_array = userinfo.split(',')

        name = userinfo_array[0]
        password = userinfo_array[1].strip('\n')

        try:
            login_token = github_star_manager.get_github_login_token()
            github_star_manager.login(login_token, name, password)
            github_star_manager.star(username, repository_name)
            logout_token = github_star_manager.get_github_logout_token()
            github_star_manager.logout(logout_token)
        except Exception, e:
            print u'star 失败 reason:', e
        print '**************'
        print '**************'
        time.sleep(1)
        if i == num:
            break
    file_manager.close()


if __name__ == '__main__':
    run_star('slipawayleaon', 'iOS-JSHeaderView', 3)
    run_star('slipawayleaon', 'PSRefresh', 5)
    run_star('slipawayleaon', 'iOS-HeaderZoom--', 2)


