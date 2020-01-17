def buySell(transaction_list):
    array=[]
    for i in range(0,len(transaction_list)-1):
        for j in range(i+1,len(transaction_list)):
            
          
            if transaction_list[i]>transaction_list[j]:
                pass
                 
            else:
                array.append(transaction_list[j]-transaction_list[i])
        if len(array)==0:
             return 0
    return  max(array)       


if __name__ == "__main__":
    print(buySell([7, 6, 4, 3, 1]))
                
