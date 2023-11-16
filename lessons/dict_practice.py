"""Practice with dictionary"""

#Create a new dictionary
icecream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Create my dictionary:")
print(icecream)

#Adding a key, value pair to a dictionary 
icecream["mint"] = 3
print("Added mint to dictionary:")
print(icecream)

#Removing a key, value pair
icecream.pop("mint")
print("Removed mint from dictionary")
print(icecream)

#Accesing a value
print(f"There are {icecream['chocolate']} orders of choclate")

#Updating a value
icecream["vanilla"] = 10
print("After updating vanilla:")
print(icecream)

print(f"There are {len(icecream)} key value")
      
#Check if value in dictionary
print("Chocolate in dictionary?")
print("chocolate" in icecream)

if "mint" in icecream:
    print({icecream["mint"]})
else:
    print("No orders of mint.")

#Loop through dictionary
for flavor in icecream:
    #print out <flavor> has <num orders> orders
    print(f"{flavor}has {icecream[flavor]} orders.")
    print(icecream["chocolate"])
    