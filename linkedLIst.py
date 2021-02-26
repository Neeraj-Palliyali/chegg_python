
class node: 
    def __init__(self): 
        data = None
        next = None
  
def add(data): 
  
    newnode = node() 
    newnode.data = data 
    newnode.next = None
    return newnode 
  
def stringToLinkedList(text,head): 
  
    head = add(text[0]) 
    curr = head 
    for i in range(len(text) - 1):  
        curr.next = add(text[i + 1]) 
        curr = curr.next
      
    return head 

def commonKmost(k, head):
    curr=head
    map1={}
    while(curr!=None):
        if(curr.data in map1):
            map1[curr.data]+=1
        else:
            map1[curr.data]=1
        curr = curr.next
    
    a = [0] * (len(map1))
    j = 0
    for i in map1:
        a[j] = [i, map1[i]]
        j += 1
    a = sorted(a, key = lambda x : x[0],
                        reverse = True)
    a = sorted(a, key = lambda x : x[1], 
                        reverse = True)
  
    print(k, "Character with most occurrences are:")
    for i in range(k):
        print(a[i][0], end = " ")



text = input("Enter String:")
head = None
head = stringToLinkedList(text, head) 
k= int(input("Enter number of ocurrence you want to find:"))
commonKmost(k,head)