arr = [7,1,5,3,6,4]

min_val = arr[0]
max_diff = 0

for i in range(1, len(arr)):
    if arr[i] < min_val:
        min_val = arr[i]
    else:
        max_diff = max(max_diff, arr[i] - min_val)

print(max_diff)

# TC = O(n)
# SC = O(1)