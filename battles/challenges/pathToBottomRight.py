test1 = r"""
         o
        / \
       o   o
      /   / \
     o   o   o           
    /     \
   o       o
"""

test2 = r"""
       o
      /
     o
    /
   o
  /
 o
"""

test3 = r"""
    o
   / \
  o   o
       \
        o
       / \
      o   o
           \
            o
"""


test4 = r"""
     o
    /
   o
    \
     o
    /
   o
    \
     o
    / \
   o   o
"""

ans4 = "LRLRR"

test5 = r"""
           o
          / \
         o   o
        / \   \
       o   o   o
      /     \   \
     o       o   o
            /   /
           o   o
            \
             o
"""

ans5 = "LRRLR"

test6 = r"""
       o
      / \
     o   o
    /   / \
   o   o   o
          /
         o
        / \
       o   o
      /
     o
    /
   o
  /
 o
"""

ans6 = "RRLLLLL"

test7 = r"""
    o
   / \
  o   o
"""

ans7 = "R"

test8 = r"""
   o
  / \
 o   o
  \
   o
    \
     o
      \
       o
"""

ans8 = "LRRR"

def format(tree):
    lines = []
    for line in tree.splitlines():
        if len(line) > 0:
            line = line.replace("/", "╱")
            line = line.replace("\\", "╲")
            lines.append('"{}"'.format(line + (30 - len(line))*" "))
    print("[" + ", ".join(lines) + "]")
