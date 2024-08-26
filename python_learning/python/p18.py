#Program to Find Odd placed Even digits in a number
input_number = int(input("Enter the number to find odd placed even digits: "))
number_str = str(input_number)

# Loop through the digits and their positions
for i in range(len(number_str)):
    digit = int(number_str[i])
    if (i % 2) != 0 and (digit % 2) == 0:
        print(f"Digit {digit} at position {i+1} is an Even digit placed at an even position")
    elif (i+1 % 2) != 0 and (digit % 2) == 0:
        print(f"Digit {digit} at position {i+1} is an Even digit placed at an odd position")
