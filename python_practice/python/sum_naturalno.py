# Natural Numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9,…..}
# Whole Numbers = {0, 1, 2, 3, 4, 5, 7, 8, 9,….}


num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    # use while loop to iterate un till zero
    while (num > 0):
        sum += num
        num -= 1
    print("The sum is", sum)