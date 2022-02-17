class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.next = None;
    
class CreateList:        
    def __init__(self):    
        self.head = Node(None);    
        self.tail = Node(None);    
        self.head.next = self.tail;    
        self.tail.next = self.head;    
           
    def add(self,data):    
        newNode = Node(data);
        
        if self.head.data is None:        
            self.head = newNode;    
            self.tail = newNode;    
            newNode.next = self.head;    
        else:
            self.tail.next = newNode;    
            self.tail = newNode;     
            self.tail.next = self.head; 
            
   
        
class Solution:
    def myrecursor (self,n, ptr,k):
        if n == 1:
            return ptr.data
        temp = k - 2
        curr = ptr
        while(temp > 0):
            curr= curr.next
            temp -=1
            
        curr.next=curr.next.next
        ptr=curr.next
        
        return self.myrecursor(n-1,ptr,k)   

    
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        if k == 1:
            return n
        
        c1 = CreateList();
        
        for i in range(1,n+1):
            c1.add(i)
        
        return self.myrecursor(n,c1.head,k)   
        
