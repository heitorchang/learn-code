#!python

import sys
from os import chdir
from subprocess import call
from gitall import GIT_REPOS, HOME_DIR

for repo in GIT_REPOS:
    repo_dir = "{}{}".format(HOME_DIR, repo)
    print("In repo", repo_dir)
    sys.stdout.flush()
    chdir(repo_dir)
    call(["git", "status", "--short"])
    sys.stdout.flush()
    
