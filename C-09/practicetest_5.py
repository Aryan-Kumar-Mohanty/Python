word="Donkey".lower()
with open("donkey.txt") as f:
    c=f.read()
cnew=c.replace(word,"#####")
with open("donkey.txt","w") as f:
    f.write(cnew) 