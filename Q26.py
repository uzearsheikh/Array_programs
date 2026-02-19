arr = [1,2,3,1]

for i in range(len(arr)):
    if (i == 0 or arr[i] > arr[i-1]) and (i == len(arr)-1 or arr[i] > arr[i+1]):
        print(arr[i])
        break
# TC=O(n)
# SC = O(1)

