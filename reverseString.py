class StringStack:

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


if __name__ =="__main__":
    word =input("Enter a word")
    mystring= StringStack()

    for k in range(0,len(word)):
        mystring.push(word[k])

    #print the reverse
    
    while not mystring.isEmpty():
        print(mystring.pop(),end="")
          



        
