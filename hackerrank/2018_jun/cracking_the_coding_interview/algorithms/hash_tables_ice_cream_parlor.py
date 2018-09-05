description = """
Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

Given the value of money and the cost of each flavor for t trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.

For example, there are n=5 flavors having cost=[1,2,3,5,6]. Together they have money=5 to spend. They would purchase flavors 2 and 3 for a cost of 5. Use 1-based indexing for your response.

Note: Two ice creams having unique IDs i and j may have the same cost

Function Description

Complete the function whatFlavors in the editor below. It must determine the two flavors they will purchase and print them as two space-separated integers on a line.

whatFlavors has the following parameter(s):

cost: an array of integers representing price per flavor
money: in integer representing the amount of money they have to spend
"""

def whatFlavors(cost, money):
    indices = {}
    for i, c in enumerate(cost, 1):
        if money - c in indices:
            return "{} {}".format(indices[money-c], i)
        indices[c] = i

def test():
    testeql(whatFlavors([1,4,5,3,2], 4), "1 4")
    testeql(whatFlavors([2,2,4,3], 4), "1 2")
