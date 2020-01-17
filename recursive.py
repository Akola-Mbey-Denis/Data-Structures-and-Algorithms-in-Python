def factorial(number):
    if number ==1 or number==0:
        return 1
    else:
        return factorial(number-1)*number 

def reverseList(list_data):
    if len(list_data)==1:
        return list_data
    else:
        return [list_data[-1]] + reverseList(list_data[:-1])   

def fibonnaci(number):
     
    if number==0:
        return 0
    elif number==1:
        return 1    
     
    else:
         return fibonnaci(number-2)+fibonnaci(number-1)  


print(factorial(3))
print(reverseList([1,2,7,9]))
print(fibonnaci(6))           