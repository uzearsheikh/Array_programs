arr = [1,2,2,3,1,4]

seen = set()
res = []

for i in arr:
    if i not in seen:
        res.append(i)
        seen.add(i)

print(res)

# TC = o(n)
# SC: = O(n)