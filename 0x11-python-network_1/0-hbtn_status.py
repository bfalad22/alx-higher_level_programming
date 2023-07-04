#!/usr/bin/python3
"""Fetch
https://intranet.hbtn.io/status
using urllib package
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')

print(f'- type: {type(body)}')
print(f'- content: {body}')
