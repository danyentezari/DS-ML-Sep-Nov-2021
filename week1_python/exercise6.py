# Exercise 6 – Correct the Customer Names
customers = [
    "mujahid",
    "haZem",
    "HEBA",
    "haLLA",
    "dominque"
]

customersCorrected = []

# 1 - Use a for loop to enumerate the list of customer name
for name in customers:
    # 2 - Use the appropriate string methods to preprocess the name
    preprocessed = name.lower()
    capitalized = preprocessed.capitalize()
    # 3 - Capitalize the names of customer (make the first letter uppercase)
    customersCorrected.append( capitalized )


print(customersCorrected)