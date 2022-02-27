class Solution:
    def fib(self, n: int) -> int:
        
        ##Memoized Code##
        def helper(n):
            if n==0 or n==1:
                dp[n]=n
                return dp[n]
            else:
                if dp[n]!=-1:
                    return dp[n]
                else:
                    dp[n]=helper(n-1)+helper(n-2)
                    return dp[n]
        dp=[-1 for i in range(n+1)]
        helper(n)
        return dp[n]
    
        ## BOTTOM UP approach with space optimization##
        
        # prev1=1
        # prev2=0
        # if n==0:
        #     return prev2
        # if n==1:
        #     return prev1
        # else:
        #     for i in range(2,n+1):
        #         x=prev1+prev2
        #         prev2=prev1
        #         prev1=x
        #     return x
                
