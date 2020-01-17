import math
def findSquareRoot(number):
    try:
        print(math.sqrt(number))
    except:
        print('Bad value for square root') 
        print('using absolute value instead') 
        print(math.sqrt(abs(number))) 

def findSquare(number):
    if number<0:
        raise RuntimeError("You can't use a negative number!")
    else:
        return number*number




if __name__=="__main__":
    number =int(input("Enter a number:")) 
    findSquareRoot(number)
    print(findSquare(number))


     