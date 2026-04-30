# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for key, value in products.items():
    products[key][0] = float(products[key][0])
    products[key][1] = int(products[key][1])
    total_sales = products[key][0]*products[key][1]
    total_sales_list.append(total_sales)
    print(f"Total sales for {key}: ${total_sales}")
    #print(f"Total sales for {key}: ${total_sales_list[-1]}")
#print(products)
total_sum = sum(total_sales_list)
print(f"Total sum of all sales: ${total_sum}")
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")
