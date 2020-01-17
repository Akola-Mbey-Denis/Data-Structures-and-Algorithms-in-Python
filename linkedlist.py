class Node:
    def __init__(self,init_data):
        self.data =init_data
        self.next =None 
    
    def get_data(self):
        return self.data 


    def get_next(self):
        return self.next 

    def set_data(self,data_item):
        self.data =data_item

    def set_next(self,next):
        self.next =next



class UnorderedList:

    def __init__(self):
        self.head=None 
    

    def isEmpty(self):
        return self.head == None 
    

    def add(self,item):
        temp =Node(item)
        temp.set_next(self.head)
        self.head =temp 


    def size(self):
        current=self.head
        count=0
        while current!=None:
            count=count+1 
            current =current.get_next()

        return count 


    def search(self,item):
        current =self.head 
        Found=True 
        while current!=None and not Found:
            if current.get_data()==item:
                Found=True 
            else:
                current=current.get_next()   


        return Found  


    def remove(self,item):
         current=self.head 
         Found =False
         previous =None 
         while current!=None and not Found:
             if current.get_data()==item:
                 Found=True 
             else:
                 current=current.get_next()

         if previous==None:
             self.head =current.get_next()
         else:
              previous.set_next(current.get_next())                       



    def Push(self,item):
        newNode =Node(item)
        newNode.next=self.head 
        self.head=newNode

    def index(self,item):
        current =self.head
        count=0
        Found=False 
        while current!=None and not Found:
            if current.get_data()==item:
               Found=True
               count=0
            else:
                 count=count+1
                 current=current.get_next()
            return count 

    def append(self,item):
        newNode =Node(item)
        if self.head is None:
            self.head =newNode
            return 
        last=self.head 
        while last.next:
            last=last.next 


        last.next=newNode


    def printList(self):
        temp =self.head 
        while temp:
            print(temp.data,end =" ")
            temp=temp.next                        