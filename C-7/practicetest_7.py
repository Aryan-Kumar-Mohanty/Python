n = int(input("Enter ur num"))

for i in range (0,n+1):
   print(" "*(n-i),end="")
   print("*"*(2*i-1),end="")
   print("\n")