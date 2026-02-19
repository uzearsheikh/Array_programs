arr = [2,2,1,1,2,2,2]

count = 0
cand = None

for i in arr:
    if count == 0:
        cand = i
    if i == cand:
        count += 1
    else:
        count -= 1

print(cand)

# TC = O(n)
# SC = O(1)