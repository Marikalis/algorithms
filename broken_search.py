# ID 65365571
def broken_search(nums, target) -> int: 
    left = 0 
    right = len(nums) - 1 
    while left <= right:
        nums_left = nums[left]
        if nums_left == target:
            return left
        middle = left + (right - left) // 2 
        nums_middle = nums[middle]
        if nums_middle == target: 
            return middle
        if (
            (nums_left < target or nums_left == target) and (
                target < nums_middle or nums_middle < nums_left
            )
        ) or (
            target < nums_middle < nums_left):
            right = middle
        else:
            left = middle + 1  
    return -1
