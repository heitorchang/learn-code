data = data.concat([

////////////////////////////////////////////////////////////
//
// NUMBER MANIPULATION
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Convert decimal to bin, oct, hex',
    reference: '',
    description: ``,
    code: `
n = 123
b = bin(n)[2:]  # discard initial 0b
o = oct(n)[2:]
h = hex(n)[2:]
    `
  },

  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Convert arbitrary base to decimal',
    reference: '',
    description: ``,
    code: `
n = '3eg'  # some number in base 19
d = int(n, 19)  # 1365 in decimal

# If coding literally, write:
h = 0xfe
o = 0o755
b = 0b1101
    `
  },

  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Process integer\'s digits right-to-left',
    reference: 'CodeFights Tourneys',
    description: `Given a decimal integer, do something digit-by-digit, starting from ones (right side)`,
    code: `
n = 12345
while n > 0:
    digit = n % 10
    print(digit)
    n //= 10
    `
  },

  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Convert integer to list of digits',
    reference: '',
    description: ``,
    code: `
n = 12345

digits = [int(c) for c in str(n)]
    
digits = list(map(int, str(n)))
    `
  },

  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Change a decimal integer to arbitrary base',
    reference: 'Rosen p. 249',
    description: `Valid for 2 <= base <= 9`,
    code: `
def changeBase(n, base):
    if n == 0:
        return '0'

    digits = []

    while n > 0:
        digits.append(n % base)
        n //= base
    return ''.join(map(str, digits))[::-1]
    `
  },

  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Convert list of ints to string',
    reference: '',
    description: ``,
    code: `
a = [1, 2, 3]

''.join(str(d) for d in a)
    
''.join(map(str, a))
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
