def bubble_sort(list):
    temp=0
    for i in range(len(list)-1,0,-1):
        for k in range(i):
            if list[i]<list[k]:
                temp =list[i]
                list[i]=list[k] 
                list[k]=temp
    return list