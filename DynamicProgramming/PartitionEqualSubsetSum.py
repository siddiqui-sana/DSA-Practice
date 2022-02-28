class Solution:
    def canPartition(self, num: List[int]) -> bool:
        
            ## Function for subset sum problem
            def helper(N,S):
                
                dp=[[False for j in range(S+1)] for i in range(N+1)]
                for i in range(N+1):
                    dp[i][0]=True
                
                for i in range(1,N+1):
                    for j in range(1,S+1):
                        if num[i-1]>j:
                            dp[i][j]=dp[i-1][j]
                        else:
                            dp[i][j]=dp[i-1][j] or dp[i-1][j-num[i-1]]
                return dp[N][S]
                    
            s=sum(num)
            if s%2!=0:      #If total sum is odd then equal subset sum isn't possible anyway
                return False
            else:
                ss=s//2
                ## We need to now just find out if there exists a subset whose sum is equal to ss i.e. half of total sum
                return helper(len(num),ss)
