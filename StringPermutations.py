import string

def StringPermute(firstString,secondString):
   '''The function takes in two strings
    It checks if they are of the same length
    If the strings are of different length,they cannot be a permutation of each other 
    If they are of the same length,
    the functiom sorts the two strings and check in they are equal
   '''
   if len(firstString)!=len(secondString):
        return False
   else:
        if sorted(firstString)==sorted(secondString):
            return True
        else:
            return False       


if __name__ =="__main__":
    print(StringPermute("dog","god"))