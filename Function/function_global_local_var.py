# local variable
# global variable

gun = 10

def checkpoint(soldiers):
    global gun # global variable use
    gun = gun - soldiers
    print("[in function] gun left: {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[in function] gun left: {0}".format(gun))
    return gun

print("gun in total: {0}".format(gun))
checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("gun left: {0}".format(gun))