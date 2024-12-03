def fourSum(nums, target):
    nums.sort()
    out = []
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            k, m = j+1, len(nums) - 1 
            while k < m:
                sum4 = nums[i] + nums[j] +nums[k]+nums[m]

                if sum4 == target:
                    out.append([nums[i], nums[j], nums[k], nums[m]])
                    while k < m and nums[k] == nums[k+1]:
                        k+=1
                    while k < m and nums[m] == nums[m-1]:
                        m-=1
                    k += 1
                    m -= 1
                elif sum4 < target:
                    k += 1
                else: m-=1                    
    return out                    



                


print(fourSum([1,2,3,4,5,6], 13))
