def test():
    testeql(findEmailDomain("prettyandsimple@example.com"), "example.com")
        
def findEmailDomain(address):
    atIndex = address.rfind('@')
    return address[atIndex+1:]

