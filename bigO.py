def findMaximumElement(List):
    max=List[0]
    for k in range(1,len(List)):
        if List[k]>max:
            max=List[k]
        else:
            NotImplemented
    return max


def secondMethod(List):
    max=0
    for k in range(0,len(List)):
        for j in range(1,len(List)):
            if List[k]>List[j]:
                max=List[k]
            else:
                max=List[j]
    return max                



     
if __name__ =="__main__":
    print(secondMethod([12,45,89,1,3,67,110,120]))     