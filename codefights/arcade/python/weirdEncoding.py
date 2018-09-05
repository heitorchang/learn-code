from base64 import b64encode, b64decode

def weirdEncoding(encoding, message):
    return (b64decode(bytes(message, 'ascii'), altchars=encoding)).decode('ascii')

def test():
    testeql(weirdEncoding("-_", "Q29kZUZpZ2h0cw=="), "CodeFights")
