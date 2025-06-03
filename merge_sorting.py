#I DON'T KNOW WHY IT'S NAMED MERGE SORT, WHEN IN ACTUALITY, IT'S DIVIDE SORT FIRST.
array = [2, 4, 23, 54, 75, 234, 46, 2] 

n = len(array)
mid = n//2

left_half = array[:mid]
right_half = array[mid:]

print(left_half,right_half)

