weather = input("Today's weather?>")
# if 조건:
#     실행 명령문

if weather == "rain" or weather == "snow":
    print("take umbrella")
elif weather == "microdust":
    print("wear mask")
else:
    print("nothing to bring")


temp = int(input("how's the temporature?>"))
if 30 <= temp:
    print("It's too hot")
elif 10 <= temp and temp < 30:
    print("It's good")
elif 0 <= temp and temp < 10:
    print("get a coat")
else:
    print("It's too cold")