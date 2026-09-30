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