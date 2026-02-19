arr = [3,2,2,3]
val = 3

i = 0

while i < len(arr):
    if arr[i] == val:
        arr.pop(i)
    else:
        i += 1

print(arr)

# TC = O(n²) 
# SC = O(1)