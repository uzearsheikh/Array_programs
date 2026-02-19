a = [1,2,3]
b = [3,4,5]

res = set()

for i in a:
    res.add(i)

for i in b:
    res.add(i)

print(list(res))

# TC: O(n+m)
# SC: O(n+m)