##Lint Code: 515

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, cost: List[List[int]]) -> int:
        # write your code here
        n=len(cost)
        if n==0:
            return 0
        else:

            for i in range(1,n):
                cost[i][0]=cost[i][0]+min(cost[i-1][1],cost[i-1][2])
                cost[i][1]=cost[i][1]+min(cost[i-1][0],cost[i-1][2])
                cost[i][2]=cost[i][2]+min(cost[i-1][0],cost[i-1][1])
            print(cost)
            return min(cost[n-1])
