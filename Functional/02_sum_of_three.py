def triplets(arr, n):
    triplets = []
    count = 0
    
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = sorted([arr[i], arr[j], arr[k]])
                    if triplet not in triplets:  # Ensure distinct triplets
                        triplets.append(triplet)
                        count += 1
    
    print("Number of distinct triplets:", count)
    print("Distinct triplets:", triplets)

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements separated by space: ").split()))

triplets(arr, n)