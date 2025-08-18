with open("file.txt") as f: 
    c=f.read()
with open("fil.txt") as f:
    c1=f.read()
if(c==c1):
    print("Identical")
else:
    print("Not identical")        
