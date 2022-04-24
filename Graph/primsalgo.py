def findMinFromDis(u):
    minval=float('inf')
    minkey=0
    for i in range(V):
        if setmst[i]==False and dis[i]<minval:
            minval=dis[i]
            minkey=i
    return minkey

    return i
def primMST():
    for i in range(V):
        u=findMinFromDis(i)
        setmst[u]=True
        # Relax opeation
        for v in range(V):
            if setmst[v]==False and graph[u][v]>0 and graph[u][v]<dis[v]:
                dis[v]=graph[u][v]
                par[v]=u
V=5
graph= [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
dis=[float('inf') for i in range(V)]
dis[0]=0
print(dis)
par=[None for i in range(V)]
setmst=[False for i in range(V)]
par[0]=-1
primMST()
print(dis)
print(par)
print(setmst)