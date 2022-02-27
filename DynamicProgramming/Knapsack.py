
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
###'''Top Down Approach'''###     
        t=[[0 for j in range(W+1)]for i in range(n+1)]
        # for i in range(n+1):
        #     for j in range(W+1):
        #         if i==0 or j==0:
        #             t[i][j]=0
                    
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    t[i][j]=max((val[i-1]+t[i-1][j-wt[i-1]]),(t[i-1][j]))
                else:
                    t[i][j]=t[i-1][j]
        return t[n][W]
        
        # code here
####'''Memoized Version'''####
        # def helper(W,wt,val,n):
        #     if n==0 or W==0:
        #         return 0
            
        #     else:
        #         if t[n][W] != -1:
        #             return t[n][W]
        #         else:
                    
        #             if wt[n-1]<=W:
        #                 t[n][W]=max((val[n-1]+helper(W-wt[n-1],wt,val,n-1)),helper(W,wt,val,n-1))
        #                 return t[n][W]
        #             else:
        #                 t[n][W]=helper(W,wt,val,n-1)
        #                 return t[n][W]
        
        # t=[[-1 for j in range(W+1)]for i in range(n+1)]
        
        # helper(W,wt,val,n)
        # return t[n][W]
