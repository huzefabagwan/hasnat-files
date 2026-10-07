import random 

data = ["stone" ," paper " , "scissor"]
pc_choice = random.choice(data)


user_choice = input("enter your choice : ").lower()
if user_choice == pc_choice:
    print("b6match Tie ")
    print(pc_choice , user_choice)
elif user_choice == "stone" and pc_choice == "paper":
    print("You loss Pc win ")
    print(pc_choice)
elif user_choice == "paper" and pc_choice == "stone":
    print("You win pc loss")
    print(pc_choice)
elif user_choice == "scissor" and pc_choice == "stone":
    print("You loss Pc win ")
    print(pc_choice)
elif user_choice == "stone" and pc_choice == "scissor":
    print("You loss Pc win ")
    print(pc_choice)
elif user_choice == "paper" and pc_choice == "scissor":
    print("pc win you loss ")
    print(pc_choice)
elif user_choice == "scissor" and pc_choice == "paper":
    print("You win pc loss")
    print(pc_choice)
else:
    print("invalid choice")

