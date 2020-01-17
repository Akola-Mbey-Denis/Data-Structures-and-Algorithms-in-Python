def urlify(in_string, in_string_length):
    return in_string[:in_string_length].replace(' ', '%20') 


# def replaceCharacters(in_string,stringLength):
#     for i in range(0,stringLength):
#         new_string=" "
#         if in_string[i]==' ':
#             in_string.replace(' ','%20')
          
#     return new_string       



if __name__ =="__main__":
    print(urlify("Welcome to Ghana  ",16))    

                 


