#!/Users/daravi/anaconda/envs/python3/bin/python3

import argparse
import getpass
import os

import requests

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", help="GitHub username to remove the repository from.", default="daravi")
args = parser.parse_args()

username = args.user
password = getpass.getpass('Enter GitHub password for ' + username + ': ')
repo_name = os.popen("git remote -v | head -n1 | awk '{print $2}' | sed 's/.*\///' | sed 's/\.git//'").read()[:-1]

r = requests.delete('https://api.github.com/repos/' + username + '/' + repo_name, auth=(username, password))
os.system('rm -rf .git')
