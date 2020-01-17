def reverseString(string):
    if len(string)==1:
        return string 
    else:
        return reverseString(string[1:])+string[0]    

def Palindrome(string):
    string= string.lower()
   
    punctuations = '''!()-[]{};: '"\,<>./?@#$%^&*_~'''
    new_sent =""
     
    for k in string:
        if not k in punctuations:
            new_sent=new_sent+k 
     
      
     
    return new_sent== reverseString(new_sent)

if __name__ =="__main__":
    test_cases =[ "madam i'm adam","aibohphobia","Live not on evil","Reviled did I live, said I, as evil I did deliver",
                 "Go hang a salami; I'm a lasagna hog","Able was I ere I saw Elba","Too hot to hoot"]
    for testcase in range(0,len(test_cases)):
        print("Test case",testcase+1, ": ",Palindrome(test_cases[testcase]))             
 
         