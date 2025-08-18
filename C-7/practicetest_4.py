n =int(input("Enter ur num "))
for i in range(2,n):
    if(n%i)==0:
        print("NOT A PRIME")
        break
else:
    print("PRIME")    

 