def findMissingNumber(array):
    for k in range(0,len(array)+1):
        if k not in array:
            return k

def reverseInteger(number):
    reverse=""
    if number<0:
        reverse=str(abs(number))
        return "-"+ reverse[::-1]
    else:   
        return reverse[::-1]            


if __name__ =="__main__":
    print(findMissingNumber( [0, 1, 3] ))
    print(reverseInteger(-123))
    def reverse_sentence(sentence): 
        new_string =sentence.split( )
        for k in range(len(new_string)-1,-1,-1):
            print(new_string[k],end=" ") 
    reverse_sentence("the sky is blue")      
               

