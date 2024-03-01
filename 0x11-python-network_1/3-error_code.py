#!/usr/bin/python3
""" 3-error_code: takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8) """
import sys
from urllib.request import Request, urlopen
from urllib.error import URLError

if __name__ == '__main__':
    url = sys.argv[1]
    request = Request(url)
    try:
        with urlopen(request) as response:
            print(response.read().decode())
    except URLError as http_error:
        print(f'Error code: {http_error.code}')
