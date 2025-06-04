#first we pick pivot.
array = [98, 3, 72, 56, 89, 12, 41, 67, 23, 1, 
         95, 83, 11, 47, 34, 28, 79, 64, 50, 9,
         102, 45, 38, 76, 88, 24, 92, 81, 15, 61, 
         110, 5, 99, 31, 18, 70, 55, 42, 26, 8]
x = len(array)
p = array[x//2] #Middle of the array

print(p)
n = len(array)
small = []
big = []
for i in range (0,n):
    if array[i] < p:
        small.append(array[i])
    else:
        big.append(array[i])

print(small,big)
