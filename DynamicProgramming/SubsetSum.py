class Solution:
    def isSubsetSum (self, N, arr, s):
        ##TOP DOWN APPROACH###
        t=[[False for j in range(s+1)] for i in range(N+1)]
        for i in range(N+1):
            t[i][0]=True
        
        for i in range(1,N+1):
            for j in range(1,s+1):
                if arr[i-1]>j:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
        
        return t[N][s]
            
        
        ##Memoization
        # def helper(N,s):
        #     if N<=0:
        #         return 0
        #     if s==0:
        #         return 1
        #     else:
        #         if t[N][s]!=-1:
        #             return t[N][s]
        #         else:
        #             if arr[N-1]>s:
        #                 t[N][s]=helper(N-1,s)
        #                 return t[N][s]
        #             else:
        #                 t[N][s]=(helper(N-1,s-arr[N-1]) or helper(N-1,s))
        #                 return t[N][s]
        # t=[[-1 for j in range(s+1)]for i in range(N+1)]
        # return helper(N,s)
        
        
        # # return t[N][s]
        # Recursive Approach
        # def helper(N,s):
        #     if N==0:
        #         return False
        #     if s==0:
        #         return True
            
        #     if arr[N-1]>s:
        #         return helper(N-1,s)
        #     else:
        #         return helper(N-1,s-arr[N-1]) or helper(N-1,s)
        
        # return helper(N,s)
