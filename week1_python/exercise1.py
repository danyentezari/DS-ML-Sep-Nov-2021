firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
email = input("Please enter your email: ")
phone = input("Please enter your phone number: ")


# Solution A
# print("Thank you. These are the details")
# print("First name: " + firstName)
# print("Last name: " + lastName)
# print("Email: " + email)
# print("Phone: " + phone)

# Solution B
print(
    "Thank you. These are the details" + "\n" +
    "First name: " + firstName + "\n" +
    "Last name: " + lastName + "\n" +
    "Email: " + email + "\n" +
    "Phone: " + phone
)