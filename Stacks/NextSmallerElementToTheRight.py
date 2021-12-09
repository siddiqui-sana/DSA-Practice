def NextSmallerElementToTheRight(arr):
    ans=[]
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        while(len(stack)!=0 and stack[-1]>arr[i]):
            stack.pop()
        if len(stack)==0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    ans.reverse()
    return ans
    
print(NextSmallerElementToTheRight([1,3,5,2,6,4]))
