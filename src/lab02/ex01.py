def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError()
    
    minV = nums[0]
    maxV = nums[0]
    for x in nums[1:]:
        if x < minV:
            minV = x
        if x > maxV:
            maxV = x
            
    return minV, maxV

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    un = []
    for x in nums:
        if x not in un:
            un.append(x)
            
    n = len(un)
    for i1 in range(n):
        for i2 in range(i1 + 1, n):
            if un[i1] > un[i2]:
                un[i1], un[i2] = un[i2],  un[i1]
    
    return un

def flatten(mat: list[list | tuple]) -> list:
    if not isinstance(mat, (list, tuple)):
        raise TypeError()
    
    r = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError()
        for i in row:
            r.append(i)
            
    return r


#1 min_max
# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# print(min_max([1.5, 2, 2.0, -3.1]))
# print(min_max([]))

#2 unique_sorted
# print(unique_sorted([3, 1, 2, 1, 3]))
# print(unique_sorted([]))
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

#3 flatten
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))