arr = [-10,-3,5,6,-2]

arr.sort()

prod1 = arr[0] * arr[1]
prod2 = arr[-1] * arr[-2]

print(max(prod1, prod2))

# TC = O(n log n)
# SC = O(1)