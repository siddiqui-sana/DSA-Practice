class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        ##findpar with rank compression
        def findpar(x):
            if parent[x]==x:
                return x
            else:
                parent[x]=findpar(parent[x])
                return parent[x]
              
         ##Union by rank
        def union(x,y):
            lp_x=findpar(x)
            lp_y=findpar(y)
            
            if rank[lp_x]>rank[lp_y]:
                parent[lp_y]=lp_x
            elif rank[lp_x]<rank[lp_y]:
                parent[lp_x]=lp_y
            else:
                parent[lp_y]=lp_x
                rank[lp_x] += 1
        # print(adj)
        s=0
        parent=[]
        E={}
        rank=[0 for i in range(V)]
        for i in range(V):
            parent.append(i)
        for i in range(len(adj)):
            edges=adj[i]
            # print(edges)
            for edge in edges:
                u=i
                v=edge[0]
                w=edge[1]
                if (u,v) not in E and (v,u) not in E:
                    E[(u,v)]=w
        # print(E)
        Ef={}
        Ef=sorted(E.items(),key=lambda x:x[1])
        # print(Ef)
        for i in Ef:
            # print(i)
            w=i[1]
            u=i[0][0]
            v=i[0][1]
            # print(u,v,w)
            lp_u=findpar(u)
            lp_v=findpar(v)
            if lp_u!=lp_v:
                union(u,v)
                s += w
        return s
