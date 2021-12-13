from collections import deque
class Solution:
    def canFinish(self, numCourses: int, edges: List[List[int]]) -> bool:
        graph={}
        for i in range(numCourses):
            graph[i]=[]
        in_degree={}
        for i in range(numCourses):
            in_degree[i]=0
        ordering=[]
        for edge in edges:
            p=edge[1]
            c=edge[0]
            graph[p].append(c)
            in_degree[c] += 1
        
        Q=deque()
        ordering=[]
        for key,value in in_degree.items():
            if value==0:
                Q.append(key)
        while(Q):
            node=Q.popleft()
            ordering.append(node)
            for nbr in graph[node]:
                in_degree[nbr] -= 1
                if in_degree[nbr]==0:
                    Q.append(nbr)
        if len(ordering)==numCourses:
            return True
        else:
            return False
