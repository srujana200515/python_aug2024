#Program to Find count of digits of a number
number=int(input("Enter the number to find its count of digit:"))
count=0
while number>0:
    number//=10
    count+=1
print(f"The count of digit of a number is {count} ")

