data = data.concat([

//////////////////////////////////////////////////////////////////////
//
// EMACS SETUP
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Emacs Setup',
    title: '.emacs',
    reference: '',
    description: `Add to your .emacs file`,
    code: `
(global-set-key (kbd "<f5>") 'run-python)

(setenv "PYTHONPATH" "/home/heitor/shared/python/my-modules/")

(setenv "PYTHONSTARTUP" "/home/heitor/shared/python/my-startup.py")

(defun my-python-test-buffer ()
  (interactive)
  (save-excursion
    (python-shell-send-string (trim-string (buffer-string)))
    (python-shell-send-string (concat "print('')\\n" "test()"))))

(add-hook 'python-mode-hook
          (lambda ()
            (local-set-key [M-return] 'my-python-test-buffer)))

(add-hook 'inferior-python-mode-hook
          (lambda ()
            (auto-complete-mode 1)))
    `
  },

  { // begin new topic
    topic: 'Emacs Setup',
    title: 'Python Startup',
    reference: '',
    description: ``,
    code: `
# file: my-startup.py

from math import exp, log, sin, cos, tan, asin, acos, atan, floor, ceil
import math
import re
from mytests import testeql, pr

# add common strings to include in autocomplete

print("testeql")
    `
  },

  { // begin new topic
    topic: 'Emacs Setup',
    title: 'Python mytests',
    reference: '',
    description: ``,
    code: `
# file: mytests.py

import sys

def testequal(expression, expected):
    print("testing", expression, "expecting", expected)

    # special case: floats, check up to 6 decimal places
    if isinstance(expression, float):
        test_passed = abs(expression - expected) < 1e-6
    else:
        test_passed = expression == expected
    if test_passed:
        print("(^o^) PASS\\n")
    else:
        print("(>_<) FAIL\\n")

# alias
testeql = testequal

def pr(s):
    """pr('a b c') prints each of the names separated by a space"""
    if type(s) != str:
        raise ValueError("Argument to pr() must be a string")
    frame = sys._getframe(1)
    names = s.split()
    for name in names:
        print(name, '=', repr(eval(name, frame.f_globals, frame.f_locals)), end=", ")
    print()
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);
