menu = ""
menu_list = []
i = 0
stock = {}
price = {}

num_of_items = int(input("How many items for stocktake? "))

for items in range(0, num_of_items):
    menu = input("Enter stocktake item here: ")
    stock_number = int(input(f"Enter stock amount of {menu} here: "))
    stock_value = float(input(f"Enter the value of {menu} here: "))
    menu_list.append(menu)
    stock[f'{menu}'] = stock_number
    price[f'{menu}'] = stock_value
    i += 1

print(menu_list)
print(stock)
print(price)

total_value = 0
with open("stocktake.txt", "w") as f:
    for item in menu_list:
        item_value = stock[item]*price[item]
        total_value += item_value
        f.write(f"{item} has {stock[item]} in stock, at value ${round(price[item],2)}, with total value of ${round(item_value,2)} \n"
              f"        Running stocktake value: ${total_value} \n")
    print(f"The total value of the stocktake is ${round(total_value,2)}")
