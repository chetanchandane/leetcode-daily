
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j, k = m-1, n-1, m+n-1
    while i>=0 and j>=0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    print(nums1)      
    # while j >=0:


       
        
         

merge([1,2,3,0,0,0,0,0], 3, [2,5,6,7,98], 5)
        
