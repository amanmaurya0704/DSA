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
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        self.root = self.insert_helper(data,self.root)
    def insert_helper(self,data,node):
        if node == None:
            newNode = BSTNode(data)
            return newNode
        if node.data > data:
            node.left = self.insert_helper(data,node.left)
        elif node.data< data:
            node.right = self.insert_helper(data,node.right)
            
    def delete(self,data):
        pass
    def search(self,data):
        return self.searchHelper(data,self.root)
    def searchHelper(self,data,root):
        if self.root == None:
            return False
        
        if self.root.data == data:
            return True
        elif self.root.data > data:
            return self.search(self.root.right)
        else:
            return self.search(self.root.left)

bstObject = BST()

bstObject.insert(20)
bstObject.insert(25)
bstObject.insert(10)
bstObject.insert(15)
print_binary_tree(bstObject.root)
