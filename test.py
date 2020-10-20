from __future__ import print_function

import pprint
import tunet


if __name__ == '__main__':
    username = input("Username:")
    password = input("Password:")
    pprint.pprint(tunet.auth4.checklogin())
    pprint.pprint(tunet.auth4.login(username, password))
    pprint.pprint(tunet.net.checklogin())
