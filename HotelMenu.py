menu = {
    'Pasta':50,
    'Pizza':40,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}

print("Welcome to our resturant BilRions")
print("Pasta: Rs 50\nPizza: Rs 40\nBurger:Rs 60\nSalad:Rs 70\nCoffee:Rs 80")

order_total = 0
item_1 = input("Enter the Name of Item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Your ordered item is {item_1}, is not availoable yet.Thank you for visiting our resturant")

another_order =  input("Do you want to add another item in your order? (YES / NO) ")
if another_order == "Yes":
    item_2 = input("Enter the Name of your second item = ")
    if item_2 in menu:
       order_total += menu[item_2]
       print(f"four Item{item_2} has been added to your order")
    else:
       print("Your ordered item is {item_2}, is not availoable yet.Thank you for visiting our resturant")
print(f"Total amount of  your ordered items is {order_total}")


