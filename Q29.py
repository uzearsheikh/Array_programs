arr = [100,4,200,1,3,2]

s = set(arr)
longest = 0

for i in s:
    if i-1 not in s:
        length = 1
        while i+length in s:
            length += 1
        longest = max(longest, length)

print(longest)

# TC = O(n)
# SC = O(n)