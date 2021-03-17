# nterms = int(input("How many terms? "))
# n1, n2 = 0, 1
# count = 0
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1

nth = int(input("No of terms: "))
n1, n2 = 0, 1
count = 0
if nth <= 0:
    print("Enter positive no")
elif nth == 1:
    print("fibonacci number for 1 no is:")
    print(n1)
else:
    print("fibonacci no for terms are:")
    while count < nth:
        print(n1)
        nthh = n1 + n2
        n1 = n2
        n2 = nthh
        count += 1

