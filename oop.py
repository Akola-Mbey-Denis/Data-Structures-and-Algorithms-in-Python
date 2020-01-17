class Store:
    def __init__(self,name,typest,loc,storeno):
        self.location =loc
        self.name =name
        self.type=typest
        self.store_number=storeno

    def  __str__(self):
        return "Name of Store:"+ self.name+"\n Store Location: "+self.location+"\n Store Number:"+str(self.store_number)


    def getStoreName(self):
        return self.name

    def getStoreLocation(self):
        return self.location


if __name__ =="__main__":
    #create instance of the class
     store1=Store('Akola','Provisions','Kumasi',11725)
     print(store1)


