marks1=int(input("Enter marks 1 : "))
marks2=int(input("Enter marks 2 : "))
marks3=int(input("Enter marks 3 : "))
 
tp=(100*(marks1+marks2+marks3 ))/300
if(tp>=40 and marks1>33 and marks2>33 and marks3>33):
    print("you have passed",tp)
else:
    print("You failed :(",tp)    
