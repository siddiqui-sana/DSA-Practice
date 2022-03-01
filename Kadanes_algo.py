class Solution(object):
    def maxSubArray(self, nums):
        max_sum=float('-inf')
        cur_sum=0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum>max_sum:
                max_sum = cur_sum
            if cur_sum<0:
                cur_sum = 0
        return max_sum
