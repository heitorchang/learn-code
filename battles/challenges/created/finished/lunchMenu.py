description = """
Pete is a picky eater and dislikes eating the same meal more than once during a school week.

Given the available choices in this week's menu, output the total number of lunch combinations Pete can choose so he doesn't repeat a meal. Note that order does not matter: Pete only cares that the five meals in one choice are different from those in another choice. 

"""

from itertools import product

def lunchMenu(menu):
    def countBeans(seq):
        return sum(1 for meal in seq if 'bean' in meal)

    acceptable = set()
    count = 0
    
    options = product(*menu)
    
    for option in options:
        
        # conversion to set will exclude repeats
        f = frozenset(option)
        if len(f) == 5:
            if f not in acceptable:
                if countBeans(f) <= 2:
                    acceptable.add(frozenset(option))
    return len(acceptable)


"""
test(lunchMenu([["hot dogs", "schnitzels", "spaghetti"],
                ["schnitzels", "hot dogs"],
                ["pizza", "meatballs", "hot dogs"],
                ["beef stroganoff", "burgers"],
                ["curry", "burgers"]]), 21)

test(lunchMenu([["Cream cheese"],
                ["Cream cheese"],
                ["Cream cheese"],
                ["Cream cheese"],
                ["Cream cheese"]]), 0)

    
test(lunchMenu([["corn", "rice"],
                ["rice", "corn"],
                ["beans", "okra"],
                ["beans", "salad"],
                ["pasta", "corn"]]), 0)
"""

test(lunchMenu([["bean burrito", "mac and cheese"],
                ["bean casserole", "chicken pot pie"],
                ["green beans", "roast beef"],
                ["bean curd", "mac and cheese"],
                ["bean soup", "roast beef"]]), 4)
                 
