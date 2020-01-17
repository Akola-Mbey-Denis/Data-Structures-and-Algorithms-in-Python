class Stack:
    '''
    This is an implemenation of stack data structure
    methods:
    pop: removes an element from the stack
    push: adds an element to the stack
    peek: returns the element at the top of the stack
    size: returns the number of elements in the stack  

    '''
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self) :
        self.items.pop()


    def peek(self):
        return self.items[len(self.items)-1] 
         

    def size(self):
        return len(self.items) 

     


    

if __name__ =="__main__":
    def decimalToBinary(decimalNumber):
    
        myStack =Stack()
        Binary =""
        
        
        
        while decimalNumber>0:
        
            remainder =decimalNumber%2
            myStack.push(remainder)
        
            decimalNumber=decimalNumber//2
        
            
        
        while  not myStack.isEmpty():
            Binary =Binary+str(myStack.pop())

        return Binary    
        
         
               
    print(decimalToBinary(20))
     



