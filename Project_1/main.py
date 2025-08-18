import random
ran =random.choice([1,0,-1])
print("Your choices are: s for snake, w for water and g for gun.")
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
you = youdict[youstr]
computer =ran
reverse_dict={1: "Snake", -1: "Water", 0: "Gun"}
 
print(f"Computer chose:{reverse_dict[computer]}")
print(f"You chose:{reverse_dict[you]}")
if computer == you:
    print("It's a draw")

else:
    if (computer == -1 and you == 1):
        print("You win!")

    elif (computer == 1 and you == 0):
        print("You lose!")

    elif (computer == 1 and you == -1):
        print("You lose!")

    elif (computer == -1 and you == 0):
        print("You win!")

    elif (computer == 0 and you == 1):
        print("You win!")

    elif (computer == 0 and you == -1):
        print("You lose!")

    else:
        print("Something went wrong!")
