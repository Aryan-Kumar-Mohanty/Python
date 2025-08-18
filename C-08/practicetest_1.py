def great():
    a =int(input("Enter the number "))
    b =int(input("Enter the number "))
    c =int(input("Enter the number "))
    if(a>b and a>c):
       return a
    elif(b>a and b>c ):
       return b
    elif(c>a and c>b ):
        return c
    
print(great())   