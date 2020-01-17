def UniqueCharacter(test_string):
    for k in range(0,len(test_string)):
        if test_string.count(test_string[k])==1:
            return k 

if __name__=="__main__":
    print(UniqueCharacter("loveleetcode"))

       