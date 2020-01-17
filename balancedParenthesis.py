class StringStack:
    '''
    StringStack:
    push: add new items to the stack,data becomes the top of the stack 
    pop: removes data items from the top of the  stack
    peek: returns a copy of the top data item in the stack 
    isEmpty: checks wether the stack is empty or not
    Size: returns the size of the stack 
    '''

    def __init__(self):
        self.word=[]

    def push(self,word):
        self.word.append(word) 


    def pop(self):
        return self.word.pop()


    def peek(self):
        return self.word[len(self.word)-1]  

    def isEmpty(self):
        return self.word==[]    

if __name__=="__main__":
    def parenthesisCheck(testString):
        myString =StringStack()
        isBalance =True
        index=0
        while index<len(testString) and isBalance:
            symbol =testString[index]
            if symbol in "{[(":
                myString.push(symbol)
            else:
                if myString.isEmpty():
                    isBalance=False
                else:
                   top= myString.pop()
                   if not matches(top,symbol):
                       isBalance=False
            index=index+1

        if isBalance and myString.isEmpty():
            return True
        else:
            return False 
def matches(open,close):
    openers="({["
    closers=")}]"
    return openers.index(open)==closers.index(close)            

print(parenthesisCheck("((([{}])))")) 
print(parenthesisCheck("(()"))               




