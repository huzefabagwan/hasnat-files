"""
Print numbers from 1 to 20 but stop at 15 using break.
Print numbers from 1 to 20 but skip 10 using continue.
Find the first number divisible by 7 between 1 and 100.
Print only odd numbers using continue.
Stop the loop when the user enters 0.
. Write a program to find whether a given number is prime or not.

5. Write a program to find the sum of first n natural numbers using while loop.

6. Write a program to calculate the factorial of a given number using for loop. 
Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
"""




"""
Q1 , Print numbers from 1 to 20 but stop at 15 using break.
"""

# i = 0
# while i <=20 :
#     if i == 15 :
#         break;
#     else:
#         print(i)

#     i+=1

# for a in range(1 , 21):
#     if a == 15 :
#         break
#     else:
#         print(a)


"""
Print numbers from 1 to 20 but skip 10 using continue.
"""

# i = 0
# while i <= 20 :
#     i+=1
#     if i == 10 :
#         continue   # skip the item
#     print(i)
    

"""
Find the first number divisible by 7 between 1 and 100
"""

# for i in range(1 , 101):
#     if i % 7 == 0 : # used to find reminder 
#         print(i)


""".
 Write a program to find whether a given number is prime or not.
"""

# num = int(input("enter your number to find is prime our not :"))

# i = 1 
# count = 0 
# while i <= num :
#     if num % i  == 0 :
#         7 % 1 == 0 
#         7 % 2 == 0 
#         7 % 3 == 0 
#         7 % 1 == 0 
#         7 % 1 == 0 
#         7 % 7 == 0 
        

#         count+=1 
#     i+=1

# if count == 2 :
#     print(count)
#     print(" prime number ")   
# else:
#     print(count)
#     print("Not prime Number")       



""" 
Write a program to calculate the factorial of a given number using for loop. 
"""


# num = int(input("enter your number to find factorial : ")) #5 * 4 * 3 * 2 *1 
# fact =  1
# for i in range(1 , num+1):
#     print(i)
#     fact = fact * i 
#     print(i)
# print("factorial: " , fact)



# l = ["Harry", "Soham", "Sachin", "Rahul" , "Sonu" , "haSnat" , "aS" , "SSS"]
# for i in l: 
#     if i.startswith("S"):
#         print("hello " , i )



# i = "Hasnat"
# print(i.startswith("Has"))
# print(i.endswith("nat"))

"""5. Write a program to find the sum of first n natural numbers using while loop"""
# print('''hello''')
# print("""hello""")

# n = int(input("enter your number : "))
# a = 0 
# i = 1
# while i <= n :
#     # print(i)
#     a = a + i 
#     i+=1
# print(a)

a = [["hasnat", [24 , 34 ]] , []] 