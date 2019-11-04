import re

p = re.compile('\w+?')

a = p.findall('aabbbc')

pr('a')
