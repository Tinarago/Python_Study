# {key:value}

cabinet = {3:"Tina", 100:"Heidi"}

print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

# error calling
# print(cabinet[5]) #error
print(cabinet.get(5)) # print none
print(cabinet.get(5, "enable"))

# find in dictionary
print(3 in cabinet) # True
print(7 in cabinet) # False

# String type key
cabinet2 = {"A-3":"Ivan", "B-100": "Long"}
print(cabinet2["A-3"])
print(cabinet2.get("B-100"))

# add new element
cabinet2["C-20"] = "New one"

# update
cabinet2["A-3"] = "another one"
print(cabinet2)

# delete
del cabinet2["A-3"]
print(cabinet2)

# print items
print(cabinet2.keys())
print(cabinet2.values())
print(cabinet2.items())

# clear the dictionary
cabinet2.clear()
print(cabinet2)