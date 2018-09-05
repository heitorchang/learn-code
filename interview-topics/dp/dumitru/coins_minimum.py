description = """
Given a list of N coins valued (V1, V2, V3, ...) and a total sum S, find the
minimum number of coins to total S (we can use as many coins of one type
as we want), or report that it is not possible to get to sum S"""

def my_coins(values, s):
    """My code after reading English solution"""
    max_coins = s // min(values) + 1
    states = [0 for _ in range(s+1)]
    for state in range(1, s+1):
        pr('state')
        cur_min = max_coins
        for j in range(state):
            pr('j')
            for coin in values:
                if coin <= state:
                    prs('coin j')
                    if coin + j == state and states[j] + 1 < cur_min:
                        cur_min = states[j] + 1
        states[state] = cur_min
    return states[s]
                       
def coins_given_solution(values, s):
    Min = [float('inf') for _ in range(s+1)]
    Min[0] = 0

    for i in range(s + 1):
        for j in range(len(values)):
            # no need for inner loop because the only states we only
            # go back to are values of coins
            if (values[j] <= i and Min[i-values[j]] + 1 < Min[i]):
                Min[i] = Min[i-values[j]] + 1
    return Min[-1]
        

def test():
    testeql(my_coins([1,3,5], 5), 1)
    testeql(my_coins([1,3,5], 11), 3)
    testeql(coins_given_solution([1,3,5], 11), 3)
