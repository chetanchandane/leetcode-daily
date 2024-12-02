def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    min_diff = float('inf')
    
    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1
        
        while j < k:
            totSum = nums[i] + nums[j] + nums[k]
            diffSum = abs(totSum - target)
            
            # Update closest_sum and min_diff if a closer sum is found
            if diffSum < min_diff:
                min_diff = diffSum
                closest_sum = totSum
            
            # Move pointers based on comparison with the target
            if totSum < target:
                j += 1
            elif totSum > target:
        