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
    
root = take_input_levelwise()

# print_binary_tree(root)   

# root = BinaryTreeNode(1)
# root.left = BinaryTreeNode(2)
# root.right = BinaryTreeNode(3)
print_level_wise(root)
# # print_binary_tree(root)

