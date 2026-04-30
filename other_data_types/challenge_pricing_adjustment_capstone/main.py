grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
eggs_price = grocery_inventory["Eggs"][1]
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    category, price, quantity = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (category, price - 1, quantity)
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes: ", grocery_inventory)

if grocery_inventory["Milk"][2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    category, price, quantity = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (category, price, quantity + 20)
else:
    print("Milk has sufficient stock.")

if grocery_inventory["Apples"][1] > 2:
    del grocery_inventory["Apples"]
    print("Apples removed from inventory due to high price.")

print("Updated inventory: ", grocery_inventory)