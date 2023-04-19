#!/usr/bin/python3
"""
script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
 with the letter as a parameter
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 2:
        q = {'q': sys.argv[1]}
    else:
        q = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', q)
    if r.json() == {}:
        print('No result')
    else:
        r = r.json()
        print('[{}] {}'.format(r.get('id'), r.get('name')))
