#Find the Nth Prime number
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(input_num):
    count = 0
    num = 1
    while count < input_num:
        num += 1
        if is_prime(num):
            count += 1
    return num


input_num = int(input("Enter the value of N: "))
print(f"The {input_num}th prime number is {nth_prime(input_num)}")
