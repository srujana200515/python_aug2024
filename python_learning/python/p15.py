 #Program to find Sum of even(odd) digits in a number.
number=int(input("Enter the  range numbers to find the sum of even(odd):"))
even_sum=0
odd_sum=0
for i in range (0,number,2):
        even_sum+=i
print("The sum of even number",even_sum)
for i in range (1,number,2):
        odd_sum+=i
        
print("The sum of odd number",odd_sum)