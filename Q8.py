arr = [2,7,11,15]
target = 9

seen = set()

for i in arr:
    if target - i in seen:
        print(i, target - i)
        break
    seen.add(i)



# Tc: O(n)
# Sc: O(n)