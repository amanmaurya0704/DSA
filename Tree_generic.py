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
               
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

print_tree_detailed(root)