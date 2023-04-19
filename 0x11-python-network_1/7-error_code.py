#!/usr/bin/python3
"""
sends a request to the URL and displays
the status code if >= 400 else displays
the body
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)
