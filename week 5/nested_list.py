# what is nested list 
# Nested List: A list inside another list is called a nested list in Python 

# syntax:
# a = [1  , 2 , 4 [ 3 , 5 ,6 ]]


number = [1 , 2 ,3 ,4 ,5 ,6 , 
          [7 , 8 , 9 ,10 ,  
           [11 , 12 , 13 , 14]
             , ["huzefa" , "hasnat"]
             ,[23.4 , 90.78]
             ]
             
             , [True , False] ]

print(number[1])
# print(number[6])
print(number[6][4])


a = [1 , 2 , 3 ,[4 , 5 ,[6 , 7 , [8 , 9]]], ["hasnat" , "raza"] , ["hassan"]]
print(a[3][2][2][1])
print(a[4][1], a[5][0])


# nested list convert into single list 

a = [[1, 2 ] , [3 , 4] ,  [5 , 6 ]]
single_list= a[0] + a[1] + a[2]
print(single_list)


# sum of all list 
a = [[1, 2 , 10 ] , [3 , 4] ,  [5 , 6 ] ,[ 9 ] ]

sum_all = sum(a[0]) + sum(a[1]) + sum(a[2] + a[3][0])  
# 1 , 2 , 10 = 13 
# 3 + 4 = 7 
# 5 + 6 = 11 
# 13 + 7 + 11 + 9 = 40 

# sum_all = sum(a)
print(sum_all) 
print(a[3][0])

