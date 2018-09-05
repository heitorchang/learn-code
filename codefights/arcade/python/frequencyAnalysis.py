from collections import Counter

def frequencyAnalysis(encryptedText):
    return [Counter(encryptedText).most_common(1)[0][0]]

def test():
    testeql(frequencyAnalysis("$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ"), ["C"])
