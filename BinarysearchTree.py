class BSTNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def print_bst(root):
    if(root is None):
        return
    print_bst(root.left)
    print(root.data,end = " ") # Inorder Traversal of my BST
    print_bst(root.right)




def print_binary_tree(node):
    if node is None:
        return
    
    # Format: Node: L->LeftChild, R->RightChild
    print(f"{node.data}:", end=" ")
    
    if node.left:
        print(f"L->{node.left.data}", end=", ")
    else:
        print("L->None", end=", ")
    
    if node.right:
        print(f"R->{node.right.data}")
    else:
        print("R->None")
    
    # Recur for the left and right children
    print_binary_tree(node.left)
    print_binary_tree(node.right)
def searchBST(root,value):
    if root==None:
        return False
    
    if root.data > value:
        return searchBST(root.left,value)
    elif root.data < value:
        return searchBST(root.right,value)
    elif root.data == value:
        return True
       
def SortedListtoBST(l1):
    if(len(l1)==0):
        return None
    mid = len(l1)//2

    rootdata = l1[mid]
    root = BSTNode(rootdata)
    root.left =SortedListtoBST(l1[:mid])
    root.right = SortedListtoBST(l1[mid+1:])
    return root
def find_max(node):
    if node == None:
        return float("-inf")
    
    left_max = find_max(node.left)
    right_max = find_max(node.right)
    
    ans = max(left_max,right_max,node.data)
    return ans
def find_min(node):
    if node == None:
        return float("inf")
    
    left_min = find_min(node.left)
    right_min = find_min(node.right)
    
    ans = max(left_min,right_min,node.data)
    return ans
def checkBST(root):
    if root==None:
        return True
    
    leftmax = find_max(root.left)
    rightmin = find_min(root.right)
    
    left_BST = checkBST(root.left)
    right_BST= checkBST(root.right)
    print(left_BST,right_BST,leftmax,rightmin,root.data)
    ans = left_BST and right_BST and (leftmax < root.data) and (root.data<rightmin)
    return ans

def checkBST_optimised(root):
    if root == None:
        return True,float("inf"),float("-inf")
    
    leftBST,leftmin,leftmax = checkBST_optimised(root.left)
    rightBST,rightmin,rightmax = checkBST_optimised(root.right)
    ans = leftBST and rightBST and (leftmax < root.data) and (root.data<rightmin)
    
    return ans, min(leftmin,root.data), max(rightmax,root.data)
def printElementsinRange(root,low,high):
    if root == None:
        return 
    if low<root.data:
        printElementsinRange(root.left,low,high)
    
    if low <= root.data <= high:
        print(root.data,end=" ")
    
    if high>root.data:
        printElementsinRange(root.right,low,high)
 
def checkBST_limit(node,minimum,maximum):
    if node == None:
        return True
    
    if node.data < minimum or node.data > maximum:
        return False
    
    ansLeft = checkBST_limit(node.left,minimum,node.data-1)
    ansRight = checkBST_limit(node.right,node.data+1,maximum)
    return ansLeft and ansRight
       
root = SortedListtoBST([1,2,3,4,5,6,7])
root3= SortedListtoBST([5,10,15,20,25,30,35,40,50,55,60,65,70,75])
# root1 = SortedListtoBST([10,50,70,90,40,250,500])
# #print_binary_tree(root)
# print_binary_tree(root1)
# # print(checkBST(root))
# print(checkBST(root1))
# print(searchBST(root,20))

root2 = BSTNode(5)
root2.left = BSTNode(15)
root2.right = BSTNode(25)
# print(checkBST_optimised(root))

# printElementsinRange(root,6,15)
print(checkBST_limit(root2,float("-inf"),float("inf")))
print(checkBST_limit(root3,float("-inf"),float("inf")))