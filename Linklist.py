class Node:
    def __init__(self,Value):
        self.data = Value
        self.next = None

def print_LL(head):
    temp = head
    while(head!=None):
        print(head.data,"->",end="")
        head = head.next
def take_input():
    value = int(input("Enter value"))
    head = None
    while (value != -1):
        newNode = Node(value)
        if head == None:
            head = newNode
        else:
            temp = head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
        value = int(input("enter value"))
    return head   
def take_input_optimized():
    value = int(input("Enter Value"))
    head = None
    tail = None
    while value!=-1:
        newNode = Node(value)
        if head==None:
            head=newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        value = int(input("Enter Value"))
    return head

def insert_at_tail(head,data):
    newNode = Node(data)
    temp=head
    if head == None:
        return newNode
    else:
        while temp.next != None:
            temp = temp.next 
        temp.next = newNode
    return head

def insert_at_head(head,data):
    newNode = Node(data)
    if head == None:
        return newNode
    else:
        newNode.next = head
        head = newNode
    return head
#10->20->30->40
#100
#
def insert_at_index(head,data,index):
    if index == 0:
        return insert_at_head
    newNode = Node(data)
    count = 0
    temp = head
    while temp is not None and count<index:
        temp=temp.next
    if temp is None:
        print("Index Out of Bound")
    newNode.next = temp.next
    temp.next = newNode
    return head
LL = take_input_optimized()
newLL = insert_at_index(LL,100,2)
print_LL(newLL)
