#!/usr/bin/python3
"""
sends a request to the URL and displays
the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import URLError, HTTPError

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            r = res.read()
            print(r.decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
    except URLError as e:
        print('Error code:', e.code)
