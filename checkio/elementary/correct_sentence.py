def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    result = text[0].upper() + text[1:]
    if result[-1] != ".":
        result += "."
    return result

    
