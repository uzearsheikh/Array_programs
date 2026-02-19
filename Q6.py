arr = [1,2,3,4,5]
flag = True
n = len(arr)

for i in range(n-1):
    if arr[i] > arr[i+1]:
        flag = False
        continue
    else:
        flag = True

print(flag)


# TC = O(n)
# SC = O(1)