def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    begin_index = text.find(begin)
    end_index = text.find(end)

    if begin_index == -1:
        left_bound = 0
    else:
        left_bound = begin_index + len(begin)
        
    if end_index == -1:
        right_bound = len(text)
    else:
        right_bound = end_index
        
    return text[left_bound:right_bound]
