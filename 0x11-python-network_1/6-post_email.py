#!/usr/bin/python3
"""
script that takes in a URL and an email, sends
a POST request to the passed URL with the email as
a parameter, and displays the body of the response
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    r = requests.post(url, email)
    print(r.text)
