absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("Today's done. {0} doesn't have a book".format(student))
        break
    print("{0}, Read a book".format(student))
