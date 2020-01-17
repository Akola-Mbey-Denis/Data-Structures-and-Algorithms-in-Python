def convertToBase(n,base):
    convertString="0123456789ABCDEF"
    if base ==1:
        return n
    if  n<base:
        return convertString[n]
    else:
        return convertToBase(n//base,base)+convertString[n%base] 

def convertToSpecifiedBase(number,desiredBase):
    string= "0123456789ABCDE"
    answer=""
    if desiredBase==1:
        
        return number
    while not (number<desiredBase):
         
        answer=answer+string[number%desiredBase]
         
        number=number//desiredBase
        if number<desiredBase:
           answer =answer+string[number]


    return  answer[::-1]



def reverseString(string_new):
    if len(string_new)==1:
        return string_new 
    else:
        return reverseString(string_new[1:])+string_new[0]   


if __name__ =="__main__":
    print(convertToBase(25,8))
    print(convertToSpecifiedBase(25,8))
    print(reverseString("Adam"))