# calculate the sum of digits - store in result
num = int(input('Enter a number: '))
result = 0
while num != 0:
    digit = num % 10
    result = result + digit # add the digit to the result
    num = num // 10
print ('Sum of digits is: ', result)
    

