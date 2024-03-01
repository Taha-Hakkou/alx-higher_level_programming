#!/usr/bin/python3
""" 1-hbtn_header: takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response """
import sys
from urllib.request import Request, urlopen


if __name__ == '__main__':
    url = sys.argv[1]
    request = Request(url)
    with urlopen(request) as response:
        print(response.headers.get('X-Request-Id'))
