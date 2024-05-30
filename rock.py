import random
user_choice=int(input("Type 0- for rock, 1- for paper, 2- for scissor --- choose your number:"))
computer_choice=random.randint(0,2)
print("Computer choose:",computer_choice)
if user_choice  <0 or user_choice >2:
    print("Please use a valid Number!")
elif user_choice==computer_choice:
    print("Drawn.")
elif user_choice == 0 and computer_choice == 2:
    print("You win.")
elif user_choice == 2 and computer_choice == 0:
    print("You lose.")
elif user_choice > computer_choice:
    print("You win.")
elif computer_choice > user_choice:
    print("You lose.")
    
