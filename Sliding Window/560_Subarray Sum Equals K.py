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
