f=open("poem.txt")
c=f.read()
if("twinkle"in c):
    print("twinkle is present")
else:
    print("word not present")    
f.close()