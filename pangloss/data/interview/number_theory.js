data = data.concat([

//////////////////////////////////////////////////////////////////////
//
// NUMBER THEORY
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Number Theory',
    title: 'Sieve of Eratosthenes',
    reference: 'CodeFights',
    description: ``,
    code: `
def primes(n):
    if n < 2:
        return []
    isPrime = [True] * (n+1)  # begin with all numbers prime
    for base in range(3, int(n ** 0.5) + 1, 2):  # potential primes
        # stop at sqrt(n) because the larger number would
        # have already been crossed out
        for multiple in range(base * 2, n+1, base):
            isPrime[multiple] = False
    primeList = [2]  # manually include the only even number
    for n in range(3, n+1, 2):  # consider all odd numbers
        if isPrime[n]:
            primeList.append(n)
    return primeList

def test():
    testeql(primes(73), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73])    
    `
  },

  { // begin new topic
    topic: 'Number Theory',
    title: 'Compositeness Test (pseudoprimes)',
    reference: 'https://en.wikipedia.org/wiki/Fermat_primality_test',
    description: `Check if a given number is probably prime. Carmichael numbers are composite, but will fool Fermat's test (it is a flawed test).`,
    code: `
def isProbablePrime(n):
    if n == 2:
        return True
    if not n & 1:
        return False  # even numbers
    return pow(2, n-1, n) == 1    
    `
  },


  { // begin new topic
    topic: 'Number Theory',
    title: 'GCD (Euclid\'s algorithm)',
    reference: 'SICP, sec. 1.2.5, PDF p. 78',
    description: ``,
    code: `
from fractions import gcd

def sicp_gcd(a, b):
    if b == 0:
        return a
    return sicp_gcd(b, a % b)
    `
  },


  { // begin new topic
    topic: 'Number Theory',
    title: 'LCM (using GCD)',
    reference: 'https://www.programiz.com/python-programming/examples/lcm',
    description: ``,
    code: `
from fractions import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)
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
