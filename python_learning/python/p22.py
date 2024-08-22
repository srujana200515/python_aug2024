#Program to print a Hollow Square of N lines
number_of_lines=int(input('Enter the number of lines to draw a hollow square:'))
for i in range(1,number_of_lines+1):
    for j in range (1,number_of_lines+1):
        if i==1 or i==number_of_lines or j==1 or j==number_of_lines:
            print(" * ", end=" ")
        else:
            print("   ",end=" ")
    print()