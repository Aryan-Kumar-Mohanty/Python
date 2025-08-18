def sumofn(i):
    if(i==1):
        return 1
    return sumofn(i-1)+i
i=int(input("enter the num of n nummbers "))
print(sumofn(i))