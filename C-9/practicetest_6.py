# with open("log.txt") as f:
#     c =f.read()
# if("python" in c):
#     print("python is present") 
# else:
#     print("not present")       
with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes python is present. Line no: {lineno}")
    lineno += 1
else:
    print("No Python is not present")
