def missing(arr, n):
    total = n * (n + 1) // 2
    
    sum = 0
    for i in arr:
        sum += i
    
    return total - sum

arr = [1, 2, 4, 5]
n = 5

result = missing(arr, n)
print("Missing number is:", result)

# TC = O(n)
# SC = O(1)
