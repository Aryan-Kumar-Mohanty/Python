class calculator:
    @staticmethod
    def greet():
        print("Good morning!!")
    def __init__(self,n):
        self.n=n
        pass
    def square(self):
        print(f"Square of {self.n} is {self.n*self.n}")
    def cube(self):
        print(f"Cube of {self.n} is {self.n**3}")    
    def sqrt(self):
        print(f"Sqrt of {self.n} is {self.n**1/2}")    
a= calculator(4)
a.greet()
a.square()
a.cube()
a.sqrt()
 