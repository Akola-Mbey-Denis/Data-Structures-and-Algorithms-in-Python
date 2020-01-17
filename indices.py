def sumIndices(test_list,target):
    indices=[]
    for i in range(0,len(test_list)-1):
        for j in range(i,len(test_list)):
            if test_list[i]+test_list[j]==target:
                indices.append(i)
                indices.append(j)
                return indices


if __name__ =="__main__":
     print(sumIndices([2, 7, 11, 15],26))               

