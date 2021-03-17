num = int(input("Enter Number:"))
fact = 1
if num < 0:
    print("negative number")
elif num == 0:
    print("number is zero")
else:
    for i in range(1, num+1):
        fact = fact*i
    print("factorial is:", fact, "of no", num)
