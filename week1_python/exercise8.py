landmarks = [
    ["Burj Khalifa", "1 Sheikh Mohammed bin Rashid Blvd - Downtown Dubai - Dubai"],
    ["The Louvre", "Rue de Rivoli, 75001 Paris, France"],
    ["Big Ben", "London SW1A 0AA, United Kingdom"],
    ["Expo 2020", "Expo 2020 Dubai Expo Road, Dubai South Jebel Ali, Dubai, United Arab Emirates "],
    ["Brandenburg Gate", " Pariser Platz, 10117 Berlin, German"],
    ["Tokyo Skytree", "1 Chome-1-2 Oshiage, Sumida City, Tokyo 131-0045, Japan"]
]

visitUAE = []

# Find the landmarks that are in the UAE. If a landmark in the 
# UAE, add the landmark name to the visitUAE list.


# Solution A
# index = 0
for index, value in enumerate(landmarks):         # entry = ["Burj Khalifa", "1 Sheikh..."]
    name = landmarks[index][0]
    address = landmarks[index][1]
    if "Dubai" in address:
        visitUAE.append(name)

print(visitUAE)




# Solution B
# def isInsideDubai(landmark):
#     address = landmark[1]
#     if "Dubai" in address:
#         return True

# for entry in landmarks:
#     if isInsideDubai(entry) == True:
#         visitUAE.append(entry[0])
# print(visitUAE)