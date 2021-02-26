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

def printList(head):
    curr=head
    while(curr!=None):
        print(curr.data, end="->")
        curr=curr.next
    print()

def swap1(head):
    curr=head
    while curr!=None and curr.next!=None:
        curr.data, curr.next.data= curr.next.data, curr.data
        curr=curr.next.next
            

li=list(map(int,input("Enter numbers:").split()))

head = None
head= toLinkedLIst(li, head)
printList(head)
swap1(head)
printList(head)



# e2.nextval = e3