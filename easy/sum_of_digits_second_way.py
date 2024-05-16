# 1 character at a time, in the sting, typecast character to integer
num = input('Enter a number: ') # input is a string even though it is a number
result = 0
for i in num:
    result = result + int(i)
   
print ('Sum of digits is: ', result)
    