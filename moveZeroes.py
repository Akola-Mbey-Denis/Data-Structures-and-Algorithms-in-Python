def moveZero(test_list):
    for i in range(0,len(test_list)-1):
        for j in range(i,len(test_list)):
          
             
                if test_list[i]==0 and test_list[j]!=0:

                
                
                    temp =test_list[j]
                    test_list[j]=test_list[i]
                    test_list[i]=temp 

         
    return test_list


if __name__ =="__main__":
    testcase =[55, 20, 40, 47, 32 ,52, 37, 11, 84, 83, 55, 25, 27 ,88 ,96, 7, 18,
     14, 45, 98, 2, 95, 87, 69, 44, 44, 36, 28 ,37, 64, 92,56, 93 ,39 ,54, 22, 30, 0, 
     70, 22 ,74, 99, 73, 53, 49 ,88, 55 ,96, 32, 32, 11, 34, 60, 93, 11, 91, 47, 15, 42,
     67, 32, 54 ,36, 50, 18, 89, 13, 13, 59, 14, 60,
     78 ,17, 11 ,9 ,87 ,88 ,27, 17 ,37, 65, 45 ,73, 94, 70, 91 ,62 ,47 ,15,
      36, 87, 83, 45 ,15, 68, 3, 17, 55]
    print(moveZero(testcase))             


