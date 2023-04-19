#!/usr/bin/python3
"""
xx
"""

if __name__ == '__main__':
    import sys
    import requests

    name = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(name, owner)
    r = requests.get(url)
    r = r.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                r[i].get('sha'),
                r[i].get('commit').get('author').get('name'))
                )
    except IndexError:
        pass
