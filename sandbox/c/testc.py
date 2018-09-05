#!/usr/bin/env python3

import sys
from subprocess import call

if __name__ == '__main__':
    cfile = sys.argv[1]
    ofile = cfile.replace(".c", ".o")
    
    call(["gcc", "-o", ofile, cfile])
    call(["./" + ofile])
