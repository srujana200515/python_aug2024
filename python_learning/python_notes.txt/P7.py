#program to check if a number is perfect square
number=int(input("Enter the number"))
i=1
while number> 0:
    number-= i
    i+=2
if number == 0:
    print("The number is a perfect square.")