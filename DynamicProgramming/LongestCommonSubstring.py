def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        dp=[[0 for j in range(m+1)]for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if S1[i-1]==S2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=0  #When we don't find chars equal simply make that cell 0
        mx=0
        for i in range(n+1):
            m=max(dp[i])
            mx=max(mx,m)
        return mx
