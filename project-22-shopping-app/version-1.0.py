print("Welcome! to Shopping Store")

actions = [1,2,3,0]
products = { "shirt":500, "pants":700, "shoes":400, "watch":200, "glasses":150, "suit":1200, "coat":570}
cart = {}

print("\nShopping Products:")
print(f"{'Product Name':<20}{'Price':<10}")
print("-" * 30)
for key, value in products.items():
    print(f"{key.capitalize():<20}{value:<10}")
print("-" * 30)

while True:
    print("\nSelect Action:")
    print("1. Add Items, 2. View Cart, 3. Checkout, 0. Exit")
    print("-" * 30)

    try:
        user_action = int(input("Enter your action: "))

        if user_action not in actions:
            print("Invalid Action! Please Enter between 1-3 or 0 for exit\n")
            continue

        if user_action == 0:
            print("Goodbye! Thanks For Shopping")
            break

        if user_action == 1:
            while True:
                item_name = input("Enter Item Name: ").lower().strip()

                if item_name in products:
                    try:
                        quantity = int(input("Add Quantity: "))

                        if 0 < quantity:
                            cart.update({item_name:quantity})
                            print(f"{item_name.capitalize()} is added to Cart")
                            break
                        else:
                            print("Item Quantity must in positive value")          
                            continue
                    except ValueError:
                        print("Invalid Input! Please Enter Valid Number")    
                        continue
                else:
                    print("Item not in Stock")
                    continue
         
        if user_action == 2 or user_action == 3:
            if not cart:
                print("Your Cart is Empty")
                continue
            else:
                print("\n")
                print("-" * 60)
                print("Cart Items")
                print(f"{'Product Name':<20}{'Quantity':<10}{'Unit Price':<15}{'Total Price':<10}")
                print("-" * 60)
                for key, value in cart.items():
                    item_total = products[key] * value
                    print(f"{key.capitalize():<20}{value:<10}{products[key]:<15}{item_total:<10}")
                print("-" * 60)
                total_cost = sum(products[key] * value for key, value in cart.items())
                print(f"{"":<20}{"":<10}{'Total Price':<15}{total_cost:<10}")
                print("-" * 60)
                print("\n")
                while True:
                    checkout = input("Checkout Cart: (y/n): ").lower().strip()
                    if checkout in ["y","n"]:
                        break
                    else:
                        print("Invalid Choice! type 'y' for yes or 'n' for no")
                        continue
                if checkout == "y":
                    print("Checkout Successfully")
                    print("Goodbye! Thanks For Shopping")
                    break

    except ValueError:
        print("Invalid Input! Please Enter between 1-3 or 0 for exit\n")
        continue