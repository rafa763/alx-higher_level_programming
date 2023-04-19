#!/usr/bin/python3
"""
script that takes in a URL and an email, sends
a POST request to the passed URL with the email as
a parameter, and displays the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        r = res.read()
        print(r.decode('utf-8'))
