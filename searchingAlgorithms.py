def sequentialSearch(List,item):
    '''
    Efficient Linear Search algorithm
    Returns True if the item we are searching for is found
    Return False if the element is not in the list  
    '''
    pos=0
    found=False 
    stop =False
    while pos <len(List) and not found and not stop:
        if List[pos]==item:
            found=True
            return found
        pos=pos +1 

        if List[pos]>item:
            stop=True
            return found

        if pos==len(List)-1 and not found:
             return  found

def binarySearch(search_list,item):
    low=0
    high =len(search_list)-1
  
    
    while low<=high:
        mid=(low+high)//2
        if search_list[mid]==item:
             return mid
        elif item>mid:
            low =mid+1
        elif item<mid:
            high=mid-1

    return -1     

def recursiveBinarySearch(search_list,item):
      
     if len(search_list)==0:
         return False
     else:
          midpoint=len(search_list)//2
          if search_list[midpoint]==item:
              return True 
          else:
               if search_list[midpoint]<item:
                   return recursiveBinarySearch(search_list[midpoint+1:],item)
               else:
                    return recursiveBinarySearch(search_list[:midpoint],item)               
         




if __name__ =="__main__":
    print(sequentialSearch([12,15,34,48,55,60,79],79)) 
    print(binarySearch([1,2,3,4,5,6,79,99],200))  
    print(recursiveBinarySearch([1,2,3,4,5,6,79,99],200))                