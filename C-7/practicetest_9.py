n = int(input("Enter ur num"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
             print("*",end="")
        elif j==0 or j==n-1:
             print("*",end="")
        else:
              print(" ",end="")
    
    print()    
#  
#  n = int(input("Enter the number: "))

# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print("*" * n)
#     else:
#         print("*", end="")
#         print(" " * (n - 2), end="")
#         print("*")
# 