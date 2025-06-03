array = [2, 4, 23, 54, 75, 234, 46, 2] 
n = len(array)

for i in range(n-1):
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)
