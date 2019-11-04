# Fermat Primality Test

# From Wikipedia (The Fermat primality test is actually a compositeness test)

# To test an integer n, pick an integer a that is coprime to n and calculate a^(n-1) mod n.

# If the result is not 1, then n is composite.
# If the result is 1, n may or may not be prime.

# Numbers for which this test fails are called Carmichael numbers, the smallest of which is 561

def isProbablyPrime(n):
    return pow(2, n-1, n) == 1
