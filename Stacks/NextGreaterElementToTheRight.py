'''Given an array arr[ ] of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

Example 1:

Input: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element 
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
since it doesn't exist, it is -1.'''


class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        ans=[]
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while len(stack)!=0 and stack[-1]<arr[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
                stack.append(arr[i])
            else:
                ans.append(stack[-1])
                stack.append(arr[i])
        ans.reverse()
                
        return ans
