x = int(input("Enter your number (1 or 2) :"))
match x:
    case 1:
        print("you chose 1 yipeee")
    case 2:
        print("you chose 2.oh no")   
    case _:
        print("you entered invalid num , you lost everything") 