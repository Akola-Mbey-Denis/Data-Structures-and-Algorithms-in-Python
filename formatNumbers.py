def insertComma(number):
    num =str(number) 
    count=0
    formatted_num=""
    if len(num)<=3:
        return num

     
    for i in range(len(num)-1,-1,-1):
        # if i==0:
        #     formatted_num=formatted_num+num[i]
        #   

        if count%3!=0: 
      
         
            formatted_num=formatted_num+num[i]    
                 
         
        else:
            if count ==len(num)-1:
                formatted_num=formatted_num+num[i] 
            else:
                formatted_num=formatted_num+num[i]               
                formatted_num=formatted_num+","
                     
        count=count+1
        return formatted_num [::-1] 


       
def place_value(number): 
    return ("{:,}".format(number)) 



def findAverageofGroups(list,m):
    average=[]
    for j in range(0,len(list)-m):
        print(j)
        average.append(sum(list[j:j+3])/m)
    return average    
#[1,2,3,4,5,6]
#(1,2,3),(2,3,4),(3,4,5)(4,5,6)

def findPair(list,target):
    for i in range(0,len(list)-1):
        for k in range(i+1,len(list)):
            if list[i]+list[k]==target:
                print("(",list[i],",",list[k],")", end=",") 

def firstOccurence(list,item):
    for k in range(0,len(list)):
        if list[k]==item:
            return k 

def missingString(string_1,string_2):
    first_string=string_1.split()
    second_string=string_2.split()
    missing=[]
    for k in first_string:
        if not k in second_string:
            missing.append(k)
    return missing        
           

def reverseSentence(my_sentence):
    mystring=my_sentence.split()
    new_sentence =mystring[::-1]
    for k in new_sentence:
        print(k ,end=" ")
    


             
         


        


  
 
        

    
if __name__=="__main__":
    print(place_value(200) )   
    findPair([0,2,3,4,6,5,1,7,8],8)
    print(firstOccurence([1,2,4,4,5,6,7,8,10],4)) 
    missingString("This is an example","is example") 
    reverseSentence("You are good")
