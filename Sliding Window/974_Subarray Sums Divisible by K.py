class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        D={}
        D[0]=1
        s=0
        c=0
        for i in range(len(nums)):
            s=s+nums[i]
            if s%k not in D:
                D[s%k] = 1
            else:
                c += D[s%k]
                D[s%k] += 1
        return c 
