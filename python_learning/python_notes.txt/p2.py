# Read a Number from the user and check if it is an Even or not


# To read data from the console, we can use input(). However the input() always reads only a string as usual with all the orther Languages.


my_number=int(input('Enter a number to check if it is Even or not : '))
print(type(my_number))

if my_number % 2 ==0:
    print(my_number, 'is a Even')
else:
    print(my_number,'is not a Even')