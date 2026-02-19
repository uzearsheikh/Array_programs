arr = [1,2,3,4,5,6,7,88,90]
k = 4
n = len(arr)

k = k % n

arr[:] = arr[n-k:] + arr[:n-k]

print(arr)


# TC = O(n)
# SC = O(n) 