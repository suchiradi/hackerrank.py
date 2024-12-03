def swapcase(s):  #s is a parameter
    result =" "   #storing an empty string
    for i in s:   #for loop to run through the entire string s
        if i.islower():  #i.islower() checks if the letter is lower case. If it is lower case it will convert it into upper case.
            result+=i.upper()  #the updated letter after conversion is stored in result
        elif i.isupper(): #i.upper() checks if the letter is uppercase. If it is in uppercase ,it will convert it into lower case.
            result+=i.lower()   #the updated letter is stored in the result 
        else:
            result+=i   #if other elements except letters are presented in the the string then it will remian unchanged
    return result

s=input("Enter a string : \n")
final=swapcase(s)  #free variable : stores the function into it
print(final)       # free variable is called