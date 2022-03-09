# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        
        Q=deque()
        Q.append(root)
        bfs=[]  ##For storing each sublist i.e. the nodes in one level
        while len(Q)!=0:
              l=len(Q)    ## At this point Q contains all nodes in a particular level so l= no.of nodes in a level
            ans=[]  ## To store the value of nodes in a level
            for i in range(l):  ## For each node in a level 
                r=Q.popleft()   ## poping each node that belonged to same level
                ans.append(r.val)
                if r.left:    ## Appending the left and right child of each node for further processing.
                    Q.append(r.left)    ##Note that these newly inserted nodes won't be popped in current iteration of for loop because these are incresing the length of Q. But poping is only happening till the last length of Queue 
                if r.right:
                    Q.append(r.right)
            bfs.append(ans)
        return bfs
