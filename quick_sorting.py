# First, we pick the pivot.
array = [98, 3, 72, 56, 89, 12, 41, 67, 23, 1, 
         95, 83, 11, 47, 34, 28, 79, 64, 50, 9,
         102, 45, 38, 76, 88, 24, 92, 81, 15, 61, 
         110, 5, 99, 31, 18, 70, 55, 42, 26, 8]

def quicksort(array):
    if len(array) <= 1: #u sptuid
        return array

    n = len(array)
    p = array[n//2] 

    small = []
    big = []
    
    for i in range(n):
        if array[i] < p:
            small.append(array[i])
        elif array[i] > p:
            big.append(array[i])

    return quicksort(small) + [p] + quicksort(big)


newarray = quicksort(array)

print("Sorted Array:", newarray)
