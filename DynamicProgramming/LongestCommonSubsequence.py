def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[0 for j in range(m+1)]for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
                    
        
        
        # def check(n,m):
        #     if n==0 or m==0:
        #         return 0
        #     if dp[n][m]!=-1:
        #         return dp[n][m]
        #     else:
        #         if text1[n-1]==text2[m-1]:
        #             dp[n][m]=1+check(n-1,m-1)
        #             return dp[n][m]
        #         else:
        #             dp[n][m]=max(check(n-1,m),check(n,m-1))
        #             return dp[n][m]
        # n=len(text1)
        # m=len(text2)
        # dp=[[-1 for j in range(m+1)]for i in range(n+1)]
        # return check(len(text1),len(text2))
