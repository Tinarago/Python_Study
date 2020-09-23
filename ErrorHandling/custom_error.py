class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
        

try:
    print("<Single digit division Calculator>")
    num1 = int(input("First num : "))
    num2 = int(input("Second num : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("input {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("Invalid input. Only single digit is allowed")
except BigNumberError as err:
    print("Big Number error occurred. only single digit allowed")
    print(err)
finally: # 무조건 실행. 프로그램 에러가 발생해서 프로그램이 중단되어도 실행됨
    print("Thank you for using this calculator")