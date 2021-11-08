# -----------------------------------------------------------------
# 1 - Built-in Functions
# -----------------------------------------------------------------

# Clearing the shell:
# Windows: CTRL + L
# Mac OS: CMD + K

# print("Hello Everybody")
# input("What is your email?")

# -----------------------------------------------------------------
# 2 - Variables
# -----------------------------------------------------------------

# Example with variable and input()
# firstName = input("What is your name? ")
# print("Your name is " + firstName)

# Example with reassining value of variable
# price = 1000
# print(price)

# price = 500
# print(price)


# -----------------------------------------------------------------
# 3 - Rules of Naming Variables
# -----------------------------------------------------------------
# (1) Cannot name variable after reserved keyword
# (2) Variable must start with lowercase letter or _
# (3) Variable cannot have any special characters except _ or numbers
# (4) Use camel-case notation

# More examples of variables
# firstName = "John"
# lastName = "Doe"
# price = 1000


# -----------------------------------------------------------------
# 4 - Data Types
# -----------------------------------------------------------------
# Strings
# Numbers
#    Integer
#    Float  
# Boolean
# Null
# Object
# Class

# Examples of string
# "ABABABA 10101010 ____"
# 'Welcome to Expo 2020!'

# 'She said "Good Morning"'
# "I can't make it today"

# "She said \"Good Morning\""

# "Your name is " + "Mary"

# "Your name is Mary"


# -----------------------------------------------------------------
# 5 -  Operators
# -----------------------------------------------------------------
# =                 Assignment
# <                 Less than
# >                 Greater than
# <=                Less than or equal
# >=                Greater than
# ==                Equality
# !                 Not
# !=                Not equal
# ||                Or
# &&                And


# -----------------------------------------------------------------
# 6 - Control Statements
# -----------------------------------------------------------------
# price = 1000
# budget = 1500


# if price <= budget:
#     print("Buy the product")
# else:
#     print("Don't buy the product")


# Apple Airpods Pro: 700
# Samsung Earbuds 2: 600
# Jabra Elit 75T: 400
# Sony XM4: 500

# userSelection = input("Please select a product: ") # Jabra Elit 75T 

# if userSelection == "Apple Airpods Pro":
#     print(700)
# elif userSelection == "Samsung Earbuds 2":
#     print(600)
# elif userSelection == "Jabra Elit 75T":
#     print(400)
# elif userSelection == "Sony XM4":
#     print(500)
# else:
#     print("Sorry, this product is not available")


# -----------------------------------------------------------------
# 7 - Data Structures (List)
# -----------------------------------------------------------------
# alphabet = [
#     "A",                # 0
#     "B",                # 1
#     "C",                # 2 
#     "D",                # 3
#     "E"                 # 4
# ]

# print( alphabet[4] )


# products = [
#    "Apple Airpods Pro",  
#    "Samsung Earbuds 2", 
#    "Jabra Elit 75T", 
#    "Sony XM4" 
# ]

# Simple example with for loop
# print( "Welcome to our e-commerce store: ")

# for elemenetVal in products:
#     print(elemenetVal)


# Example with enumerate()
# print( "Welcome to our e-commerce store: ")
# for index, value in enumerate(products):
#     print(products[index])


# -----------------------------------------------------------------
# 7.1 - List Methods
# -----------------------------------------------------------------
# https://www.w3schools.com/python/python_ref_list.asp
# .append(value)               Adds element to end of List  
# .pop(index=optional)         Removes element from end of List OR specified index  
# .insert(index, value)        Adds element to start of List OR specified index
# .remove()                    Removes element from start of List
# .reverse()                   Reverses the elements according to value


# alphabet = [
#     "B",                # 0
#     "C",                # 1 
#     "D",                # 2
#     "F"                 # 3
# ]


# # Add to the end
# alphabet.append("G")

# # Add to the end
# alphabet.append("H")

# # Add at the beginning
# alphabet.insert(0, "A")

# # Add in the middle
# alphabet.insert(4, "E")  

# print(alphabet)




# destinations = [
#     'Tokyo',
#     'Bali',
#     'Istanbul',
#     'Cairo',
#     'Mahe',
#     'Rome'
# ]

# # Example with 'break'
# for city in destinations:
#     if city == 'Mahe':
#         print('Yeah, we fly there')
#         break
#     else:
#         print('Sorry, no flights at the moment')


# if "Bali" in destinations:
#     print('Yeah, we fly there')


# petStore = [
#     'cat',
#     'dog',
#     'parrot',
#     'fish',
#     'turtle',
#     'crocodile on the loose',
#     'hamster'
# ]

# Example with the 'if' and 'in' keywords
# if 'crocodile on the loose' in petStore:
#     print("run away")


# Example with the 'if', 'in', and 'not' keywords
# if 'crocodile on the loose' not in petStore:
#     print("go inside")
# else:
#     print("run away")


# -----------------------------------------------------------------
# 7.2 Lists, Sets, Tuples, Dictionaries
# -----------------------------------------------------------------
# List
# - Mutable
# - Repeat values
# - Indexed

# firstName = [
#     'Mohammad',
#     'Mohammad',
#     'Mary',
#     'Mary',
#     'Mike'
# ]

