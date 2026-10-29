# student = {
#     "name":"hasnat",
#     "Python":56 , 
#     "Java":89 , 
#     "Sql":85 
# }
# total = student["Python"]+ student["Java"] + student["Sql"]
# print("student_namee " , student["name"])
# print("total_marks =" ,  total)






accounts = {
   9860:{
       "name":"hasnat",
       "phone number" : 998989889,
       "account type" : "Saving" ,
       "balance": 78992
       ,
       "fulldetails":{
        "adhar_number" : {
            "number":8964534337387387

        }
       }

   } ,
   9861:{
       "name":"muddassir",
       "phone number" : 998959887,
       "account type" : "Saving",
        "balance": 78922
   } ,
   9862:{
       "name":"hassan",
       "phone number" : 998899889,
       "account type" : "Saving",
        "balance": 78992
   } ,
   9863:{
       "name":"mahtab",
       "phone number" : 9586989889,
       "account type" : "Saving",
        "balance": 78912
   } ,
   9864:{
       "name":"uzair",
       "phone number" : 9989565589,
       "account type" : "Saving",
        "balance": 28992
   } 
}

user_choice = int(input("Enter Your 4 digit account Number :- "))
if user_choice in accounts:
    print("name:",accounts[user_choice]["name"] )
else:
    print("Your Account Number is not present in this bank please cheack the bank detail /")