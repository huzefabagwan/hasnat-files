
user_name = input("Enter your name : ")

user_age = int(input("enter your age : "))
if user_age >= 18 :
    print("Room Types \n 1 for Normal Room , price = 1500 \n 2 for Deluxe Room , price 2500 \n 3 for Premium Room , price = 4000")
    room_type = int(input("Which room you want :-  "))
    days = int(input("How many days  :- "))
    if room_type == 1 :
        room_cost = 1500* days
    elif room_type == 2 :
         room_cost = 2500* days   
    elif room_type == 3 :
        room_cost = 4000* days
    else:
         print("enter corect choice ")
        #  ========================================================
    food = input("you want food (Yes or No) price per day = 500 :- ")
    ac= input("enter you want ac (Yes or No ) price per day = 300:- ")  
    # ================================================================
    if food == "yes" :
         food_cost = 500*days

    else:
         food_cost = 0 
     # ===============================================================
    if ac == "yes" :
         ac_cost = 300*days
    else:
        ac_cost = 0 
    # ===============================================================
    print(ac_cost , food_cost , room_cost)
    total = (room_cost + food_cost + ac_cost)
    discount = 0
    if food == "yes" and ac == "yes" :
        discount = total * 10 / 100

    if total > 5000 :
            discount = discount + (total * 5 / 100
)


    final_amount = total - discount


    print("========================================================")
    print("        This is your bill           ")
    print("========================================================")
    print("Customer : " , user_name)
    print("Customer Age :" , user_age) 
    
   
    
    
    print(f"Room cost : \t\t ₹{room_cost}")
    print(f"Food cost : \t\t ₹{food_cost}")
    print(f"AC cost : \t\t ₹{ac_cost}")




     
    print(f"Total cost: ₹{total}")
    print(f"Discount : ₹{discount}")
    print(f"Final Amount : ₹{final_amount}")

    print("Booking is Confrom ")
    print("Thanks For Choicing My hotel Room")

    print(20*"*")
    
    
else:
    print("Booking is not allow ")









