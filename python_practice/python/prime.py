# check prime no between interval
lower = int(input("enter lower no:"))
upper = int(input("enter upper no:"))

for num in range(lower, upper +1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# check enter no is prime or not
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")