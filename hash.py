class HashTable:

    def __init__(self):
        self.size=11
        self.slots=[None]*self.size 
        self.data=[None]*self.size


    def insert(self,key,value):
        '''
        It inserts a new data item into the hash table  
        '''
        hash_value =self.hash_function(key,len(self.slots)) 

        if self.slots[hash_value]==None:
            self.slots[hash_value]=key 
            self.data[hash_value ]=value
        else:
            if self.slots[hash_value]==key:
                self.data =value
            else:
                next_slot =self.rehashfunction(hash_value,len(self.slots))     
                while self.slots[next_slot]!=None and self.slots[next]!=key:
                    next_slot=self.rehashfunction(next_slot,len(self.slots))
                if self.slots[next_slot]==None:
                    self.slots[next_slot]=key 
                    self.data[next_slot]=value
                else:
                    self.data[next_slot]=value 
    def hash_function(self,key,size): 
        '''
        Generates the slot location to store an item in the hash table
        '''
        return key%size

    def rehashfunction(self,old_hash,size):
        '''
        Regenerates a slot to place a data item if the first slot is occupied. Mediates against collision 
        '''
        return (old_hash+1)%size                       
    
    def retrieveItem(self,key):
        start_slot=self.hash_function(key,len(self.slots))
        data =None 
        stop =False
        found=False 
        position=start_slot 
        while self.slots[position]!=None and not found and not stop:
            if self.slots[position]==key:
                found=True 
                data=self.data[position]
            else:
               position=self.rehashfunction(position,len(self.slots))
               if position==start_slot:
                   stop=True 
        return data 

    def __getitem__(self,key):
        return self.retrieveItem(key)


    def __setitem__(self,key,data):
        return self.insert(key,data)                   

if __name__=="__main__":
    hash =HashTable()
    hash.insert(45,"Akola")
    hash.insert(50,"Denis")
    hash.insert(34,"Adam")
    hash.insert(20,"Potter")

    print(hash.data)
    print(hash.slots)
    print(hash.retrieveItem(20))