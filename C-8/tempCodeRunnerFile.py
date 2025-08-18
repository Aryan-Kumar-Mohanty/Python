def pattern(i):
    if(i==0):
        return
    print("*"*i)
    pattern(i-1)
i =int(input("Enter the no of rows "))
pattern(i) 