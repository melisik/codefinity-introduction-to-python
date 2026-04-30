# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count = 0
for item in shelf:
    if item == "apples":
        apple_count += 1
print("Number of Apples: " + str(apple_count))
banana_index = shelf.index("bananas")
print("First Banana Index: " + str(banana_index))
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
grapes_count = shelf.count("grapes")
if grapes_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")
if "oranges" in shelf:
    oranges_index = shelf.index("oranges")
    print("Oranges are at index: " + str(oranges_index))
else:
    print("Oranges are out of stock.")
