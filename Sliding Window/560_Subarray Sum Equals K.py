#O(n) Space and time Complexity
# Maintain a frequency map as {prefix_Sum:frequency of this prefix sum}
# While looping the array:
#0. hash_map[current_prefix_sum] += 1
#1. If (current_prefix_sum - k) exists in the map, it means there is a subarray found hence  increment the counter.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        D={}
        D[0]=1
        s=0
        c=0
        for i in range(len(nums)):
            s=s+nums[i]
            if s-k in D:
                c += D[s-k]
            if s in D:
                D[s] += 1
            else:
                D[s]=1
                
        return c 
