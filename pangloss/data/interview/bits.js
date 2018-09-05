data = data.concat([

////////////////////////////////////////////////////////////
//
// BITS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Bits',
    title: 'Turning individual bits on or off',
    reference: 'https://codefights.com/interview-practice/topics/bits/tutorial',
    description: `Given an arbitrary bit sequence, turn a specific bit on or off`,
    code: `
def turn_bit_on(n, idx):
    """Turn n's bit on (set to 1) at index idx,
    where the rightmost bit is 0,
    then the second-to-last is 1"""

    # idea:
    #    0b?????
    # OR 0b00100
    #    -------
    #        x   will always equal 1

    on_seq = 1 << idx
    return n | on_seq

def turn_bit_off(n, idx):
    """Turn n's bit off (set to 0) at index idx,
    where the rightmost bit is 0,
    then the second-to-last is 1"""

    # idea:
    #     0b?????
    # AND 0b11011
    #     -------
    #         x   will always equal 0

    bit_len = n.bit_length()
    off_seq = ~(1 << idx)  # use NOT operator

    return n & off_seq    
    `
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Representing numbers in binary',
    reference: '',
    description: ``,
    code: `
# decimal to binary
n = 30
s = bin(n)[2:]  # '11110'

# binary to decimal
x = int(s, 2)   # int(string, base)
testeql(n, x)
    `
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Find the single number among pairs of numbers',
    reference: 'HackerRank, CodeFights',
    description: `Given an array where there is a single unique number and every other number occurs twice, find this single number.
      <br><br>
    Trick: an XOR operation will set the first number, and is reversible. When numbers overlap, the latest operation will be reversed when the number is encountered again.
      <br><br>
      Note: XOR is commutative, a ^ b == b ^ a, and associative, a ^ (b ^ c) == (a ^ b) ^ c.
    `,
    code: `
def single_integer(a):
    runningVal = 0
    for i in a:
        runningVal ^= i
    return runningVal    
    `
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Invert ones and zeros',
    reference: '',
    description: ``,
    code: `
# use the NOT operator, ~ (tilde)

x = 0b10011
n = ~x
print(x | n)  # -1 (see Twos' complement)
    `
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Twos\' complement',
    reference: 'https://stackoverflow.com/questions/34300336/negative-numbers-to-binary-system-with-python',
    description: `See a negative value as a series of bits without the minus sign`,
    code: `
n = -12
width = 16
bin(n + (1 << width))
`
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Toggle a bit',
    reference: '',
    description: `Toggle a bit at index idx, swapping a 0 with a 1 and a 1 with a 0.`,
    code: `
def toggle_bit(n, idx):
    """Toggle bit at index idx,
    where the rightmost bit is 0,
    then the second-to-last is 1"""

    toggle_mask = 1 << idx
    return n ^ toggle_mask  # use XOR
    `
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Create byte sequence from hex values',
    reference: 'Python Fluente, 133',
    description: ``,
    code: `
b = bytes.fromhex("31 4b ce a9")  # b'1K\\xce\\xa9'
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
