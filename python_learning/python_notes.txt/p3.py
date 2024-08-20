# Accept a number as input, say X and define a logic to get the output say Y. The input can only be 0 or 1 and the output must be 1 if input is 0 and viceversa. Do not use Boolean Algebra

X=int(input('Enter the input number (0 and 1 only): '))
Y=1-X
# check if the input is valid 
if X==0 or X==1:
    print('The output is (Y)',Y)
else:
    print('Invalid input. please Enter the valid input(0 and 1 only)')
