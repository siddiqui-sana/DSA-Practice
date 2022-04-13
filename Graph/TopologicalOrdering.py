from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        Q=deque()
        d={}    # Dictionary to hold indegree of each node
        res=[]
        for i in range(V):
            d[i]=0  #Initializing the indegree of each vertex as zero
        for i in range(V):
            chl=adj[i]  # Adjacency list coresponding to node i
            for child in chl:
                d[child] += 1   # Calculating the indegree of nodes
        # print(d)
        for vertex,indegree in d.items():
            if indegree==0:
                Q.append(vertex)    #Filling the queue with nodes whose indegree is 0
        while(len(Q)!=0):   
            node=Q.popleft()
            res.append(node)
            for c in adj[node]: # When a job is done the we will reduce the dependency ie indegree of each of its neighbor by 1
                d[c] -= 1
                if d[c]==0:
                    Q.append(c) # We append in queue only those vertex whose indegree is 0.
        return res
