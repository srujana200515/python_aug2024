#Assume 1 and 2 are 1st 2 terms of the series and print the 1st N term of Fibo series (HemaChandra numbers)
def hemaChandra_series(n):
    a, b = 1, 2
    series = [a, b]
    
   
    for _ in range(2, n):
        a, b = b, a + b
        series.append(b)
    
    return series

N = int(input("Enter the number of terms: "))
print("HemaChandra series:", hemaChandra_series(N))
