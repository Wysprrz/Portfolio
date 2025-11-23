# variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains.

# Strings - series of text

first_name = "Pee"
food = "tuna"
email = "wysprrz@gmail.com"
print(f"Hello {first_name}")
print(F"You like {food}")
print(f"Your email is {email}")

#Integers - Whole numbers (no decimals)
age = 21
quantity = 3
num_of_students = 30

print(f"You are {age} years old.")
print(f"You are buying{quantity} items")
print(f"Your class has {num_of_students} students")

# Float - Numbers that can have decimals

price = 10.99
gpa = 3.2
distance = 5.5

print(F"THe price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"you ran {distance}km")

# Boolean - Only true or false. 

is_student = False
for_sale = True
is_online = True


print(f"Are you a student?: {is_student}")

if is_online:
    print("You are online")
else:
    print("You are offline")

if is_student:
    print("You are a student")
else: 
    print("you are NOT a student")

if for_sale:
    print("that item is for sale")
else:
    print("that item is NOT avaliable")

#Challenge section

#My four variables
favorite_food = "tuna"
my_age = 21
my_weight = 343.2
my_boolean = True

#assignment tracking
assignment = "Post four variables, a string, a intiger, a float, a bloolean"
assignment_completed = False 
grade = 0

if assignment_completed == True:
    grade = 100
else: 
    grade = 0 


#output

print(f"Assignment completed: {assignment_completed}")
print(f"Grade: {grade}")