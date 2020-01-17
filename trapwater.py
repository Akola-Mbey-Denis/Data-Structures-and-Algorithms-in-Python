def trapWater(test_array):
    sum=0
    for i in range(0,len(test_array)-1):
        if test_array[i]>test_array[i+1]:
            sum=sum+(test_array[i]-test_array[i+1])


    return sum 

if __name__ =="__main__":
    print(trapWater([2,0,4,0,6,1,7 ]))            

