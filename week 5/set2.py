"""
1. Union

Definition: Union do sets ke saare unique elements ko combine karta hai.

A = {1, 2, 3}
B = {3, 4, 5}

A.union(B)
# {1, 2, 3, 4, 5}


2. Intersection

Definition: Intersection do sets me common elements ko return karta hai.

A = {1, 2, 3}
B = {3, 4, 5}

A.intersection(B)
# {3}


3. Difference

Definition: Difference pehle set ke woh elements return karta hai jo dusre set me present nahi hain.

A = {1, 2, 3}
B = {3, 4, 5}

A.difference(B)
# {1, 2}
"""


# union set
# a = {1 , 2 , 3 ,  9 , 9 ,6 , 6 , 7 }
# b = { 3 , 4 , 5 , 6  , 7 , 7 , 9 , 9 }

# print(b.union(a))
# print(a.union(b))


# intersection set 

# a = {1 , 2 , 3 ,  9 , 9 ,6 , 6 , 7 }
# b = { 3 , 4 , 5 , 6  , 7 , 7 , 9 , 9 }

# print(b.intersection(a))


# diffrance


a = {1 , 2 , 3 }
b = {1 , 2 , 4}
print(b.difference(a))

#(total_marks / 500)*100 