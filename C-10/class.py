class Employee:
     
    language="py"#<----this is an class attribute
    salary=1000000000
 

 
aryan=Employee()
aryan.name="Aryan"#<----- this is an instance attribute
print(aryan.name,aryan.language,aryan.salary)    
 
harry=Employee()
harry.name="harry"
print(harry.name,harry.salary,harry.language)    