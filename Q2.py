arr = [4,2,9,1,7]

max = arr[0]
min = arr[0]

for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

print("Max:",max)
print("Min:",min)

# TC = O(n)
# SC = O(1)