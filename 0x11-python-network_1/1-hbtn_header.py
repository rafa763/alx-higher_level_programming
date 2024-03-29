#!/usr/bin/python3
"""
sends a request to the URL and displays
the value of the X-Request-Id variable found
in the header
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as res:
        r = dict(res.info())
        print(r.get('X-Request-Id'))
