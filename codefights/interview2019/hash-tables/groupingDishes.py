from collections import defaultdict

def groupingDishes(dishes):
    ingredientsHashTable = defaultdict(list)
    for dish in dishes:
        dishName = dish[0]
        ingredients = dish[1:]
        for i in ingredients:
            ingredientsHashTable[i].append(dishName)
    # print(ingredientsHashTable)
    
    out = []
    for k in sorted(ingredientsHashTable.keys()):
        if len(ingredientsHashTable[k]) > 1:
            out.append([k] + sorted(ingredientsHashTable[k]))

    return out


test(groupingDishes([["Salad","Tomato","Cucumber","Salad","Sauce"], 
 ["Pizza","Tomato","Sausage","Sauce","Dough"], 
 ["Quesadilla","Chicken","Cheese","Sauce"], 
 ["Sandwich","Salad","Bread","Tomato","Cheese"]]),
     [["Cheese","Quesadilla","Sandwich"], 
 ["Salad","Salad","Sandwich"], 
 ["Sauce","Pizza","Quesadilla","Salad"], 
 ["Tomato","Pizza","Salad","Sandwich"]])
