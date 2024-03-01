#!/usr/bin/python3
""" 100-github_commits: takes 2 arguments in order to solve this challenge """
import sys
import requests


if __name__ == '__main__':
    repository, owner = sys.argv[1:]
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'
    response = requests.get(url)
    for element in response.json()[:10]:
        commit = element.get('commit')
        print(f'{commit.get("tree").get("sha")} \
{commit.get("author").get("name")}')
