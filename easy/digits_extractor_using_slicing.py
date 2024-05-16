# displaying the last digit of the string first, one digit at a time
# using slicing
num = input('Enter a number: ') # input is a string even though it is a number
for digit in num[::-1]: 
    print(digit, end=" ")
    