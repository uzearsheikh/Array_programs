
def second_largest(arr):
    arr.sort()
    return arr[-2]

print(second_largest([10,20,4,45,99]))


# O(nlogn)
# O(1) due to inplace sorting no extra space is allowed