accounts = {
    3335:
            {
                "Name":"Hasnat",
                "phone number":9865325632,
                "Account_type": "Saving" ,
                "balance":89562


            },
            
     3336:     
                        {
                            "Name":"uxair",
                            "phone number":6865325632,
                            "Account_type": "Saving",
                              "balance":89562
                            
            
                        },
    3337:
                                    {
                                        "Name":"hassan",
                                        "phone number":9865356632,
                                        "Account_type": "Saving",
                                          "balance":89562
                                        
                        
                                    }
            
        }


print("\n1 for Details \n2 for View Balance \n3 for Widthdrawal Amount\n4 for Deposit Amount  ")
user_choice = int(input("Enter Your Choice :- "))
account_number = int(input("Enter Your Account Number: - "))
if account_number in accounts:
    if user_choice == 1 :
        print(accounts[account_number])
    elif user_choice == 2 :
        print(f"Your Balance is :- {accounts[account_number]["balance"]}")
    elif user_choice == 3 :
        Withdrawal_amount = int(input("Enter Your Withdrawal Amount :- "))
        if Withdrawal_amount <= accounts[account_number]["balance"]:
            accounts[account_number]["balance"] -= Withdrawal_amount
            print(f"Your Remaining Balance is {accounts[account_number]["balance"]}")
        else:
            print("Insufficient Balance")
    elif user_choice == 4 :
        deposit_amount = int(input("enter your amount :- "))
        accounts[account_number]["balance"]+=deposit_amount
        print("Deposite Successfull")     
        print("your balance:-", accounts[account_number]["balance"])        
else:

            
        pass 

