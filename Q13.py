arr = [1,2,3,2,4,1,5]

seen = set()
dup = set()

for i in arr:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)

print(list(dup))

# TC=O(n)
# SC= O(n)