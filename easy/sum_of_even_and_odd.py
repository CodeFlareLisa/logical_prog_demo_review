# sum of even and odd number
num = int(input('Enter a number: '))
result = 0
while num != 0:
    digit = num % 10
    result = result + digit # add the digit to the result
    num = num // 10
print ('Sum of digits is: ', result)


num = int(input("Enter a number"))
if num <= 0:
    print(num, ' is invalid')
else: 
    if num % 2 == 0:
      print(num, " is even")
    else:
        print(num," is odd")

    