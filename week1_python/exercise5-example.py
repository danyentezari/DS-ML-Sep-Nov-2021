# 1 - Create a function called 'coffeeMachine'

# 2 - Give the function the parameters: 
# 'coffeeType', 'milkOption', and 'size'
# possible arguments for coffeeType: 'Latte', 'Americano', 'Turkish'
# possible arguments for milkOption: 'Skimmed Dairy', 'Coconut', 'Almod'
# possible arguments for size: 'small', 'medium', 'large'
def coffeeMachine(coffeeType, milkOption, size):
    cupOfCoffee = []
    cupOfCoffee.append(coffeeType)
    cupOfCoffee.append(milkOption)
    cupOfCoffee.append(size)

    price = 0

    # Check the size
    if size == 'Small':
        price += 1
    elif size == 'Medium':
        price += 3
    elif size == 'Large':
        price += 5
    else: 
        return

    if milkOption == '':
        price += 0
    elif milkOption == 'Dairy':
        price += 2
    elif milkOption == 'Coconut':
        price += 5
    elif milkOption == 'Horse':
        price += 7
    else:
        return

    cupOfCoffee.append(price)

    return cupOfCoffee


# 3 - Call the function to create three different cups of coffee
coffee1 = coffeeMachine("Latte","Coconut","Large")
coffee2 = coffeeMachine("Americano","","Large")
coffee3 = coffeeMachine("Cortado", "Dairy", "Small")

# 4 - Print each result
print(coffee1)
print(coffee2)
print(coffee3)