import math
class Tree:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right
def construct(arr,low,high): 
    if high<low:
        return None
    mid=(low+high)//2
    root_value=arr[mid]
    left_node=construct(arr,low,mid-1)
    right_node=construct(arr,mid+1,high)
    new_node=Tree(root_value,left_node,right_node)
    return new_node

def pre_order(root):
    if root==None:
        return
    else:
        print(root.data,end=" ")
        pre_order(root.left)
        pre_order(root.right)
def find_max(root):
    if root==None:
        return -1

    if root.right is not None:  # Largest element will be on the right most side in BST
        return find_max(root.right)
    else:
        return root.data

def find_min(root):
    if root==None:
        return -1
    else:
        if root.left is not None:
            return find_min(root.left)
        else:
            return root.data
def in_order(root):
    if root==None:
        return 
    else:
        in_order(root.left)
        print(root.data,end=" ")
        in_order(root.right)

def search(root,val):
    if root==None:
        return None
    if root.data==val:
        return root
    else:
        if val>root.data:
            return search(root.right,val)
        else:
            return search(root.left,val)
def insert(root,val):
    if root==None:
        return Tree(val,None,None)
    else:
        if root.data>val:
            root.left=insert(root.left,val)
        elif val>root.data:
            root.right=insert(root.right,val)
    return root
def delete(root,val):
    if root==None:
        return None
    else:
        if val>root.data:
            root.right=delete(root.right,val)
        elif val<root.data:
            root.left=delete(root.left,val)
        else:
            if root.left is not None and root.right is not None:
                left_max = find_max(root.left)
                root.data=left_max
                root.left=delete(root.left,left_max)
                return root
            elif root.left is not None:
                return root.left
            elif root.right is not None:
                return root.right
            else:
                return None
def checkValidation(root,min_value,max_value):
    if root is None:
        return True
    if root.data>min_value and root.data<max_value:
        return checkValidation(root.left,min_value,root.data) and checkValidation(root.right, root.data,max_value)
    return False



def validate(root):
    return checkValidation(root,-math.inf,math.inf)




arr=[10,20,30,40,50,60,70,80,90]
root=construct(arr,0,len(arr)-1)
print(insert(root,67))
in_order(root)
print(delete(root,67))
in_order(root)

