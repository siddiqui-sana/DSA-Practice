def nextLargerElementToTheLeft(arr):
    #code here
    ans=[]
    stack=[]
    for i in range(0,len(arr)):
        while len(stack)!=0 and stack[-1]<arr[i]:
            stack.pop()
        if len(stack)==0:
            ans.append(-1)
            stack.append(arr[i])
        else:
            ans.append(stack[-1])
            stack.append(arr[i])
    return ans
    
L=[5,2,9,1,5,6,0]
ans=nextLargerElementToTheLeft(L)
print(ans)
