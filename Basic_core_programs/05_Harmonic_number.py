def harmonic_number(n):
    if n == 0:
        return print("N must be greater than zero")
    
    sum_harmonic = 0
    for i in range(1, n + 1):
        sum_harmonic += 1 / i
    
    return sum_harmonic

N = int(input("Enter the value of N: "))
print("The", N, "th Harmonic Number is:", harmonic_number(N))