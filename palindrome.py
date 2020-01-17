from deque import Deque 
def brute_force_version(test_string):
    return test_string==test_string[::-1]
 


def isPalindrome(test_string):
    queue =Deque()
    stillTrue=True
    for k in test_string:
        queue.add_rear(k)

    while queue.size()>1 and stillTrue:
        first=queue.remove_front()
        second=queue.remove_rear()    

        if first!=second:
            stillTrue=False
        else:
            stillTrue=True

    return stillTrue   
                




if __name__ =="__main__":
    print(brute_force_version("madam"))
    print(isPalindrome("madam"))