# Exercise 7 – Add Up the Value
sales = [
    "$10000",
    "$25 000",
    "$1300",
    "$ 10200",
    "$ 1300",
    "$10200",
    "$30200",
]

total = 0

# 1 - Use a for loop to enumerate the list of sales values
# for value in sales:
#     print( value )

# 2 - Use the appropriate string methods to preprocess the values
# Note: to cast use int() function
# for value in sales:
#     price = value
#     priceNoCurrency = price.replace("$","")
#     priceNoSpace =  priceNoCurrency.replace(" ", "")
#     priceInt = int(priceNoSpace)
#     print(priceInt)


# 3 - Add up each value to get the total


# Solution A
# for value in sales:
#     price = value
#     # Replace the $ sign
#     priceNoCurrency = price.replace("$","")
#     # Replace the spaces
#     priceNoSpace =  priceNoCurrency.replace(" ", "")
#     # Cast as integer
#     priceInt = int(priceNoSpace)
#     # Increment total by the integer
#     total += priceInt

# print( total )


# Solution B
# for value in sales: 
#     total += int(value.replace("$","").replace(" ", ""))

# print(total)