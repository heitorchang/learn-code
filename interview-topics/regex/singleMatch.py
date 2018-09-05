import re

# match state and ZIP code
p = re.compile(r'([A-Z]{1,2}) (\d{1,5})')

address = "San Juan, CA 92301 ; Kealoha HI 99201 ; Pine Grove ID 67293"

m = p.match(address)
testeql(m, None)
# does not match because match() only matches beginning of string

s = p.search(address)
testeql(s.group(), "CA 92301")
# search looks at the entire string, MatchObject.group() returns the entire string

state = s.group(1)
testeql(state, "CA")

zipCode = s.groups()[1]
testeql(zipCode, "92301")

f = p.findall(address)
hawaii = f[1]
testeql(hawaii[0], "HI")

i = p.finditer(address)
for match in i:
    print('iterating...', match.group())
