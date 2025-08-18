class Employee:
     
    language="py"#<----this is an class attribute
    salary=1000000000
    def getinfo(self):
        print(f"The language is :{self.language},and the salary is :{self.salary}")
    @staticmethod
    def greet():
        print("good morning")

 
aryan=Employee()
aryan.name="Aryan"
aryan.language="Java"#<----- this is an instance attribute more priortised than class atribute
print(aryan.name,aryan.language,aryan.salary) 
aryan.getinfo()  
aryan.greet() 
 
harry=Employee()
harry.name="harry"
print(harry.name,harry.salary,harry.language)    
