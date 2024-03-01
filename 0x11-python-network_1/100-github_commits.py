#!/usr/bin/python3
""" 100-github_commits: takes 2 arguments in order to solve this challenge """
import sys
import requests


if __name__ == '__main__':
    repository, owner = sys.argv[1:]
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'
    response = requests.get(url)
    for commit in response.json()[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
