def checkio(array):
    """
    Second solution (Dec. 2017)
    """
    if len(array) == 0:
        return 0
        
    return sum(array[::2]) * array[-1]
    
