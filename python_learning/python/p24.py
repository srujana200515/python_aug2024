#Check if a number is Prime
input_number=int(input("Enter a number to check if it is a prime:"))
def is_prime(input_number):
    if input_number<= 1:
        return False
    for i in range(2, int(input_number**0.5) + 1):
        if input_number % i == 0:
            return False
    return True


if is_prime(input_number):
    print(f"{input_number} is a prime number")
else:
    print(f"{input_number} is not a prime number")


