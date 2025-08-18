class employee:
    def __init__(self):
        
        print("i am the constructor of employee")
    a=1    
class programmer(employee):
    def __init__(self):
        super().__init__()
        print("i am the constructor of programmer")
    b=2
      
class manager(programmer):
    def __init__(self):
        super().__init__()
        print("i am the constructor of manager")
    c=3
d=manager()
print(d.a)   