def detectAnagram(first_string,second_string):
    #check to see if the two strings are of equal length
    if len(first_string)!=len(second_string) :
        return False
    else:
        first =sorted(first_string)
        second =sorted(second_string)
        for k in range(0,len(first)):
            if first[k]!=second[k]:
                #check to see if the two words contains the same characters.
                return False
            else:
                return True  
def efficientSolution(first_string,second_string ):
   #26 counters for each alphabet letters 
    c1=[0]*26
    c2=[0]*26

    for i in range(len(first_string)):
        pos =ord(first_string[i])-ord('a')
        c1[pos]=c1[pos]+1


    for k in range (len(second_string)):
        pos =ord(second_string[k])-ord('a')
        c2[pos]=c2[pos]+1

    j=0
    stillOk =True
    while j<26 and stillOk:
        if c1[j]==c2[j]:
            j=j+1
        else:
            stillOk=False
    return stillOk            
                 




if __name__ =="__main__":
    print(detectAnagram("dog","dog"))
    print(efficientSolution("dog","god"))
