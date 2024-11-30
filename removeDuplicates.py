
def removeDuplicates(nums):
    if len(nums)<2:
        return len(nums)
    if len(nums)>1:
        ans = {}
        k = 0
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans[nums[i]] = 1
                k += 1
                # print(k)
            else:
                ans[nums[i]] += 1
        for i in range(len(nums)):
            nums.pop()  


        for i, (key, value) in enumerate(ans.items()):
            nums.append(key)
        print(nums)
        return k
    
print(removeDuplicates([1,1,2,3,3]))




        