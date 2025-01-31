class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class StackUsingLinkList:
    def __init__(self):
        self.head = None
        self.len = 0
    def push(self,data):
        newNode = Node(data)
        self.len+=1
        if(self.head == None):
            self.head = newNode
            return f"Added {data} to the stack"
        
        newNode.next = self.head
        self.head = newNode
        return f"Added {data} to the stack"
    def top(self):
        if self.head is None or self.len == 0:
            return "Stack is empty, no top element"
        return self.head.data
    def pop(self):
        if self.head is None or self.len == 0:
            return "Stack is empty, no top element"
        
        dataAtTop = self.head.data
        self.head = self.head.next
        self.len -=1
        return dataAtTop
    def size(self):
        return self.size
    def is_empty(self):
        return self.size==0
mystack = StackUsingLinkList()
    
    
print(mystack.is_empty())
print(mystack.push(10))
print(mystack.push(20))
print(mystack.push(30))
print(mystack.push(40))
print(mystack.is_empty())
print(mystack.pop())
print(mystack.pop())
print(mystack.size())
print(mystack.top())
    
