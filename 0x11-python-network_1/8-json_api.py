#!/usr/bin/python3
""" 8-json_api: takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter """
import sys
import requests


if __name__ == '__main__':
    letter = sys.argv[1] if len(sys.argv) > 1 else ''
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': letter})
    try:
        data = response.json()
        if len(data) == 0:
            print('No result')
        else:
            print(f'[{data.get("id")}] {data.get("name")}')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
