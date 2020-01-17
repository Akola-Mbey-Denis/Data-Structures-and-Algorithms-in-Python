def distint_numbers(list):
    count=0
    if len(list)==0:
        return 0
    elif len(list)==1:
        return 1
    else:    
        for k in range (0,len(list)-1):        
            if list[k]==list[k+1]:
                del list[k]

                 
    return len(list)

if __name__=="__main__":
    print(distint_numbers([1,1,2]))         
