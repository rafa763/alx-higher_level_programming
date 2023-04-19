#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys

    name = sys.argv[1]
    token = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(name, token))
    print(r.json().get('id'))
