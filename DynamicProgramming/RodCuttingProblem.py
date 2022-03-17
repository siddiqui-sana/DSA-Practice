class Solution:
    def cutRod(self, price, n):
        #code here
        ###Tabulation
        dp=[[0 for j in range(n+1)]for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i<=j:
                    dp[i][j]=max(price[i-1]+dp[i][j-i],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][n]
                
        ###Memoization
        # def helper(i,N):
        #     if i==0 or N==0:
        #         return 0
        #     if dp[i][N]!=-1:
        #         return dp[i][N]
                
        #     else:
        #         if i<=N:
        #             dp[i][N]=max((price[i-1]+helper(i,N-i)),helper(i-1,N))
        #             return dp[i][N]
        #         else:
        #             dp[i][N]=helper(i-1,N)
        #             return dp[i][N]
        
        # dp=[[-1 for j in range(n+1)]for i in range(n+1)]
        # helper(n,n)
        # ##return helper(n,n)
        # return dp[n][n]
