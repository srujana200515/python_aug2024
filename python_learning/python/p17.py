#Program to Find Odd(Even) placed digits in a number
input_number = int(input("Enter the number to find odd(even) placed digits in a number:"))
number_str = str(input_number)


for i in range(len(number_str)):
    digit = number_str[i]
    if (i % 2) == 0:
        print(f"Digit {digit} at position {i+1} is Even placed")
    else:
        print(f"Digit {digit} at position {i+1} is Odd  placed")
