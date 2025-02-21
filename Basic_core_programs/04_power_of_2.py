def print_powers_of_two(N):
    print(f"Powers of 2 up to 2^{N}:")
    for i in range(N + 1):
        power_value = 2 ** i
        print(f"2^{i} = {power_value}")

def main():
    N = int(input("Enter a value for N (0 <= N < 31): "))
    if 0 <= N < 31:
        print_powers_of_two(N)
    else:
        print("Please enter a value for N where 0 <= N < 31.")
main()