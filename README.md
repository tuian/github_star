# github_star

运行这个脚本可以让你的github中star变得更多, 这个脚本主要是给大家提供一个思路, 建议大家学习一下就好, 小心运行, 小心github帐号被封掉, 得不偿失

这里一共有下面几个需要执行的文件

build_user.py
github_join.py
github_star.py


使用这个脚本的方式如下:

1. 执行 build_user.py, 生成 username.txt 文件, 这里保存了github的帐号和密码, 为了接下来的操作做准备
2. 执行 github_join.py, 这个文件是为了注册刚刚生成的username.txt文件中的那些用户
3. 执行 github_star.py, 这个文件就是最后的操作, 给你的项目添加star

如果想要对生成的账户的用户名和生成账户的多少做修改, 直接修改build_user.py中的 usernumber及 username_suffix这两个变量即可, build_user.py源码如下:

```
if __name__ == '__main__':
    usernames = ['Pittman', 'Skinner', 'Slater', 'Slaughter', 'Sloan', 'Aalto', 'Aaron', 'Ab', 'Abadam', 'Abbas', 'Baade', 'Baal', 'Babbage', 'Gabriel', 'Gaines', 'Galen', 'Nadine']

    # 人数
    usernumber = 5
    # 人名的后缀长度
    username_suffix = 6

    for i in xrange(0, usernumber):
        name = usernames[random.randint(0, len(usernames) - 1)]
        for k in xrange(0, username_suffix):
            name = name + str(random.randint(0, 9))
        password = name
        building_users(name, password)
```

最后给你的项目star需要改动的代码在github_star.py的最底部, 源码如下:

```
# param username: 你的用户名
# param repository_name: 你的项目仓库名
# param num: 你想要的star数量

if __name__ == '__main__':
    run_star('slipawayleaon', 'iOS-JSHeaderView', 3)
    run_star('slipawayleaon', 'PSRefresh', 5)
    run_star('slipawayleaon', 'iOS-HeaderZoom--', 2)
```
