class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp=[[0 for j in range(5)] for i in range(n)]
        for i in range(5):
            dp[0][i]=1
            
        for i in range(1,n):
            prev_row_sum=sum(dp[i-1])
            dp[i][0]=prev_row_sum
            for j in range(1,5):
                dp[i][j]=dp[i][j-1]-dp[i-1][j-1]
        
        return sum(dp[n-1])
                
                
                
                
            
