"""General ₹1,000
Private ₹2,500
ICU ₹5,000
3. Extra charges
Medical test: ₹1,500
Medicine: ₹2,000
4. Conditions (if-elif-else)
Age 18 se kam → Minor Patient
Age 18 ya zyada → Adult Patient
Bill ₹10,000 se zyada → 10% discount
Bill ₹5,000 se ₹10,000 tak → 5% discount
Bill ₹5,000 se kam → No discount
5. List aur Set
Patient ke selected services ko list mein store karo aur set se unique services nikalo.
6. Final bill print karo




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
number_days = int(input("How many Days patient are here: "))
print("1 for General \n 2 for private\n 3 for ICU ")
