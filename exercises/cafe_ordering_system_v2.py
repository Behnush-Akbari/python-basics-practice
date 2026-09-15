the_menu = {
             "drinks": {
                "1": {"name": "Juice", "price": 2.0},
                "2": {"name": "wine", "price": 5.0},
                "3": {"name": "Coffee", "price": 2.5}
            },
             
            "food": { 
                "1": {"name":"pizza", "price":10.0},
                "2": {"name":"hamburger", "price":10.98},
                "3": {"name":"pasta", "price": 9.73},
                "4": {"name":"stake", "price":11.53},
                "5": {"name":"chicken", "price":10.5},
                "6": {"name":"salad", "price":0.23}
            }, 
            
           "deserts":{
                "1":{"name":"cheesecake", "price":3.0},
                "2":{"name": "ice cream", "price":2.23},
                "3":{"name" : "brownie", "price":3.2},
                "4":{"name":"cake", "price":2.5}
            }
           }

order = [] 

print("~." * 50)
print("~~~~☕ WELCOME TO MY PYTHON CAFE! ☕~~~~")
print("~." * 50)


while True:
    print("\n=== MAIN MENU ===")
    for category in the_menu.keys():
        print(f"👉 {category.title()}")
    print("👉 Pay (Go to Checkout)")

    selected_category = input("\nChoose a category or type 'pay': ").strip().lower()

    if selected_category == "pay":
        break

 if selected_category in the_menu:
        current_category_items = the_menu[selected_category]
        
        while True:
            print(f"\n--- 🍽️ {selected_category.upper()} MENU ---")
            for item_id, item_info in current_category_items.items():
                print(f"[{item_id}] {item_info['name']} - ${item_info['price']}")

            print("\n💡 Tip: Type 'menu' to go back to Main Menu")
            item_choice = input(f"Select your {selected_category} number: ").strip().lower()

           
            if item_choice == "menu":
                print("\n🔙 Returning to Main Menu...")
                break

            if item_choice in current_category_items:
                chosen_item = current_category_items[item_choice]

                while True:
                    quantity_input = input(f"How many '{chosen_item['name']}' would you like? ").strip()
                    if quantity_input.isdigit() and int(quantity_input) > 0:
                        quantity = int(quantity_input)
                        break
                    else:
                        print("⚠️ Please enter a valid positive number!")
                        
                item_total = chosen_item["price"] * quantity
                order.append({
                    "category": selected_category,
                    "name": chosen_item["name"],
                    "price": chosen_item["price"],
                    "quantity": quantity,
                    "total": item_total
                })

                print(f"✅ Added {quantity}x {chosen_item['name']} to your cart successfully!")
            else:
                print("!! Invalid item number! Please select from the list above.")

            else:
            print("!!Invalid category! Please choose from the available categories or type 'pay'.")

print("\n" + "‍‍~." * 50)
print("🧾 FINAL BILL & PAYMENT GATEWAY")
print("~." * 50)

if not order:
    print("Your cart is empty! No order placed. Have a great day! 👋")
else:
    subtotal = 0.0
    print(f"{'Item':<18} | {'Qty':<5} | {'Price':<8} | {'Total':<8}")
    print("-" * 50)

    for item in order:
        print(f"{item['name']:<18} | {item['quantity']:<5} | ${item['price']:<7.2f} | ${item['total']:<7.2f}")
        subtotal += item["total"]

    tax = subtotal * 0.09 
    grand_total = subtotal + tax

    print("-" * 50)
    print(f"Subtotal:       ${subtotal:.2f}")
    print(f"Tax (9%):       ${tax:.2f}")
    print(f"Grand Total:    ${grand_total:.2f}")
    print("=" * 50)
    print("💳 Connecting to Payment Gateway... Payment Successful! 🎉")
    print("Thank you for your order, Behnush! Enjoy your meal! 🍕☕🍰")



