'''Program to print the Equi Lateral Triangle of N lines
    *
   ***
  *****
 *******
********* '''
input_rows=int(input("Enter the number of rows:"))
for i in range(input_rows):
    
    for j in range(input_rows - i - 1):
        print(" ", end="")
   
    for k in range(2 * i + 1):
        print("*", end="")
   
    print()