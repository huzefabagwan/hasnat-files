patient_name = input("Enter Patient Name :- ")
Age = int(input("patient age :- "))
if Age <= 18 :
    patient_type = "Minor patient"
elif Age >= 18 :
    patient_type ="Adult patient"
else :
    print("Invalid age")

print("\n 1 for genral room ,price = 1000rs , \n 2 for private room, price = 2500rs , \n 3 for icu Room,price = 5000rs")
room_type = int(input("Room choice" ))
if room_type == 1 :
   room_amount = 1000
elif room_type == 2 :
   room_amount = 2500
elif room_type == 3 :
    room_amount = 5000
else :
    print("invalid choice")

admit_days = int(input("how many days you admited:- "))
medical_test = int(input("Medical Test (1 for Yes or 2 for No)\n ,price = 1500 rs per day :- "))
medicine = int(input("Medical You want (1 for Yes or 2 for No)\n price = 2000 rs per day :- "))

# ===============================medical==============================
if medical_test == 1 :
   medical_test_amount = 1500
elif medical_test == 2:
    medical_test_amount = 0
    
else : 
    print("Invalid Choice")

# ==========================medicine=============================================
if medicine == 1 :
    medicine_amount = 2000
elif medicine == 2 :
    medicine_amount= 0 
else:
    print("invalid")
# ============================================================= 
total_bill =  (room_amount*admit_days) + medicine_amount  + medical_test_amount
print(total_bill) 
if total_bill > 10000:
    discount = total_bill *(10/100)
elif total_bill > 5000 and total_bill < 10000 :
    # F + T  = T 
    # T + F  = F
    discount = total_bill *(5/100)
elif total_bill < 5000 :
    discount = 0 
else:
    print("invalid input")
# ======================================================================
final_amount = total_bill -  discount
print("*"*50)
print("Total Bill ")
print("*"*50)
print("\n\n")
print(f"Patient Name :- {patient_name}")
print(f"patient Age:-{Age} :-")
print(f"patient Type:-{patient_type} :-")
print("\n\n")
print(f"Room Charges :- {room_amount*admit_days}")
print(f"test Charges:- {medical_test_amount}")
print(f"medicine charges:- {medicine_amount}")
print("\n\n")
print("total bill " , total_bill)
print("discount:- ", discount )
print("final bill:- " , final_amount)
print("\n\n")
print("Status: BILL GENERATED")
# ====================================================================

# if medical_test == 1 or medicine == 1 :
#     total_bill >= 10000 
#     print(medical_test + medicine*admit_days/10)

# elif medical_test == 2 or medicine == 2 :
#     total_bill <= 10000 or total_bill >= 5000 
#     print(admit_days/5)
# elif total_bill <= 5000 :
#     print("No discount Apply")
# elif medical_test == 1 or medicine == 2 :
#     print(medical_test*admit_days) 
# elif medicine == 1 or medical_test == 2 :
#     print(medicine*admit_days)
# else :
#     print("invalid choice")






"""
    # Question: Hospital Billing System Using Python

Write a Python program to develop a Hospital Billing System that calculates a patient's
 final hospital bill based on room charges, medical tests, medicines, and applicable discounts.

### Requirements

**1. User Input**

Accept the following details from the user:
- Patient Name
- Age
- Number of Days Admitted
- Room Type (General / Private / ICU)
- Medical Test Required (Yes / No)
- Medicine Required (Yes / No)

**2. Room Charges Per Day**

Calculate room charges according to the selected room type:
- General Room: ₹1,000 per day
- Private Room: ₹2,500 per day
- ICU: ₹5,000 per day

**3. Extra Charges**

Add the following charges if the services are selected:
- Medical Test: ₹1,500
- Medicine: ₹2,000

**4. Conditional Statements (if-elif-else)**

Use conditional statements to perform the following operations:
- If the patient's age is below 18, display **Minor Patient**.
- If the patient's age is 18 or above, display **Adult Patient**.
- If the total bill is greater than ₹10,000, apply a 10% discount.
- If the total bill is between ₹5,000 and ₹10,000 (inclusive), apply a 5% discount.
- If the total bill is below ₹5,000, no discount will be applied.

**5. List and Set**

- Store the patient's selected services in a list.
- Use a set to obtain unique services.

**6. Final Bill Generation**

Display the following details:
- Patient Name and Age
- Patient Category (Minor / Adult)
- Room Type and Number of Days
- Selected Services
- Room Charges
- Extra Charges
- Total Bill Before Discount
- Discount Percentage and Discount Amount
- Final Bill Amount After Discount

### Objective

To understand and implement user input, 
variables, conditional statements, lists, sets, and arithmetic operations in Python by
 developing a Hospital Billing System.
================================
      HOSPITAL BILL
================================
Patient Name: Huzefa
Age: 20
Patient Type: Adult

Room: Private
Days: 3

Room Charges: ₹7500
Test Charges: ₹1500
Medicine Charges: ₹2000

Total Bill: ₹11000
Discount: ₹1100
Final Bill: ₹9900

Status: BILL GENERATED
================================


"""