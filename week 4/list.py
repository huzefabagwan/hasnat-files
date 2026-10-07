"""
A list is a collection of multiple items stored in a
 single variable in python 
,list are created using square brackets []
"""


# fruits = [ "apple" , "orange" , "banana " , "mango" ,
#            234 , 234.6 , True ]
# print(fruits)


# # indexing start from 0
# # print(fruits[2][2])
# # print(fruits[0])
# # print(fruits[6])

# #slicing  on list 
# print(fruits[0:3:2])
# print(fruits[0:3])


# # add iteams 
# fruits.append("papaya")
# print(fruits)


# fruits.insert(1 , "KIWI") # syntex[index_number , "name of iteam"]
# print(fruits)

# # update 
# fruits[1] = "papaya"
# print(fruits)


# #multiple value add  
# fruits.extend(["apple" , "kiwi"])
# print(fruits)



# remove 

fruits = [ "apple" , "orange" , "banana " , "mango" ,
           234 , 234.6 , True ]


# fruits.remove("apple")
# print(fruits)

# fruits.pop()
# print(fruits)

# del fruits[3]
# print(fruits)


print(fruits.index("mango"))

print("apple" in fruits)
print("hasnat" not in fruits)


  


