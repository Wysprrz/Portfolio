# Typecasting = the process of converting a variable from one data type to another

name = "Pedro Rivera"
age = 21
gpa = 3.4
is_student = True



# typecating gpa to integer

gpa = int(gpa)

print(gpa) #will print 3 


#typcasting name to boolean

name = bool(name)
print(name) #will print True because name is not empty. 

#Typecasting age to string
age = str(age)
print(age) #Will print "21" as a string

age += "1" # will concatenate "1" to age since age is now a string. 
print(age) # will print "211"