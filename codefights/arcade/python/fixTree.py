def fixLine(line):
    return ('*' * line.count('*')).center(len(line), " ")

def fixTree(tree):
    return list(map(lambda line: ('*' * line.count('*')).center(len(line), " "), tree))

def test():
    testeql(fixTree([
  "      *  ", 
  "    *    ", 
  "***      ", 
  "    *****", 
  "  *******", 
  "*********", 
  " ***     "
]), [
  "    *    ", 
  "    *    ", 
  "   ***   ", 
  "  *****  ", 
  " ******* ", 
  "*********", 
  "   ***   "
])

    testeql(fixLine("      *  ") , "    *    ")
