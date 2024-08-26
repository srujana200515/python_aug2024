#Program to reverse a number
input_number=int(input("Enter the number to reverse:"))
reversed_num=0
while input_number!=0:
    digit=input_number % 10
    reversed_num=reversed_num * 10 + digit
    input_number //= 10
print("the reversed number is :",reversed_num)
