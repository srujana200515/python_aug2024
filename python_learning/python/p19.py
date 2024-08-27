#Program to print the Right angled Triangle of N lines
input_number = int(input("Enter a number to print the rows of triangle:"))
for i in range(0,input_number):
    for j in range(0,i+1):
        print("*",end=' ')
    print("\r")
