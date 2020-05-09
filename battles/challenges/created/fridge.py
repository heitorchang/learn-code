desc = """
Your startup has gone from ramen profitable to rice and beans profitable, but you think cooking is a waste of time that could be used for coding. You will now try optimizing your kitchen planning.

Given the ingredients `available` in your fridge and the `needed` ones for a recipe, return the **number of portions** that can be made from the available ingredients.

Each of these arguments is a string. Ingredients and their quantities are separated by commas. Ingredients are always in the plural and may have spaces. They are not ordered in any meaningful way.

Measurements for ingredients (such as cups, pounds) will be the same in both arguments. Numbers are always integers.

For example:

```
available: "3 carrots, 2 bell peppers, 5 cups rice, 10 potatoes"
needed: "1 carrots, 1 bell peppers, 2 potatoes"
```

You should return `2`, because you'll be out of bell peppers after making the second portion of the recipe.
"""

def dictionize(s):
    """convert string argument to dict of ingredients"""
    dc = {}
    for e in s.split(","):
        e = e.strip()
        tokens = e.split()
        ct = int(tokens[0])
        name = " ".join(tokens[1:])
        dc[name] = ct
    return dc

def fridge(available, needed):
    ad = dictionize(available)
    nd = dictionize(needed)

    portions = 0
    while True:
        for ingr in nd:
            if ingr not in ad:
                return portions
            
            if ad[ingr] < nd[ingr]:
                return portions
        else:
            for ingr in nd:
                ad[ingr] -= nd[ingr]
            portions += 1
                
pairtest(
    fridge(
        "3 carrots, 2 bell peppers, 5 cups rice, 10 potatoes",
        "1 bell peppers, 1 carrots, 2 potatoes"
    ), 2,

    fridge(
        "10 eggs, 3 cups flour",
        "5 eggs, 1 cups sugar, 2 cups flour"
    ), 0,

    fridge(
        "2342 grains rice, 5302 granules salt",
        "250 grains rice, 230 granules salt"
    ), 9,
    
    fridge(
        "5 heads cabbage, 3 pounds chicken, 15 onions",
        "2 onions, 1 pounds chicken, 1 heads cabbage"
    ), 3,
    
    fridge(
        "5000 grams spaghetti, 62 tomatoes, 35 carrots",
        "1 carrots, 1 tomatoes, 100 grams spaghetti"
    ), 35,
)
        
