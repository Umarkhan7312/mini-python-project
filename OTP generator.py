import random

otp = ""

try:
    for i in range(int(input())):
        x = random.randint(0,9)
        otp = otp + str(x)
    print(f"Your one time password OTP : {otp}")

except Exception as e:
    print("enter int")
    print(e)
