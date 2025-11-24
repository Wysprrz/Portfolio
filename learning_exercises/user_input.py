#input() = A function that prompts the user to enter data  
#          Returns the entered data as a string


name = input("What is your name: ") #prompts the user for their name)
age = input("How old are you?: ")
# age = int(input("How old are you?: ")) # This solves the typecasting age as an int, negates the need, automatically makes it an int. 

age = int(age) #typecasting age as an int, because inputs are stoed as strings, so you cannot concatinate age +1, will throw an error. 
age = age + 1 

print(f"Hello {name}!")
print("Happy birthday!") # doesn't need to be an f string, only use f if you need variables
print(f"You are {age} years old")
