"""
isbn.c - San Kwon
This code checks the validity of an inputted ISBN-10 value.
"""

isbn = input("ISBN: ")
while isbn.isdigit() == False:
    isbn = input("Retry: ")

# This part stores the tenth digit
num = int(isbn)
tenthdigit = num % 10
num = num // 10

# This part keeps track of the sum of the first 9 digits
digitsum = 0
for i in range(1, 10):
    digit = num % 10
    digitsum = digitsum + digit * (10 - i)
    num = num // 10

if tenthdigit == digitsum % 11:
    print("YES")
else:
    print("NO")
