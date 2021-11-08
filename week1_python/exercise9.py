hotel = {
    "name": "Burj Al Arab",
    "no.stars": 7,
    "location": "Dubai, United Arab Emirates",
    "types.room": [
        {
            "name": "Presidential",
            "price": 50000
        }, 
        {
            "name": "Panoramic",
            "price": 35000
        }, 
        {
            "name": "Sky Marina",
            "price": 20000
        }, 
        {
            "name": "Palace",
            "price": 45000
        }, 
        {
            "name": "The Seventh Star",
            "price": 40000
        }
    ],
    "helipad": True
}


# 1 - Print the name of the hotel
print( hotel['name'] )

# 2 - Print the number of stars for the hotel
print( hotel['no.stars'] )

# 3 - Print the number of the types of rooms
print( len(hotel['types.room']) )

# 4 - Put the prices of the rooms into a separate list
roomPrices = []
for room in hotel['types.room']:    
    roomPrices.append( room['price'] )
print(roomPrices)

# 5 - If the hotel has a helipad, print "Fly away!"
if hotel['helipad'] == True:
   print("Fly away!")

# 6 - Print all of the keys of hotel
# hint: you can use the .keys() method
print( hotel.keys() )

# 7 (Bonus) - Add an element to the "Presidential" room
# with key "accesstohelipad" and value True
hotel['types.room'][0]['accesstohelipad'] = True
print( hotel['types.room'][0] )