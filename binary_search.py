array = [3, 8, 12, 17, 21, 27, 33, 39, 44, 50]

target = 24


high = len(array)
mid = high // 2

if array[mid] < target:
    for i in range(mid,high):
        if array[i] == target:
            print(i)
