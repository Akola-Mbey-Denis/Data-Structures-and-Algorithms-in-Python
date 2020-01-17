def short_bubble_sort(list):
    exchanges =True 
    pass_num =len(list)-1
    while pass_num>0 and exchanges:
        exchanges=False
        for i in range(pass_num):
            if list[i]>list[i+1] :
                exchanges=True 
                temp =list[i]
                list[i]=list[i+1]
                list[i]=temp 
        pass_num=pass_num-1 
    return list    



def selectionSort(a_list):
     
    for  i in range(len(a_list)-1,0,-1):
        pos_of_max=0
        for j in range(1,i+1):
            if a_list[j]>a_list[pos_of_max]:
                pos_of_max=j
        temp =a_list[j]
        a_list[i]=a_list[pos_of_max]
        a_list[pos_of_max]=temp 
    return a_list 


def insertionSort(test_list):
    for i in range(0,len(test_list)):
        current_value =test_list[i]
        position =i 
        while position>0 and test_list[position-1]>current_value:
            test_list[position]=test_list[position-1]
            position=position-1 

        test_list[position]=current_value
    return test_list 


# def shell_sort(test_list):
#     sublist_count=len(test_list)//2
#     while sublist_count>0:
#         for i in range(sublist_count):
#             gap_insertion(test_list,i,sublist_count)
#         print("After increments of size", sublist_count, "The list is",test_list)
#         sublist_count=sublist_count//2 
     

# def gap_insertion(a_list,start,gap):
#     for j in range(start+gap,len(a_list),gap):
#         current_value=a_list[j]
#         position =j

#         while position>=gap and a_list[position-gap]>current_value:
#             a_list[position]=a_list[position-gap]
#             position=position-gap 

#         a_list[position-gap]=current_value   

            
def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is",        a_list)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
    while position >= gap and a_list[position - gap] >current_value:
        a_list[position] = a_list[position - gap]
        position = position - gap
        a_list[position] = current_value
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)








if __name__ =="__main__":
    list_1=[12,45,90,11,5,2,7,34,0,78,22]  
    print(shell_sort(list_1))
    print(list_1)