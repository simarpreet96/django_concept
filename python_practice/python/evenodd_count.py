# to count even odd no in list
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
even_count=0
odd_count=0

for num in l1:
    if num%2==0:
        even_count += 1
    else:
        odd_count += 1

print("total Even numbers : ", even_count)
print("total Odd numbers : ", odd_count)


# find the no is even or odd

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#     print("{0} is Even number".format(num))
# else:
#     print("{0} is Odd number".format(num))
