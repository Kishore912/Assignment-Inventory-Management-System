def Add_Product():
    product_id = int(input("Enter Product ID: "))
    product_name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = int(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    print("Product added successfully .")
    return product_id, product_name, category, price, quantity 


def print_inventory(inventory_dict):
    print("Inventory:")
    print("{:<12} {:<20} {:<12} {:<8} {:<8}".format("Product ID", "Product Name", "Category", "Price", "Quantity"))
    for i in range(len(inventory_dict["product_id_list_dict"])):
        print("{:<12} {:<20} {:<12} {:<8.2f} {:<8}".format(inventory_dict["product_id_list_dict"][i], inventory_dict["product_name_list_dict"][i], inventory_dict["category_list_dict"][i], inventory_dict["price_list_dict"][i], inventory_dict["quantity_list_dict"][i]))  


inventory_dict={
    'product_id_list_dict' : [],
    'product_name_list_dict' : [],
    'category_list_dict' : [],
    'price_list_dict' : [],
    'quantity_list_dict' : []
}

while True:
    print(" Menu:\n1. Add Product\n2. Update Product Information\n3. Display Inventory\n4. Exit ")
    Choice = int(input("Enter your choice: "))
    if Choice==1:
        product_id, product_name, category, price, quantity = Add_Product()
        inventory_dict["product_id_list_dict"].append(product_id)
        inventory_dict["product_name_list_dict"].append(product_name)
        inventory_dict["category_list_dict"].append(category)
        inventory_dict["price_list_dict"].append(price)
        inventory_dict["quantity_list_dict"].append(quantity)

    elif Choice == 3:
        print_inventory(inventory_dict) 

    elif Choice==4:
        print("Inventory saved successfully. Exiting.")
        break    
    else:
        print("hi")






# Menu:
# 1. Add Product
# 2. Update Product Information
# 3. Display Inventory
# 4. Exit   







