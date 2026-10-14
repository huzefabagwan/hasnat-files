
# 1. Tuple kya hai in Python?
# Definition: A tuple is an ordered collection of elements that is immutable, meaning its elements cannot be changed after creation.
# Hinglish mein: Tuple ek aisa collection hai jisme multiple values store kar sakte hain, lekin tuple banne ke baad uski values change nahi kar sakte.
# Example:
# student = ("Huzefa", 20, "Python", 85.5)print(student)



# Output:
# ('Huzefa', 20, 'Python', 85.5)


# Yahan tuple mein 4 elements hain: ek string, ek integer, ek string aur ek float.
# 2. Tuple ki main properties
# - Ordered: Elements ka order fixed rehta hai.
# - Immutable: Elements ko change, add ya remove nahi kar sakte.
# - Allows duplicates: Same value multiple times ho sakti hai.
# - Different data types: String, integer, float etc. store kar sakte hain.
# - Indexed: Har element ka index hota hai, jo 0 se start hota hai.
# 3. Tuple kaise create karte hain?
# 1. Empty tuple
# t = ()print(t)



# Output: ()

# 2. Multiple elements wala tuple
# t = (10, 20, 30, 40)print(t)



# Output: (10, 20, 30, 40)

# 3. Single-element tuple
# t = (10,)print(type(t))



# Output: <class 'tuple'>
# Important: Single element ke baad comma , lagana zaroori hai.

# 4. Without parentheses
# t = 10, 20, 30print(t)



# Output: (10, 20, 30)


# 4. Tuple ke operations
# Python mein tuple ke important operations ye hain:
# 1. Indexing
# Index ki help se specific element access karte hain.
# t = (10, 20, 30, 40)print(t[0])print(t[2])print(t[-1])



# Output:
# 10
# 30
# 40


# - Positive indexing 0 se start hoti hai.
# - Negative indexing -1 last element ko access karti hai.
# 2. Slicing
# Tuple ka ek particular portion nikalne ke liye slicing use hoti hai.
# t = (10, 20, 30, 40, 50)print(t[1:4])print(t[:3])print(t[2:])print(t[::-1])



# Output:
# (20, 30, 40)
# (10, 20, 30)
# (30, 40, 50)
# (50, 40, 30, 20, 10)


# Yaad rakho: t[1:4] mein index 1 include hota hai, lekin index 4 include nahi hota.
# 3. Concatenation (+)
# Do tuples ko combine karne ke liye.
# a = (10, 20)b = (30, 40)print(a + b)



# Output: (10, 20, 30, 40)
# 4. Repetition (*)
# Tuple ko multiple times repeat karne ke liye.
# t = (1, 2)print(t * 3)



# Output: (1, 2, 1, 2, 1, 2)
# 5. Membership (in, not in)
# Check karne ke liye ki element tuple mein hai ya nahi.
# t = (10, 20, 30)print(20 in t)print(50 not in t)



# Output:
# True
# True


# 6. Iteration
# Loop ki help se tuple ke har element ko access karna.
# t = (10, 20, 30)for x in t:    print(x)



# Output:
# 10
# 20
# 30


# 7. Length (len())
# Tuple mein total elements count karne ke liye.
# t = (10, 20, 30, 40)print(len(t))



# Output: 4
# 8. Minimum aur Maximum
# t = (40, 10, 30, 20)print(min(t))print(max(t))



# Output:
# 10
# 40


# 9. Sum (sum())
# Tuple ke numeric elements ka total nikalne ke liye.
# t = (10, 20, 30)print(sum(t))



# Output: 60
# 10. Comparison
# Tuples ko compare bhi kar sakte hain.
# a = (10, 20)b = (10, 30)print(a < b)



# Output: True
# Python pehle corresponding elements compare karta hai. Yahan 10 == 10, phir 20 < 30, isliye result True hai.
# 5. Tuple ke built-in methods
# Python tuple ke paas sirf 2 built-in methods hain.
# 1. count()
# Tuple mein kisi value ke kitne occurrences hain, woh count karta hai.
# t = (10, 20, 10, 30, 10)print(t.count(10))



# Output: 3

# 2. index()
# Kisi value ka pehla index return karta hai.
# t = (10, 20, 30, 20)print(t.index(20))



# Output: 1
# 20 do baar hai, lekin index() pehli occurrence ka index deta hai.

# Exam point: append(), remove(), insert(), pop() aur sort() tuple ke methods nahi hain, kyunki tuple immutable hota hai.
# 6. Tuple immutable kaise hai?
# t = (10, 20, 30)t[1] = 50print(t)



# Output mein TypeError aayega, kyunki tuple ke elements ko directly modify nahi kar sakte.
# Lekin tuple ko list mein convert karke change kar sakte hain:
# t = (10, 20, 30)my_list = list(t)my_list[1] = 50t = tuple(my_list)print(t)



# Output: (10, 50, 30)
# Yahan original tuple ko directly modify nahi kiya; list bana kar naya tuple create kiya hai.
# 7. Tuple aur List mein difference
# Tuple	List
# Parentheses () commonly use hote hain	Square brackets [] use hote hain
# Immutable hota hai	Mutable hoti hai
# Elements directly change nahi kar sakte	Elements change kar sakte hain
# 2 built-in methods: count(), index()	Multiple methods, jaise append(), remove()
# Fixed data ke liye useful	Frequently changing data ke liye useful
# Example:
# a = (10, 20, 30)  # Tupleb = [10, 20, 30]  # List



# 8. Tuple unpacking
# Tuple ke elements ko alag-alag variables mein assign karna tuple unpacking kehlata hai.
# student = ("Huzefa", 20, 85)name, age, marks = studentprint(name)print(age)print(marks)



# Output:
# Huzefa
# 20
# 85


# Variables ki count aur tuple elements ki count normally same honi chahiye.
# 9. Nested tuple
# Jab ek tuple ke andar doosra tuple hota hai, use nested tuple kehte hain.
# t = (10, 20, (30, 40))print(t[2])print(t[2][0])



# Output:
# (30, 40)
# 30


# 10. Tuple se related important functions aur operations — revision
# Operation / function	Use
# len(t)	Elements ki count
# t[index]	Element access karna
# t[start:end]	Slicing
# t1 + t2	Concatenation
# t * n	Repetition
# x in t	Membership check
# min(t)	Minimum value
# max(t)	Maximum value
# sum(t)	Numeric elements ka sum
# t.count(x)	Value ki occurrences count karna
# t.index(x)	Value ka first index
# tuple(iterable)	Iterable ko tuple mein convert karna
# for x in t	Elements par iterate karna
# a, b = t	Tuple unpacking
# Note: min(), max() aur sum() jaise functions tabhi valid hote hain jab unke liye data suitable ho."""
# """