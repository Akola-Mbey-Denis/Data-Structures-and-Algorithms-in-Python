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




class OrderList:

    def __init__(self):
        self.head=None 

    def isEmpty(self):
        return self.head ==None

    def size(self):
        current=self.head
        count=0
        while current!=None:
            count=count+1
            current =current.get_next() 

        return count 


    def search(self,item):
         current =self.head 
         found=False 
         stop=False 
         while current!=None and not found and not stop:
             if current.get_data()==item:
                 found=True 
             else:
                  if current.get_data()> item:
                      stop=True 
                  else:
                      current=current.get_next()

         return found 


    def add(self,item):
          current =self.head
          prev=None 
          stop =False 
         # found=False
          current=self.head
          while current!=None and not stop:
               if  current.get_data()>item:
                      stop=True 
               else:
                       prev =current 
                       current =current.get_next() 
          temp =Node(item)
          if prev==None:
                temp.set_next(self.head)
                self.head=temp 

          else:
                  temp.set_next(current)
                  self.head=temp 

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

    def printList(self):
        temp =self.head 
        while temp:
            print(temp.data,end =" ")
            temp=temp.next 

if __name__ =="__main__":
    List1=OrderList()
    List1.add(12)
    List1.add(45)
     
    List1.printList()
     
         

                        
          






         