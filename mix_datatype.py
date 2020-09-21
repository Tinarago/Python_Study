# set type creation
menu = {"coffee", "milk", "juice"}
print(menu, type(menu))

# change to List []
menu = list(menu)
print(menu, type(menu))

# change to tuple ()
menu = tuple(menu)
print(menu, type(menu))

# change back to set {}
menu = set(menu)
print(menu, type(menu))