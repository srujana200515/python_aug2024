#Find Nth Fibo term (assume 1 and 2 as 1st 2 terms)
def fibonacci(input_num):
    if input_num == 1:
        return 1
    elif input_num == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(3, input_num + 1):
            a, b = b, a + b
        return b
    

# Example usage:
input_num=int(input('Enter the number to find fibonacci:'))
print(f"The {input_num}th Fibonacci term is: {fibonacci(input_num)}")
