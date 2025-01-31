from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        
def print_tree_detailed(root):
    if root == None:
        return
    print(f"{root.data}:",end="")
    for eachChild in root.children:
        print(eachChild.data, end=",")
    print()
    for eachChild in root.children:
       print_tree_detailed(eachChild)
def take_input_recursion():
    data = int(input("Enter the data for the Node:"))
    node = TreeNode(data)
    numChildren = int(input(f"Enter the number of children of {data}"))
    for eachChild in range(numChildren):
        child = take_input_recursion()
        node.children.append(child)
    return node

def take_input_levelwise():
    data = int(input("Enter the root data"))
    root = TreeNode(data)
    queue = deque([root])
    while (len(queue))!=0:
        current_node = queue.popleft()
        numChildren = int(input("Enter number of children of "+ str(current_node.data)))
        for i in range(numChildren):
            childData = int(input(f"Enter data for child{i+1} of {current_node.data}:"))
            childNode = TreeNode(childData)
            current_node.children.append(childNode)
            queue.append(childNode)
    return root

def countNodes(root):
    if root == None:
        return 0
    numberOfNodes = 1
    for eachChild in root.children:
        numberOfNodes += countNodes(eachChild)
    return numberOfNodes

def heightOfTree(root):
    if(root == None):
        return 0
    height = 1
    max_child_height=0
    for eachChild in root.children:
        max_child_height = max(max_child_height,heightOfTree(eachChild))
    height+=max_child_height
    return height

def preorderTraversal(root):
    if root==None:
        return
    print(root.data,end="")
    for eachchild in root.children:
        preorderTraversal(eachchild)

def postorderTraversal(root):
    if root==None:
        return
    for eachchild in root.children:
        postorderTraversal(eachchild)
    print(root.data,end='')
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

child1_1 = TreeNode(5)
child1_1_1 = TreeNode(6)
root.children.append(child1)
root.children.append(child2)
root.children.append(child3)
child1.children.append(child1_1)
child1_1.children.append(child1_1_1)

print_tree_detailed(root)
print(f"no of nodes: {countNodes(root)}")
print(f"height of tree: {heightOfTree(root)}")
preorderTraversal(root)
print("\n")
postorderTraversal(root)
# print_tree_detailed(root)

# root = take_input_recursion()
# print_tree_detailed(root)

# root = take_input_levelwise()
# print_tree_detailed(root)