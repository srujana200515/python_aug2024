#Program to find biggest (smallest) digit in a number
num=int(input("Enter the number to find biggest and smallest digit in it:"))
temp_number =num
largest_digit = 0
smallest_digit= 9
while num:
        digit = num % 10
        if digit > largest_digit :
            largest_digit=digit
          
        elif digit < smallest_digit:
            smallest_digit=digit
        num=num // 10
print(smallest_digit,"is the smallest digit")
print(largest_digit,"is the largest digit")
        
