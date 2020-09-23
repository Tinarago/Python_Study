try: 
    print("Division Calculator")
    nums = []
    nums.append(int(input("First number: ")))
    nums.append(int(input("Second number: ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("Error!! Invalid value!")
except ZeroDivisionError as err:
    print("Error! Can't divide by 0!")
    print(err)
except Exception as err:
    print("Unknown Error occurred")
    print(err)