#!/usr/bin/python3
""" 0-hbtn_status: fetches https://alx-intranet.hbtn.io/status """
from urllib.request import urlopen


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        data = response.read()
        print('Body response:')
        print(f'\t- type: {type(data)}')
        print(f'\t- content: {data}')
        print(f'\t- utf8 content: {data.decode()}')
