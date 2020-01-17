def quickSort(test_data):
    quick_sort_helper(test_data,0,len(test_data)-1)
    return test_data


def quick_sort_helper(data,first,last):
    if first<last:
        split_point=partition(data,first,last)
        quick_sort_helper(data,first,split_point-1)
        quick_sort_helper(data,split_point+1,last)

def partition(data,first,last):
    pivot_value =data[first]
    left_mark=first+1 
    right_mark =last 
    done =False
    while not done:
        while left_mark<=right_mark and data[left_mark]<pivot_value:
            left_mark=left_mark+1

        while data[right_mark]>=pivot_value and right_mark>=left_mark:
            right_mark=right_mark-1 

        if right_mark<left_mark:
            done =True
        else: 
            temp = data[left_mark]
            data[left_mark] = data[right_mark]
            data[right_mark] = temp            

        temp =data[first]
        data[first]=data[right_mark]
        data[right_mark]=temp 
        return right_mark            


if __name__=="__main__":
    print(quickSort([12,67,34,32,90,78,43,11]))