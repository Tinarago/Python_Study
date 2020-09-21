# Element adding or editing is not allowed
# faster than the List

menu = ("Sushi", "California Roll")
print(menu[0])
print(menu[1])

# AttributeError: 'tuple' object has no attribute 'add'
# menu.add("Grape")

# 
name = "Tina"
age = 100
hobby = "coding"
print(name, age, hobby)

(name, age, hobby) = ("Tina", 200, "coding")
print(name, age, hobby)
