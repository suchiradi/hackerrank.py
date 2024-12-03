def swapcase(s):
    result =" "
    for i in s:
        if i.islower():
            result+=i.upper()
        elif i.isupper():
            result+=i.lower()
        else:
            result+=i
    return result

s=input("Enter a string : \n")
final=swapcase(s)
print(final)    