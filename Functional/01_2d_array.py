def read_2d_array(rows, cols):
    array = []
    print(f"Enter {rows * cols} elements row-wise:")
    for i in range(rows):
        row = list(map(str, input().split()))
        array.append(row)
    return array

def print_2d_array(array):
    print("2D Array:")
    for row in array:
        print(" ".join(row))

M = int(input("Enter number of rows (M): "))
N = int(input("Enter number of columns (N): "))

matrix = read_2d_array(M, N)
print_2d_array(matrix)
