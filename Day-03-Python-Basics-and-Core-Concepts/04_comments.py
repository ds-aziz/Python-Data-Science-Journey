#Subject of this python script:
#Authored by: Aziz Baloch
#Where to contact: github profile link "OR" email (gmail) google collab


#step-1: why we using single qoutation?
print('Aziz') #when we writing a string

#step-2:why we use double qoutation?
print("Aziz")
print("Aziz's book") #when writing strings and making use of other qoutation marks

#step-3: why we use triple qoutation?
print("""
Aziz
baloch
25
""") #To write multiple lines of string and also using """ or '' inside the string

#Assignment: why to use comments in python?  Mention 10 study cases

"""

Comments woh text hota hai jo code likhte waqt hum apne ya dusre programmers ki samajh ke liye likhte hain. 
Python ka interpreter (code chalane wala engine) inhein ignore kar deta hai, 
yaani ye code ki output par koi asar nahi daalte.

10 Study Cases (Kyun zaroori hain?):
1.Code ki wazahat (Explanation): 
Jab logic mushkil ho, to batane ke liye ke ye function kya kar raha hai.

# Yeh variable price ko store karta hai
price = 100

2.Debugging: 
Agar koi code kaam nahi kar raha, to us line ko comment bana kar check karna ke kya problem wahan se aa rahi hai.

# print("This line is causing error") 
print("The code works now!")

3.Documentation: 
Functions ke upar unke input aur output ka tareeqa likhna.

def add(a, b):
    # Yeh function do numbers ko add karne ke liye hai
    return a + b

4.Teamwork: 
Jab tumhari team mein koi aur tumhara likha hua code dekhe, to usse jaldi samajh aa jaye.

# Ali: Is part ko mat cheerna, yeh database se connected hai
db_connection = "connected"

5.Future Reference: 
6 mahine baad jab tum wapas apna hi code dekho, to bhool na jao ke ye "formula" kyun lagaya tha.

# Pichli dafa maine yahan tax 15% calculate kiya tha
tax = price * 0.15

6.Code Testing: 
Nayi functionality check karte waqt purane code ko temporary hide (comment) karna.

# old_formula = price * 0.10
new_formula = price * 0.12 # Naya updated formula

7.TODO Lists: 
Code mein aage ke liye kaam note karna (jaise: # TODO: Yahan database connection banana hai).

# TODO: Yahan par user ka email validate karna baqi hai.

8.Highlighting Important Blocks: 
Bade programs mein sections ko alag-alag dikhane ke liye (jaise: # --- User Profile Section ---).

# --- User Profile Section ---
user_name = "Ammar"
age = 25

9.Warning signs: 
Agar koi specific line khatarnak ho (jaise database delete karna), to wahan warning likhna.

# WARNING: Is line ko delete mat karna, data lose ho sakta hai
delete_all_records = False

10.Version Control: 
Purane code ko delete karne ke bajaye comment karke rakhna taake zaroorat padne par wapas la sako.

# Version 1.0: Simple print
# print("Hello World")

# Version 2.0: Input function added
name = input("What is your name? ")
print("Hello " + name)

"""






















































