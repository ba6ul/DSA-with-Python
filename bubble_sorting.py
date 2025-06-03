# -------------------- Bubble Sort Explanation --------------------
# Bubble Sort is a simple sorting algorithm that repeatedly compares adjacent elements
# and swaps them if they are in the wrong order. This process continues until the array
# becomes sorted.

#
# 🔹 Time Complexity:
# - Worst & Average Case: O(n²) → Due to nested loops.
# - Best Case: O(n) → If the array is already sorted (optimized version).
# - Space Complexity: O(1) → Works in-place (no extra space required).
#
# -------------------- Bubble Sort Implementation --------------------
array = [2, 4, 23, 54, 75, 234, 46, 2] 
n = len(array)-1

for i in range(n):
    for j in range(n-i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)
