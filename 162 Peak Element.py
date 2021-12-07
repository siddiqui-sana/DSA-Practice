# O(logn)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        beg=0
        end=len(nums)-1
        if len(nums)==1:
            return 0
        while(beg<=end):
            mid=(beg+end)//2
            
            if mid==0:
                if nums[0]>nums[mid+1]:
                    return mid
                else:
                    beg=mid+1
            if mid==len(nums)-1:
                if nums[mid]>nums[mid-1]:
                    return mid
                else:
                    end=mid-1
            if beg==end:
                return beg
            
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]<nums[mid]<nums[mid+1]:
                beg=mid+1
            else:
                end=mid-1
     
