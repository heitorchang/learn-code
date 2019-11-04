def isSentenceCorrect(sentence):
    pattern = re.compile(r'[A-Z][^.!?]*?[.!?]$')
    return re.match(pattern, sentence) is not None
