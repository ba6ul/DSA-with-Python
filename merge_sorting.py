# I DON'T KNOW WHY IT'S NAMED MERGE SORT, WHEN IN ACTUALITY, IT'S DIVIDE SORT FIRST.

# -------------------- Merge Sort Explanation --------------------
# Merge Sort is a divide-and-conquer sorting algorithm that recursively splits the array 
# into smaller halves, sorts them, and then merges them back together in sorted order.
# This ensures an efficient and stable sorting mechanism.

# 🔹 Time Complexity:
# - Worst, Best & Average Case: O(n log n) → Consistent efficiency across all cases.
# - Space Complexity: O(n) → Requires additional memory for merging sorted halves.

# -------------------- Merge Sort Implementation --------------------

array = [98, 3, 72, 56, 89, 12, 41, 67, 23, 1, 
         95, 83, 11, 47, 34, 28, 79, 64, 50, 9,
         102, 45, 38, 76, 88, 24, 92, 81, 15, 61, 
         110, 5, 99, 31, 18, 70, 55, 42, 26, 8]

def merge_sort(array):

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge_rule(left_half, right_half)

# Combing the array based on rules
def merge_rule(left, right):
    result = []
    i, j = 0, 0

    # Rule
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


sorted_array = merge_sort(array)
print("Original Array:\n", array)
print("\nSorted Array:\n", sorted_array)
