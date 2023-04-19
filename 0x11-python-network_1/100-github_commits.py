#!/usr/bin/python3
"""
xx
"""

if __name__ == '__main__':
    import sys
    import requests

    name = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, name)
    r = requests.get(url).json()

    for c in r[0:10]:
            print('{}: {}'.format(
                c['sha'],
                c['commit']['author']['date'])
                )
