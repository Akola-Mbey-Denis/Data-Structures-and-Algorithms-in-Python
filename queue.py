class Queue:
    def __init__(self):
        self.items =[] 

    def  isEmpty(self):
        return self.items==[]  


    def enqueue(self,item):
        self.items.insert(0,item) 


    def  dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items) 

    def __str__(self):
        return str(self.items)    


if __name__ == "__main__":
    myQueue =Queue()
    myQueue.enqueue(12)
    myQueue.enqueue(18)
    myQueue.enqueue("boy")
    print(myQueue)
                     