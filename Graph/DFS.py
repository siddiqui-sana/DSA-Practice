def dfsOfGraph(V, adj):
    def dfs(node,temp,visited):
        temp.append(node)
        visited[node]=True
        for i in adj[node]:
            if visited[i] is not True:
                dfs(i,temp,visited)
        return temp
    
    visited=[False for i in range(V)]
    res=[]
    for node in range(V):
        if visited[node] is not True:
            temp=[]
            res.extend(dfs(node,temp,visited))
    return res
    
V,E=map(int,input().split())
adj=[[] for i in range(V+1)]
for i in range(E):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
ans=dfsOfGraph(V,adj)
for i in range(len(ans)):
    print(ans[i])
    
