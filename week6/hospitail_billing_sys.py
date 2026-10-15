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
================================"""




patient_name = input("Enter Patient Name: ")
patient_Age = int(input("entre patient Age: "))
print("1 for General ( ₹1,000 per day) \n 2 for private (₹2500 per day)\n 3 for ICU(₹5,000 per day) ")
room_type = int(input("enter your choice : "))
days = int(input("Enter Number of Days Admitted : "))
medical = input("Medical test required (yes our no ): ").lower()
Medicine = input("enter you want Medicine(yes our no ): ")

if room_type == 1:
    room_type = 1000
    room = "Gen"
elif room_type == 2 :
    room_type = 2500
elif room_type == 3 :
    room_type = 5000
# ======================================================
# patient_type :
if patient_Age < 18:
    patient_type = "Minor patient"
elif patient_Age > 18 :
    patient_type = "Adult patient"
# ====================================================

if medical == "yes":
    medical = 1500 
else:
    medical= 0 
 
if Medicine == "yes":
    Medicine = 2000
else:
    Medicine = 0 
# =======================calculation ===============
room_amount = room_type * days

total_amount = room_amount + medical + Medicine 

# =====================discount==============================
discount = 0 
if total_amount > 10000:
    discount = total_amount*(10/100)
    final_amount = total_amount - discount
elif total_amount >5000 and total_amount < 10000:
    discount = total_amount*(5/100)
    final_amount = total_amount - discount
elif total_amount < 5000 :
    discount = 0 
    final_amount = total_amount - discount

# ========================final amount========================================

print(f"Patient Name:- {patient_name}")
print(f"patient Age:- {patient_Age}")
print(f"patient Type:- {patient_type}")
print("\n")
print(f"Room Type : {room_type}")
print(f"Days:-{days}")
print("\n")
print(f"Room charges : {room_amount}")
print(f"Test charges : {medical}")
print(f"Medicien charges : {Medicine}")
print("\n")
print(f"Total Bill : {total_amount}")
print(f"Discount : {discount}")
print(f"Final Amount  : {final_amount}")
print(f"Status:BILL GENERATED")




