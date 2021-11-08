# Exercise 4
# Do not change the code below
jar = [
    'Red Ball',
    'Blue Ball',
    'Red Ball',
    'Red Ball',
    'Blue Ball',
    'Red Ball',
    'Red Ball',
    'Blue Ball'
]

redBall = []
blueBall = []


# 1 - Use either the (a) 'for', (b) 'if else', or (c) 'if in' statements 
# to enumerate 'jar'

# 2 - Put each element in the correct List

for value in jar:
    if value == "Red Ball":
        redBall.append(value)
    else:
        blueBall.append(value)

print(redBall)
print(blueBall)