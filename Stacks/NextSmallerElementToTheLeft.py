class Solution:
    def leftSmaller(self, n, a):
      ### n-> size of array
      ### a-> array
        # code here
        stack=[]
        ans=[]
        for i in range(n):
            while len(stack)!=0 and stack[-1]>=a[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
                stack.append(a[i])
            else:
                ans.append(stack[-1])
                stack.append(a[i])
        return ans
