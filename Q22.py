arr = [1,2,3]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        print(arr[i:j+1])

# TC=O(n²)
# SC=O(1)