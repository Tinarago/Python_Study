for waiting_num in [0, 1, 2, 3, 4]:
    print("waiting: {0}".format(waiting_num))

for waiting_num2 in range(1,6):
    print("waiting: {0}".format(waiting_num2))

starbucks = ["Ironman", "Thor", "groot"]
for customer in starbucks:
    print("{0}, your coffee's reddy".format(customer))

# for loop in single line
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

# 
students = ["Iron Man", "Thor", "Groot"]
students = [len(i) for i in students]
print(students)

# 
students = ["Iron Man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)