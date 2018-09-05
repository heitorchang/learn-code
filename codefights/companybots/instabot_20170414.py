import re
from decimal import Decimal

from itertools import combinations
from collections import defaultdict

def deliveryFee(intervals, fees, deliveries):
    intervals.append(24)
    delCt = [0 for _ in range(len(intervals))]
    
    for delivery in deliveries:
        pr('delivery')
        for i in range(1, len(intervals)):
            if delivery[0] < intervals[i]:
                pr('delivery[0]')
                delCt[i-1] += 1
                break
    delCt = delCt[:-1]
    pr('delCt')
    ratio = [0 for _ in range(len(fees))]
    for i in range(len(fees)):
        if delCt[i] > 0:
            ratio[i] = fees[i] / delCt[i]
    pr('ratio')
    val = ratio[0]
    for r in ratio:
        if abs(r-val) > 0.0001:
            return False
    return True

def shoppingList(items):
    p = re.compile(r'[0-9]+\.?[0-9]*')
    m = p.search(items)
    total = Decimal('0.00')
    while m:
        pr('m.group()')
        total += Decimal(m.group())
        e = m.span()[1]
        items = items[e:]
        m = p.search(items)
    return float(total)

description = """
The FDA recommends that for a healthy, balanced diet, a person on average needs around 2,000 Kcal a day to maintain their weight. As a result, Instacart is set to release a new feature that will help customers control their daily intake of calories. Given a list of items in a customer's cart, it will show the items that can be consumed in one day such that their total caloric value is as close to 2000 as possible.

Knowing the caloricValue of each bought item, return the 0-based indices of the items to be consumed in one day. If there is more than one option, return the lexicographically smallest one.

Example

For caloricValue = [400, 800, 400, 500, 350, 350], the output should be
dailyIntake(caloricValue) = [0, 2, 3, 4, 5].

Caloric value of items [1, 3, 4, 5] and [0, 2, 3, 4, 5] both sum up to 2000 but since [0, 2, 3, 4, 5] is lexicographically smaller than [1, 3, 4, 5], the answer is [0, 2, 3, 4, 5].

For caloricValue = [150, 900, 1000], the output should be
dailyIntake(caloricValue) = [0, 1, 2].

The total sum of all items (i.e. 2050) is 50 Kcal larger than 2000, so the answer is [0, 1, 2].

Input/Output

[time limit] 4000ms (py3)
[input] array.integer caloricValue

Caloric value of each item in the cart. The total sum of all items is not greater than 104.

Guaranteed constraints:
1 ≤ caloricValue.length ≤ 30,
2 ≤ caloricValue[i] ≤ 104.

[output] array.integer

The items to consume in a day.
"""

from itertools import combinations
from collections import defaultdict

def computeDiff(caloricValue, selected):
    target = 2000
    total = 0
    for s in selected:
        total += caloricValue[s]
    result = abs(total - 2000)
    return result

def dailyIntake(caloricValue):
    if abs(caloricValue[0]) > 2000:
        return []
    if len(caloricValue) == 1:
        return [0]
    mindiff = 2000
    r = range(len(caloricValue))
    sums = defaultdict(list)
    for i in range(1, len(caloricValue)+1):
        localMin = 2000
        cl = combinations(r, i)
        for c in cl:
            pr('c')
            d = computeDiff(caloricValue, c)
            if d <= localMin:
                localMin = d
                
            if d <= mindiff:
                mindiff = d
                sums[mindiff].append(c)

        if localMin > mindiff:
            break
    return list(sorted(sums[mindiff])[0])

    
def test():
    #testeql(deliveryFee([0, 10, 22], [1,3,1], [[8,15], 
    #                                           [12,21], 
    #                                           [15,48], 
    #                                           [20,17],
    #                                           [23,43],
    #                                           ]), True)

    # testeql(shoppingList("wanna 22.2&15.3olo 0.00 and 12.12kk0.02 ..34"), 83.64)
    # testeql(shoppingList("Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4"), 7.48)
    testeql(dailyIntake([1000, 2100, 700, 1100]), [0,3])
    testeql(dailyIntake([150, 900, 1000]), [0,1,2])
