arr = [1,2,3,4,5]
k = 2
n = len(arr)

k = k % n

arr[:] = arr[k:] + arr[:k]

print(arr)

# TC = O(n)
# SC = O(n)