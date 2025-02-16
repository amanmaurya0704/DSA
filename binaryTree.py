from collections import deque
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def print_binary_tree(root):
    if root == None:
        return
    
    print(root.data, end=":")
    
    if root.left == None:
        print("L -> None",end=",")
    else:
        print(f"L -> {root.left.data}",end=",")
        
    if root.right == None:
        print("R -> None\n",end="")
    else:
        print(f"R -> {root.right.data}\n",end="")
    
    print_binary_tree(root.left)
    print_binary_tree(root.right)

def take_input_binary_tree():
    data = int(input("Enter Data for the node: "))
    if data == -1:
        return None
    
    node = BinaryTreeNode(data)
    print(f"Enter the left child of {data}")
    node.left = take_input_binary_tree()
    print(f"Enter the right child of {data}")
    node.right = take_input_binary_tree()
    
    return node
def take_input_levelwise():
    data = int(input("Enter the data of root: " ))
    if data==-1:
        return None
    root = BinaryTreeNode(data)
    queue = deque([root])
    
    while len(queue)!=0:
        current_node = queue.popleft()
        left_child_data = int(input(f"Enter left child of {current_node.data}: "))
        if left_child_data != -1:
            left_node = BinaryTreeNode(left_child_data)
            current_node.left = left_node
            queue.append(left_node)
        right_child_data = int(input(f"Enter right child of {current_node.data}: "))
        if right_child_data != -1:
            right_node = BinaryTreeNode(right_child_data)
            current_node.right = right_node
            queue.append(right_node)
    return root
def print_level_wise(root):
    if root == None:
        return
    
    queue = deque([root])
    while len(queue)!=0:
        currentNode = queue.popleft()
        print(currentNode.data,end = ":")
        if currentNode.left != None:
            print(f"L -> {currentNode.left.data}",end = ",")
            queue.append(currentNode.left)
        else:
            print("L -> None",end = ",")
        if currentNode.right != None:
            print(f"R -> {currentNode.right.data}",end = ",")
            queue.append(currentNode.right)
        else:
            print("R -> None",sep = ",")
        print("\n")
def height(root):
    if root ==None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    
    heightOfTree=1+max(leftHeight,rightHeight)
    return heightOfTree
    
def diameter_of_a_tree(root):
    if root == None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    
    leftDiameter = diameter_of_a_tree(root.left)
    rightDiameter = diameter_of_a_tree(root.right)
    
    ans = max(leftDiameter,rightDiameter,leftHeight+rightHeight)
    return ans

def isbalanced(root):
    if root == None:
        return True
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    
    if abs(leftHeight-rightHeight) > 1:
        return False
    
    return isbalanced(root.left) and isbalanced(root.right)

def isBalanced_optimised(root):
    if root == None:
        return True,0
    
    leftIsbalanced, leftHeight = isBalanced_optimised(root.left)
    rightIsbalanced, rightHeight = isBalanced_optimised(root.right)
    
    curretHeight = 1+max(leftHeight,rightHeight)
    
    current_balanced = abs(leftHeight - rightHeight)<=1 and leftIsbalanced and rightIsbalanced
    
    return current_balanced,curretHeight

def preorder_traversal(root):
    if root == None:
        return
    print(root.data,end = ",")
    preorder_traversal(root.left)
    preorder_traversal(root.right)    
    
def postorder_traversal(root):
    if root == None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data,end=",")
    
def inorder_traversal(root):
    if root == None:
        return
    inorder_traversal(root.left)
    print(root.data,end = ",")
    inorder_traversal(root.right)
    
def construct_BT_from_preorder_inorder(inorder,preorder,inS,inE,preS,preE):
    if(inS>inE or preS>preE):
        return None
    
    root_data = preorder[preS]
    root = BinaryTreeNode(root_data)
    
    inorder_root_index=-1
    for i in range(inS,inE+1):
        if inorder[i] == root_data:
            inorder_root_index=i
            break
    if(inorder_root_index==-1):
        print("root not founr in inorder,please check logic")
        return None
    
    linS = inS
    linE = inorder_root_index-1
    lpreS = preS+1
    lpreE = linE-linS + lpreS
    
    
    rinE = inE
    rpreS = lpreE + 1
    rpreE =preE 
    rinS = inorder_root_index+1
    
    root.left = construct_BT_from_preorder_inorder(inorder,preorder,linS,linE,lpreS,lpreE)
    root.right = construct_BT_from_preorder_inorder(inorder,preorder,rinS,rinE,rpreS,rpreE)
    
    return root

preorder = [1,2,4,5,3,6]
inorder = [4,2,5,1,3,6]
n = len(inorder)
root = construct_BT_from_preorder_inorder(inorder,preorder,0,n-1,0,n-1)
print_level_wise(root)
    
    
#root = take_input_levelwise()

# print_binary_tree(root)   

# root = BinaryTreeNode(1)
# root.left = BinaryTreeNode(2)
# root.right = BinaryTreeNode(3)
# print_level_wise(root)
# # print_binary_tree(root)

# root = BinaryTreeNode(1)
# root.left = BinaryTreeNode(2)
# root.right = BinaryTreeNode(3)
# root.left.left = BinaryTreeNode(4)
# root.left.right = BinaryTreeNode(5)
# root.left.left.left = BinaryTreeNode(8)

# root1 = BinaryTreeNode(1)
# root1.left = BinaryTreeNode(2)
# root1.right = BinaryTreeNode(3)
# root1.left.left = BinaryTreeNode(4)
# root1.left.right = BinaryTreeNode(5)
# root1.right.right = BinaryTreeNode(6)

# # Tree 2: Slightly complex tree with height 4
# root2 = BinaryTreeNode(10)
# root2.left = BinaryTreeNode(20)
# root2.right = BinaryTreeNode(30)
# root2.left.left = BinaryTreeNode(40)
# root2.left.right = BinaryTreeNode(50)
# root2.right.left = BinaryTreeNode(60)
# root2.right.right = BinaryTreeNode(70)
# root2.left.left.left = BinaryTreeNode(80)

# # Tree 3: More complex tree with height 5
# root3 = BinaryTreeNode(100)
# root3.left = BinaryTreeNode(200)
# root3.right = BinaryTreeNode(300)
# root3.left.left = BinaryTreeNode(400)
# root3.left.right = BinaryTreeNode(500)
# root3.right.left = BinaryTreeNode(600)
# root3.right.right = BinaryTreeNode(700)
# root3.left.left.left = BinaryTreeNode(800)
# root3.left.left.right = BinaryTreeNode(900)
# root3.right.right.left = BinaryTreeNode(1000)
# root3.right.right.right = BinaryTreeNode(1100)
# print_binary_tree(root1)
# # print(diameter_of_a_tree(root3))
# #print(isBalanced_optimised(root))
# preorder_traversal(root1)
# print("\n")
# postorder_traversal(root1)
# print("\n")
# inorder_traversal(root1)