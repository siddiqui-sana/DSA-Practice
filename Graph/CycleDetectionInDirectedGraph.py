class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        def helper(s):
            vis[s]=True
            recst[s]=True
            for ad in adj[s]:
                if vis[ad]==False and helper(ad):
                    return True
                elif recst[ad]==True:
                    return True
            recst[s]=False
            return False
        
        vis=[False for i in range(V)]
        recst=[False for i in range(V)]
        for i in range(V):
            if vis[i]==False:
                if helper(i)==True:
                    return True
                    
        return False
      
      ##adj=[[]] List of list where each sublist is the adjacency list for the vertex (index)
