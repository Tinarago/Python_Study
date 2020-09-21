# while

customer = "IronMan"
index = 5
while index >= 1:
    print("{0}, coffee's reddy. {1} times left".format(customer, index))
    index -= 1
    if index == 0:
        print("Coffee's gone...")
    

# infinite loop
# customer = "Thor"
# index = 1
# while True:
#     print("{0}, coffee's reddy. {1} left".format(customer, index))
#     index += 1

customer = "Thor"
person = "Unknown"
while person != customer:
    print("{0}, coffee's reddy".format(customer))
    person = input("What's your name?>")