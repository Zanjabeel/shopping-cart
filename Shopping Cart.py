
item = input("Enter the item name ")
price = float(input("Enter the price "))
amount_m = float(input("How much money do you have? $ "))

num_items = amount_m / price #the number of items you can buy

print("The total number of items you can buy is", num_items)

quantity = int(input("How many items do you wanna buy? "))

total_price = price * quantity
remainder = amount_m % price
# Same result if you use either
# remainder = amount_m % price
# OR remainder = amount_m - total_price

print("The total price is", total_price)
print(f"the amount of money you have left is $ {remainder}")
print(f"You've bought {quantity} {item}/s")

print("------------------------------")

# The input function can be empty
# but the user won't know what they should input, and that's why you need an input prompt: input("")

item = input()
price = float(input())
amount_m = float(input())

num_items = amount_m / price #the number of items you can buy

print("The total number of items you can buy is", num_items)

