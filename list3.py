class node: 
    def __init__(self): 
        data = None
        next = None
  
def add(data): 
  
    newnode = node() 
    newnode.data = data 
    newnode.next = None
    return newnode 
  
def toLinkedLIst(no,head): 
  
    head = add(no[0]) 
    curr = head 
    for i in range(len(no) - 1):  
        curr.next = add(no[i + 1]) 
        curr = curr.next
      
    return head 

def removeLastNode(head): 
    
    
    return head

def asNextElement(ki, head):
    if head == None: 
        return None
    if head.next == None: 
        head = None
        return None
    second_last = head 
    while(second_last.next.next): 
        second_last = second_last.next
    second_last.next = None
    curr=head
    while(curr!=None):
        print(curr.data, end="->")
        curr=curr.next
    head = add(ki[0])
    curr = head 
    for i in range(len(ki) - 1):  
        curr.next = add(ki[i + 1]) 
        curr = curr.next
    
    return head

def printList(head):
    curr=head
    while(curr!=None):
        print(curr.data, end="->")
        curr=curr.next
    print()



li=list(map(int,input("Enter numbers:").split()))

head = None
head= toLinkedLIst(li, head)
printList(head)
ki=list(map(int,input("enter New list as last element:").split()))
head= asNextElement(ki, head)
printList(head)