#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
using urllib backage
"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        r = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(r)))
        print('\t- content: {}'.format(r))
        print('\t- utf8 content: {}'.format(r.decode('utf-8')))
