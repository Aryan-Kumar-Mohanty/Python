class employee:
    a=1
class programmer(employee):
    b=2
class manager(programmer):
    c=3
d=manager
print(d.a,d.b,d.c)    