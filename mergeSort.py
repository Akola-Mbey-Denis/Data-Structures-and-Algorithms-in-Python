def mergeSort(data):
    print("data splitting")
    if len(data)>1:
        mid=len(data)//2
        right_half=data[:mid]
        left_half=data[mid:]

        mergeSort(right_half)
        mergeSort(left_half)
        i=j=k=0

        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                data[k]=left_half[i]
                i=i+1
            else:
                data[k]=right_half[j]
                j=j+1 
            k=k+1 

        while i<len(left_half):
            data[k]=left_half[i] 
            i=i+1
            k=k+1 

        while j<len(right_half):
            data[k]=right_half[j]
            j=j+1
            k=k+1 
        print("merging " ,data) 

a_list=[12,88,6,7,9,1,4]
mergeSort(a_list) 
print(a_list)       
        

                      

             
 



