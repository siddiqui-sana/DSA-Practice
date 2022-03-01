class Solution:
    def countFriendsPairings(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
            
        # code here 
        dp=[0 for i in range(n+1)]
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+(i-1)*dp[i-2])%(10**9+7)
        
        # print(dp)    
        return dp[n]
