arr = [3,4,-1,1]

s = set(arr)
i = 1

while True:
    if i not in s:
        print(i)
        break
    i += 1
# SC=O(n)
# TC=O(n)