#!/usr/bin/python3
""" 10-my_github: takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """
import sys
import requests


if __name__ == '__main__':
    username, password = sys.argv[1:]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    print(response.json().get('id'))
