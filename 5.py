#key value pairs
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
print(karnataka_food["Bengaluru"])
#You can also use the get() method to access values, which is safer because it doesn’t throw an error if the key doesn’t exist.
print(karnataka_food.get("Mysuru","Not found"))
# dict() command 
karnataka_food = dict(
    Bengaluru = "Bisi Bele Bath", 
    Mysuru = "Mysore Pak", 
    Mangaluru = "Neer Dosa"
)
print(karnataka_food["Bengaluru"])

#Adding and Updating Dictionary Elements
karnataka_food["Shivamogga"] = "Kadubu"
print(karnataka_food)
