#!/usr/bin/python3
"""Fetch
https://intranet.hbtn.io/status
using urlib package
"""

import urlib.request

if  __name__ == '__main__':
    with urlib.request.urlopen('https://intranet.hbtn.io/status') as request:
        response = request.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('UTF-8')))
