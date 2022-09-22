x = int((input('Enter a number ')))
y = int((input('Enter another number ')))
method = input('addition or subtraction or multiplication or division or remainder : ')
addition = x +y
subtraction = x -y
multiplication = x * y
division = x / y
remainder = x % y
if(method) == "addition":
    print(addition)
elif(method) == "subtraction":
    print(subtraction)
elif(method) == "multiplication":
    print(multiplication)
elif(method) == "division":
    print(division)
elif(method) == "remainder":
    print(remainder)    
