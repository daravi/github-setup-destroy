#!/Users/daravi/anaconda/envs/python3/bin/python3

import argparse
import getpass
import json
import os

import requests

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", help="GitHub username to create the repository for.", default="daravi")
parser.add_argument("-n", "--name", help="Name of the repository to be created.")
parser.add_argument("-d", "--description", help="Description of the repository to be created.")
args = parser.parse_args()

username = args.user

if args.name:
	name = args.name
else:
	name = input("repo name: ")
if args.description:
	description = args.description
else:
	description = input("repo description: ")

password = getpass.getpass('Enter GitHub password for ' + username + ': ')

data = {'name': name, 'description': description}

r = requests.post('https://api.github.com/user/repos', json=data, auth=(username, password))

remote_url = r.json()['html_url']

os.system('git init')
os.system('git add .')
os.system('git commit -m "First commit"')
os.system('git remote add origin ' + remote_url)
os.system('git push -u origin master')