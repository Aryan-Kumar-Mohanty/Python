try:
    a=int(input("Enter ur number "))
    b=int(input("Enter ur number "))
    print(a/b)
except ZeroDivisionError as z :
    print("Infinite")
