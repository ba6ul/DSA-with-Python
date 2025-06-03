array = [98, 3, 72, 56, 89, 12, 41, 67, 23, 1, 
         95, 83, 11, 47, 34, 28, 79, 64, 50, 9,
         102, 45, 38, 76, 88, 24, 92, 81, 15, 61, 
         110, 5, 99, 31, 18, 70, 55, 42, 26, 8]


def insertion_sort(array):
    n = len(array)
    for i in range (1,n):
        selected = array[i]
        j = i -1
        for j in range (i-1,-1,-1):
            if array[j] > selected:
                array[j+1] = array[j]
                x=j
            else:
                break
            array[j] = selected
insertion_sort(array)
print(array)
