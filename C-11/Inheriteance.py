class Employee:
    company ="ITC"
    def show(self):
        print(f"The name is {self.name} & the salary is {self.salary}")
class Programmer(Employee):
    company="Infotech"
   
         
    def showlang(self ):
        print(f"The name is{self.name }& he is good at {self.lang}")
a=Employee
b=Programmer("raj","py")
print(a.company,b.company)                
