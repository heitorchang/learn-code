#!/usr/bin/env python3

import sys
from subprocess import call

if __name__ == '__main__':
    javafile = sys.argv[1]

    call(["javac", javafile])
    call(["java", javafile.replace(".java", "")])
