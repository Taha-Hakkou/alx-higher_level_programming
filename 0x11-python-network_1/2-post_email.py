#!/usr/bin/python3
""" 2-post_email: takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """
import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode


if __name__ == '__main__':
    url, email = sys.argv[1:]
    data = urlencode({'email': email}).encode()
    request = Request(url, data)
    with urlopen(request) as response:
        print(response.read().decode())
