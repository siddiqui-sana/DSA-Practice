def supplyWater(n, k, wells, pipes):
	# Write your code here.
	def findmin(dis,mstset,i,n):
		minval=float('inf')
		minkey=0
		for v in range(n+1):
			if mstset[v]==False and dis[v]<minval:
				minval=dis[v]
				minkey=v
		return minkey
	matrix=[[0 for j in range(n+1)]for i in range(n+1)]
	for i in range(1,n+1):
		matrix[0][i]=wells[i-1]
	for edges in pipes:
		u=edges[0]
		v=edges[1]
		cost=edges[2]
		matrix[u][v]=cost
		matrix[v][u]=cost
		print(v,v,cost)

	print(matrix)
	mstset=[False for i in range(n+1)] 
	dis=[float('inf')for i in range(n+1)]
	dis[0]=0
	for v in range(n+1):
		u=findmin(dis,mstset,v,n)
		mstset[u]=True
		for i in range(n+1):
			if mstset[i]==False and matrix[u][i]!=0 and matrix[u][i]<dis[i]:
				dis[i]=matrix[u][i]
	return sum(dis)

print(supplyWater(3,2,[1,2,2],[[1,2,1],[2,3,1]]))
