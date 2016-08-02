# coding: utf-8

import random

file_manager = open('username.txt', 'w')

def building_users(name, password):
    file_manager.write((name + ',' + password + '\n').encode('utf-8'))

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

