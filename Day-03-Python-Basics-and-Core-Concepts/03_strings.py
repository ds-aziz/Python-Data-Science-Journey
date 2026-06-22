
print('baloch')
print("i am 25 year old")

print("""
i am aziz baloch.
i have completed my BS Statistics Degree,
i am 25 year old
""")

#Assignment: what is type casting and how do we use in python.

""""Type Casting ka matlab hai ek data type ki value ko dusre data type mein badalna. 
Python mein kabhi-kabhi humein integer (number) ko string (text) mein ya float (decimal wala number) ko 
integer mein convert karne ki zaroorat padti hai.
Kyun karte hain? Kyunki Python mein hum har do cheezon ko aapas mein jod (concatenate) nahi sakte. 
Maslan, agar tum ek text aur ek number ko + karoge, to error aayega.
Kaise karte hain? Python mein functions use hote hain: int(), float(), aur str()."""

#Example:
age = 25
# Agar hum print("My age is " + age) likhenge to error aayega.
# Isliye hum age ko string mein cast karenge:
print("My age is " + str(age))