# Set
# - Mutable
# - Unique value
# - Indexed
# airports = {
#     'JFK',
#     'DBX',
#     'LHR',
#     'LAX',
#     'CAI'
# }


# Tuple
# - Immutable
# - Repeat value
# - Indexed
# daysOfWeek = (
#     'Sun',
#     'Mon',
#     'Tue',
#     'Wed',
#     'Thu',
#     'Fri',
#     'Sat'
# )

# Dictionary
# - Mutable
# - Repeat values
# - Unique keys
# - Custom keys
# airports2 = {
#     'JFK': 'New York',
#     'LHR': 'London',
#     'DBX': 'Dubai',
#     'DWS': 'Dubai',
#     'LAX': 'Los Angeles',
#     'CAI': 'Cairo'
# }


# airports3 = {
#     'New York': 'JFK',
#     'London': 'LHR',
#     'Dubai': 'DXB',
#     'Los Angeles': 'LAX',
#     'Cairo': 'CAI'
# }


# print( airports2['Los Angeles'] )


# -----------------------------------------------------------------
# 8 - Functions
# -----------------------------------------------------------------
# Simple example
# def sumTwoNumbers(numA, numB):
#     result = numA + numB
#     return result

# sumTwoNumbers(8,7)
# sumTwoNumbers(10,20)
# sumTwoNumbers(100,200)


# Example calling a function with 'for' statement
# def createGreeting(name, message):
#     return message + ", " + name

# customers = [
#     'Mujahid',
#     'Mohamed',
#     'Sushma',
#     'Amba',
#     'Zulfikar'
# ]

# greeting = "Good Morning"

# for eachCustomer in customers:
#     message = createGreeting(eachCustomer, greeting)
#     print(message)


# -----------------------------------------------------------------
# 9 - Strings
# -----------------------------------------------------------------

# Working with string
# place = "Astrolabs"

# print( place[0] )
# print( place[-1] )
# print( place[8] )
# print( place[ len(place)-1 ])


# String Methods
# .lower()                      Converts string to lower case
# .upper()                      Converts string to upper case
# .casefold()                   Converts string to lower case AND modifies strings
# .title()                      Capitalize the string
# .split(delimeter)             Turn the string into a list by some delimeter
#  delimeter.join(list)         Turn the list into string by some delimeter
# .find()                       Find a matching character in a string
# .format()                     Replace placeholder with values in a string
# .replace()                    Replace a match with a replacement

# place = "AstroLabs"
# print( place.lower() )
# print( place )

# print( place.upper() )

# print( place.casefold() )
# print( place )

# country = "germany"
# print( country.title() )

# todaysDate = "10/10/2021"
# print( todaysDate.split("/") )

# fullName = ['John','M','Doe']
# print( " ".join(fullName) )

# location = "AstroLabs, Cluster R, JLT, Dubai, UAE"
# print( location.find("Dubai") )


# print( "Hello {} {}, \n\nWelcome to {}".format("John","Doe","Dubai") )

# if "Dubai" in location:
#     print("Yes, this is in Dubai")


# print( "ABCDEFGHI"[0:4] )

# print( ["Dubai","Shanghai","Tokyo","Berlin"][1:3]  )

# print( "Sunday 10/Oct/2021".replace("/","-") )

# print( "Hello Mujahid\n\nYou have won AED 1 Million!.\n\nReply to this email to claim your prize".replace("\n","") )



# -----------------------------------------------------------------
# 10 - Multidimensional List
# -----------------------------------------------------------------

# customers = [
#     ['firstname', 'lastname'],
#     ['jack', 'bezos'],
#     ['bill', 'zuckerberg'],
#     ['steve','gates']
# ]


# airports = {
#     'Dubai': [
#         {
#             'airportcode':'DXB',
#             'airportname': 'Dubai International',
#             'no.terminals': 3
#         },
#         {
#             'airportcode':'DWC',
#             'airportname': 'Dubai World Central',
#             'no.terminals': 1
#         }
#     ],
#     'London': [
#         {
#             'airportcode': 'LHR',
#             'airportname': 'London Heathrow',
#             'no.terminals': 5
#         }
#     ]
# }

# print( airports['Dubai'][0]['airportcode']  )



# -----------------------------------------------------------------
# 11 - Classes and Object
# -----------------------------------------------------------------


# class Car:

#     # properties
#     bodyType = ""
#     model = ""
#     brand = ""
#     color = ""
#     speed = 0

#     # methods
#     def __init__(self, brandArg, modelArg, colorArg, bodyTypeArg):
#         self.brand = brandArg
#         self.model = modelArg
#         self.color = colorArg
#         self.bodyType = bodyTypeArg

#     def accelerate(self):
#         # self.speed += 10
#         return

#     def brake(self):
#         # self.accelerate(0)
#         return

#     def gearShift(self):
#         # 
#         return

#     def ignition(self):
#         # 
#         return



# modelX = Car("Tesla", "Model X", "red", "sedan")
# modelX.accelerate()
# modelX.brake()
# modelX.color

# m5 = Car("BMW", "M5", "blue", "sedan")
# m5.color


