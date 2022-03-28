###To find the no.of ways to achieve the given sum

# def solve(n,s):
#     if n==0:
#         return 0
#     elif s==0:
#         return 1
#     else:
#         if coins[n-1]>s:
#             return solve(n-1,s)
#         else:
#             return solve(n,s-coins[n-1])+solve(n-1,s)


# def solve(n,s):
#     if n==0:
#         return 0
#     elif s==0:
#         return 1
#     if dp[n][s]!=-1:
#         return dp[n][s]
#     else:
#         if coins[n-1]>s:
#             dp[n][s]=solve(n-1,s)
#             return dp[n][s]
#         else:
#             dp[n][s]=solve(n,s-coins[n-1])+solve(n-1,s)
#             return dp[n][s]

def solve(n,s):
    dp=[[0 for j in range(s+1)]for i in range(n+1)]
    for i in range(0,n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,s+1):
            if coins[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] + dp[i][j-coins[i-1]]
    return dp[n][s]
    
coins=[2,5,3,6]
s=10
# dp=[[-1 for j in range(s+1)]for i in range(len(coins)+1)]
print(solve(4,10))
