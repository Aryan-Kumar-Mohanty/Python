class Twodvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"{self.i},{self.j}are the values")    
        
class ThreeDvector(Twodvector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k
    def show(self):
        print(f"{self.i},{self.j},{self.k}are the values")       
m=Twodvector(1,2)                
n=ThreeDvector(1,2,3)
n.show()