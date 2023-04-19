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
    headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer'+token,
            'X-GitHub-Api-Version': '2022-11-28'
            }
    r = requests.get('https://api.github.com/users/'+name, headers)
    print(r.json().get('id'))
