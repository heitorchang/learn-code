from math import exp, log, sin, cos, tan, asin, acos, atan, floor, ceil
import sys
import re
import json
from myunittest import pairtest
# from myjsonutils import myjsonload
from datetime import date, datetime, timedelta

import pprint

pprinter1 = pprint.PrettyPrinter(depth=1)
pprinter2 = pprint.PrettyPrinter(depth=2)
pprinter3 = pprint.PrettyPrinter(depth=3)
pprinter4 = pprint.PrettyPrinter(depth=4)
pprinter5 = pprint.PrettyPrinter(depth=5)
pprinterd = pprint.PrettyPrinter(depth=10)  # deep printer

def pp1(arg):
    pprinter1.pprint(arg)

def pp2(arg):
    pprinter2.pprint(arg)

def pp3(arg):
    pprinter3.pprint(arg)

def pp4(arg):
    pprinter4.pprint(arg)

def pp5(arg):
    pprinter5.pprint(arg)

def pp(arg):
    pprinterd.pprint(arg)

# replace regular print with prettyprint
def myhook(value):
    if value is not None:
        pp(value)

sys.displayhook = myhook
