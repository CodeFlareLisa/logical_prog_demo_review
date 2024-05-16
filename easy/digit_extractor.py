# love the digit extractor!

num = int(input('Enter a number: '))
while num != 0:
    digit = num % 10
    print(digit , end = " ")
    num = num // 10     # integer division
    