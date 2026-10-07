# names = ["hasnat" , "hassan" , "muddassir" ]
# user = input("enter your name : ")
# if user in names:
#     print("yes" , user , " in  the list ")
# else:
#     print("NO your name  is not present in list " )


number = [ 1 , 2 , 3 , 4 ,5 ,  6]
number.append(20)
number.sort()
number.reverse()
number.pop()
number.clear()
number.append(23)
number.insert(0 , 12)
number.extend([23 , 56])


print("sum : " , sum(number) )
print(number)
    