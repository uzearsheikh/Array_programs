arr = [1,2,3,4,5,6]
arr.sort()

res = []
l = 0
r = len(arr) - 1

while l <= r:
    if l != r:
        res.append(arr[r])
        res.append(arr[l])
    else:
        res.append(arr[l])
    l += 1
    r -= 1

print(res)
# TC = O(n log n)
# SC = O(n)