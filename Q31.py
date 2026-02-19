arr = [1,3,5,2,2]

total = sum(arr)
left = 0

for i in range(len(arr)):
    total -= arr[i]
    if left == total:
        print(i)
        break
    left += arr[i]
# TC= O(n)
# SC= O(1)