a = [1,2,3,4]
b = [3,4,5,6]

s = set(b)
res = []

for i in a:
    if i in s:
        res.append(i)

print(res)
# TC: O(n+m)
# SC: O(m)