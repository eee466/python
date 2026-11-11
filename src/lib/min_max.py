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