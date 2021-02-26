
class Node:
    def _init_ (self,data):
        self.data = data
        self.next = None
        
    def _str_(self):
    # """magic method for the string"""
        return(str(self.data))
    
    def _repr_(self):
        return(str(self.data))
    
class LinkedList:
    def _init_(self,data):
        self.first = Node(data)
        self.last = self.first
        self.temp = self.first
        self.n = 1
        
    def append(self,data):
        newNode = Node(data)
        if self.n == 1:
            self.first.next = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = self.last.next
            self.n = self.n + 1
    
    def _iter_(self):
        self.i = 1
        return self
    
    def _next_(self):
        if self.i > self.n:
            raise StopIteration
        else:
            data = self.temp
            self.temp = self.temp.next
            self.i += 1
            return (data)
    
    def _len_(self):
        return self.n
    
    def _str_(self):
        result = ""
        self.temp = self.first
        for i in range(self.n):
            result += str(self.temp.data) + "->"
            self.temp = self.temp.next
        return result
    
    def _getitem_(self,index):
        try:
            for i in range(self.n):
                self.temp = self.first
                if i == index:
                    return self.temp.data
        except IndexError:
            return "list index out of range"
    
    def _setitem_(self, index, data):
        pos = 0
        try:
            for i in self:
                if pos == index:
                    i.data = data
                    return True
                pos += 1
        except IndexError:
            return "list index out of range"
    
    def _add_(self, data):
        resultLinkedList = LinkedList(self.first)
        temp = self.firstnext
        for i in range(1, self.n):
            print("inside : ", temp.data)
            resultLinkedList.append(temp.data)
            temp = temp.next
            resultLinkedList.append(data)
        return resultLinkedList

a = LinkedList(0)
a.append(1)
a.append(2)

print("7 points if this works")
for n in a:
    print(n)

    print("")

print("2 points if this works")
for n in a:
    print(n)

    print("")

print("3 points if both of these work")
for n in a:
    if n == 2:
        break
    else:
        print(n)

        print("")

for n in a:
    if n == 2:
        break
    else:
        print(n)

        print("")
