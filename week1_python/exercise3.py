ingredients = [
    'tomato',
    'chilli',
    'banana',
    'eggs',
    'cheese',
    'pepperoni',
    'strawberry',
    'olives',
    'pineapple'
]


pizza = []

# Add your code below...

# 1 - Complete your blacklist manually
blacklist = ['strawberry','banana','eggs','pineapple']

# 2 - If an ingredient is not in the blacklist,
# add the ingredient to the pizza
for item in ingredients:
    if item not in blacklist:
        pizza.append(item)


# 3 – Print the pizza list
print( pizza )