try:
    print("<Single digit division Calculator>")
    num1 = int(input("First num : "))
    num2 = int(input("Second num : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("Invalid input. Only single digit is allowed")