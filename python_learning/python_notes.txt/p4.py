# Program to Accept 3 distinct numbers and find smallest among them.

num1 =int(input('Enter the  first distinct numbers to find smallest among them:'))
num2 =int(input('Enter the  second distinct numbers to find smallest among them:'))
num3 =int(input('Enter the  third distinct numbers to find smallest among them:'))

if num1< num2 and  num1<num3:
    print('The smallest number among the three distinct number is:',num1)

elif  num2<num3:
     print('The smallest number among the three distinct number is:',num2)
else:
     print('The smallest number among the three distinct number is:',num3)
    
    