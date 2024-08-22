#Program to find 2nd smallest digit in a number
input_number = int(input('Enter a number to find 2nd smallest digit in it: '))

temp_number = input_number
small_digit = 9
smallest_digit = 9
while input_number != 0:
    digit = input_number % 10 # fetch last digit
    input_number = input_number // 10 #remove last digit
    if smallest_digit > digit:
        small_digit = smallest_digit
        smallest_digit = digit
    elif digit < small_digit:
        small_digit = digit
print(f'2nd smallest digit in {temp_number} is {small_digit}')







