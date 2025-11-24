# Exercise 2 Shopping Cart Program

#variables
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: ")) #typecasted as a float because need decimals might be change
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"YOu have bought {quantity} x {item}/s") # /s is like a newline?
print(f"Your total is: ${total}")
