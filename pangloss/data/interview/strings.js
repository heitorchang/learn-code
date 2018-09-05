data = data.concat([


//////////////////////////////////////////////////////////////////////
//
// STRINGS
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Strings',
    title: 'Reverse',
    reference: '',
    description: ``,
    code: `
"abc"[::-1]

s = "esrever"
r = s[::-1]
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Check if upper, lower, digit, etc.',
    reference: '',
    description: `Given a string, check if all its characters are uppercase, lowercase, digits, etc.`,
    code: `
s = "my string"
s.islower()
s.isupper()
s.isdigit()
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Convert to upper and lowercase',
    reference: '',
    description: ``,
    code: `
s = "PyThOn iZ kEwL"
s.upper()  # PYTHON IZ KEWL
s.lower()  # python iz kewl
s.swapcase()  # pYtHoN Iz KeWl
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
    topic: 'Strings',
    title: 'Encode and decode (strings to bytes)',
    reference: 'Python Fluente, p. 131',
    description: ``,
    code: `
s = 'café'
b = s.encode('utf-8')
d = b.decode('utf-8')
`
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Case-insensitive comparisons',
    reference: 'Python Fluente, 133',
    description: `When dealing with non-ASCII characters, lower() is not reliable`,
    code: `
s = "AbCdE"
s.casefold()  # 'abcde'
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Unicode normalization',
    reference: 'Python Fluente, 150',
    description: `Normalization of Unicode strings allow for safer comparisons between them`,
    code: `
from unicodedata import normalize

s = "café"
normalize('NFC', s)  # 'café'

# NFC combines characters as much as possible
# (resulting in the shortest string)

# NFD decomposes characters into basic ones (letters and diacritics)

# NFC is recommended by the W3C

# NFKC and NFKD (the K stands for Compatibility) are stronger forms
# of normalization

# NFKC and NFKD cause loss of data (4^2 becomes 42) so must be used
# with caution
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Remove diacritics',
    reference: 'Python Fluente, 156',
    description: ``,
    code: `
import unicodedata
import string

def remove_diacritics(s):
    norm_s = unicodedata.normalize('NFD', s)
    result = ''.join(c for c in norm_s if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', result)
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Generate the alphabet',
    reference: '',
    description: ``,
    code: `
alphabet = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])    
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
