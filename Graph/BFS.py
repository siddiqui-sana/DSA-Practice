from queue import Queue
def bfsOfGraph(V, adj):
    # code here
    visited=[False for i in range(V)]
    ans=[]
    q=Queue()
    q.put(0)
    visited[0]=True
    while q.empty()==False:
        x=q.get()
        ans.append(x)
        adj_nodes=adj[x]
        for i in adj_nodes:
            if visited[i]==False:
                q.put(i)
                visited[i]=True
    return ans
    
V,E=map(int,input().split())
# V=int(input())
# E=int(input())
adj=[[] for i in range(V)]
for i in range(E):
    u,v=map(int,input().split())
    # u=int(input())
    # v=int(input())
    adj[u].append(v)
ans=bfsOfGraph(V,adj)
for i in ans:
    print(i,end='')


  
  
