description = """
Pete is a picky eater and dislikes eating the same meal more than once during a school week.

Given the available choices in this week's menu, output the total number of lunch combinations Pete can choose so he doesn't repeat a meal. Note that order does not matter: Pete only cares that the five meals in one choice are different from those in another choice. 

"""

from itertools import product

def lunchMenu(menu):
    choices = set()
    count = 0
    
    options = product(*menu)
    for option in options:
        if len(set(option)) == 5:
            count += 1
            print(count, option)
            f = frozenset(option)
            if f not in choices:
                choices.add(frozenset(option))
            else:
                print("already added")
    return len(choices)


"""
test(lunchMenu([["Hot dogs", "Schnitzels", "Spaghetti"],
                ["Schnitzels", "Hot dogs"],
                ["Pizza", "Meatballs", "Hot dogs"],
                ["Beef stroganoff", "Burgers"],
                ["Curry", "Burgers"]]), 21)

test(lunchMenu([["Cream cheese"],
                ["Cream cheese"],
                ["Cream cheese"],
                ["Cream cheese"],
                ["Cream cheese"]]), 0)
"""
    
test(lunchMenu([["Corn", "Rice"],
                ["Rice", "Corn"],
                ["Beans", "Okra"],
                ["Beans", "Salad"],
                ["Pasta", "Corn"]]), 0)
