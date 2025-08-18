class employee:
    a=1
class coder:
    b=2
class programmer(employee,coder):
    c=3
d=programmer
print(d.a,d.b,d.c)    