nums = [3,2,4]
target = 6

def check(nums, target):
    nums.sort()
    l = 0
    r = len(nums) - 1
    
    while l < r:
        current_sum = nums[l] + nums[r]
        
        if current_sum == target:
            return l, r
        elif current_sum < target:
            l += 1
        else:
            r -= 1
    
    return None  

result = check(nums, target)
print(result)
