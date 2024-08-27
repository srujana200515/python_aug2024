#Program to Print X shape inside Hollow Square
def print_hollow_square(size):
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

size = int(input("Enter the size of the hollow square: "))
print_hollow_square(size)
