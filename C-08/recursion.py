# x =int(input("Enter ur num : "))
# fact =1
# for i in range(1,x+1):
#     fact *=i
# print(fact)   
n =int(input("Enter ur number :"))  
def fact(n):
     
    if(n==1 or n== 0):
       return 1
    else:
        return n*fact(n-1)    
       
        
print(fact(n))