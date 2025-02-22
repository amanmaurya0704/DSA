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
        return node
    def get_min_node(self,node):
        current = node
        while current.left is None:
            current = current.left
        return current
        
    def delete(self,data):
        self.root = self.delete_helper(data,self.root)
    def delete_helper(self,data,node):
        if node ==None:
            return None
        if node.data>data:
            node.left = self.delete_helper(data,node.left)
        elif node.data<data:
            node.right = self.delete_helper(data,node.right)
        else:
            if node.right == None:
                return node.right
            elif node.left is None:
                return node.left
            min_larger_node= self.get_min_node(node.right)
            node.data = min_larger_node.data
            node.right = self.delete_helper(min_larger_node.data,node.data)
        return node
                
                
         
    def search(self,data):
        return self.searchHelper(data,self.root)
    def searchHelper(self,data,node):
        if node == None:
            return False
        
        if node.data == data:
            return True
        if node.data > data:
            return self.searchHelper(data,node.left)
        else:
            return self.searchHelper(data, node.right)
    

bstObject = BST()

bstObject.insert(20)
bstObject.insert(25)
bstObject.insert(10)
bstObject.insert(15)
print(bstObject.search(10))
#print_binary_tree(bstObject.root)
bstObject.delete(10)
print(bstObject.search(10))
print_binary_tree(bstObject.root)
