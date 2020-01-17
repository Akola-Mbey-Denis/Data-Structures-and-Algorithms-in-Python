import string
def unique_String(testString):
    test= testString.lower()
     
    words=[]
    for k in test:
        if not k in words:
            words.append(k)
    if len(testString)>len(words):
        return False 
    else:
        return True          
                
         
     



if __name__=="__main__":
    print(unique_String("Akola"))    

