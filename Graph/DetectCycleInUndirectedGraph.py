def isCycle(self, V, adj):
		#Code here
		def helper(s,parent):
		    vis[s]=True
		    for i in adj[s]:
		        if vis[i]==False:
		            if helper(i,s)==True:
		                return True
		        elif i!=parent:
		            return True
		    return False
		
		
		vis=[False for i in range(V)]
		for i in range(V):
		    if vis[i]==False:
		        if helper(i,-1)==True:
		            return True
		return False
