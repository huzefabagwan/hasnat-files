"""
1. String Slicing

Definition: String slicing is used to extract a 
specific part of a 
string using 

syntax:
[start:stop:step].

[start : stop : step ]


2. String Reverse:

Definition: String reverse means arranging the characters of 
a string from last to first using a negative step -1."""

name = "hasnat" # sclicing start from 0 
#[0 , 1 , 2 , 3 ,4 , 5 ]
print(name[1:3])
# positive step [0 , 1 , 2 ,3 .......n-1]
a = [ 1 ,2, 3, 4, 5 , 6 ,7 , 9 , 10 ]
# neagtive step [n-1 ............, -3  -2, -1 ]
print(a[0:6])
print(a[:11:4]) 
print(a[3:6:2])

s = "Hasnat shaikh"
print(s[0:8])

rev = "hasnat"
print(rev[::-1])
print(rev[-6:]) # -2 - 1 = -3 
print(rev[-1: -6 ]) # -6 - 1  = -7
print(rev[::-1])



# stop [n-1] 