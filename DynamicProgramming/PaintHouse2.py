###Lint Code 516

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, cost):
        # write your code here
        if len(cost)==0:
            return 0
        if len(cost)==1:
            return cost[0][0]
        else:
            n=len(cost)
            k=len(cost[0])
            l=sorted(cost[0])
            mn=l[0]
            second_mn=l[1]    
            for i in range(1,len(cost)):
                for j in range(0,k):
                    if cost[i-1][j]==mn:
                        cost[i][j] += second_mn
                    else:
                        cost[i][j] += mn
                
                l=sorted(cost[i])   ##To find the least and second least cost.
                mn=l[0]
                second_mn=l[1]    
            return min(cost[n-1])
                    
##### Instead of using loop to find minimum cost of previous row, we just use two variables to reduce the complexity. We maintain 'min' and 'second_min' to store the minimum
##### and second minimum cost pf previous row.
##### Intution behind maintaing the least and second least cost is: If the least cost happens to be of same color of which we want to color the next house(row), then we will take second least cost. Otherwise least cost.
