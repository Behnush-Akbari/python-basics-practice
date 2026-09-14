print("hello world!, this is our menu.")

product_kind = ["drinks", "foods", "deserts"]
print(product_kind)

drinks = ["apple juice", "orange juice", "tee", "coffee", "water"]
foods = ["pizza", "hamburger", "spagetti", "chicken and rice", "stake", "freis"]
deserts = ["cheesecake", "cake", "icecreme", "marshmalo"]
choose_product_kind = input("choose product kind: ")


price_list = [{"apple juice": 2, "orange juice":2.3, "tee":3, "coffee":2.5, "water":0.5},
              {"pizza":10, "hamburger":10.98, "spagetti":9.73, "chicken and rice":11.53, "stake":23.03, "freis":1.23},
              {"cheesecake":3, "cake":2.23, "ice cream":1.36, "marshmalo":1.37}]
    
if choose_product_kind == product_kind[0]:
    drinks = ["apple juice", "orange juice", "tee", "coffee", "water"]
    print(f"this is our drinks menu:{drinks}")
    choose_drink = input("choose your drink: ")
    chosen_item_price = price_list[0][choose_drink]
    print(f"price: {chosen_item_price}")
    if choose_drink == drinks[0]:
        count_drink = int(input(f"how many {choose_drink} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_drink) * ((chosen_item_price) + ((9*chosen_item_price)/100)), 2)
        print(f"u should pay {total_price} $")
    elif choose_drink == drinks[1] :
        count_drink = int(input(f"how many {choose_drink} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_drink * chosen_item_price) + (count_drink * tax), 2)
        print(f"u should pay {total_price} $")
    elif choose_drink == drinks[2] :
        count_drink = int(input(f"how many {choose_drink} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_drink * chosen_item_price) + (count_drink * tax), 2)
        print(f"u should pay {total_price} $")
    elif choose_drink == drinks[3] :
        count_drink = int(input(f"how many {choose_drink} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_drink * chosen_item_price) + (count_drink * tax), 2)
        print(f"u should pay {total_price} $")
    elif choose_drink == drinks[4] :
        count_drink = int(input(f"how many {choose_drink} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_drink * chosen_item_price) + (count_drink * tax), 2)
        print(f"u should pay {total_price} $")
    else:
        print("plz check your answer and try again")
elif choose_product_kind == product_kind[1]:
    foods = ["pizza", "hamburger", "spagetti", "chicken and rice", "stake", "freis"]
    print(f"this is our foods menu:{foods}")
    choose_food = input("choose your food: ")
    chosen_item_price = price_list[1][choose_food]
    print(f"price: {chosen_item_price}")
    if choose_food == foods[0]:
        count_food = int(input(f"how many {choose_food} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_food * chosen_item_price) + (count_food * tax), 2)
        print(f"u should pay {total_price} $")
    elif choose_food == foods[1] :
        count_food = int(input(f"how many {choose_food} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_food * chosen_item_price) + (count_food * tax), 2)
        print(f"u should pay {total_price} $")
    elif choose_food == foods[2] :
        count_food = int(input(f"how many {choose_food} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_food * chosen_item_price) + (count_food * tax), 2)
        print(f"u should pay {total_price} $")
    elif choose_food == foods[3] :
        count_food = int(input(f"how many {choose_food} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_food * chosen_item_price) + (count_food * tax), 2)
        print(f"u should pay {total_price} $")
    elif choose_food == foods[4] :
        count_food = int(input(f"how many {choose_food} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_food * chosen_item_price) + (count_food * tax), 2)
        print(f"u should pay {total_price} $")
    elif choose_food == foods[5] :
        count_food = int(input(f"how many {choose_food} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_food * chosen_item_price) + (count_food * tax), 2)
        print(f"u should pay {total_price} $")
    else:
        print("plz check your answer and try again")
elif choose_product_kind == product_kind[2]:
    deserts = ["cheesecake", "cake", "icecreme", "marshmalo"]
    print(f"this is our deserts menu: {deserts}")
    choose_deserts = input("choose your desert: ")
    chosen_item_price = price_list[2][choose_deserts]
    print(f"price: {chosen_item_price}")
    if choose_deserts == deserts[0]:
        count_deserts = int(input(f"how many {choose_deserts} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_deserts * chosen_item_price) + (count_deserts * tax), 2)
        print(f"u should pay {total_price} $")
    elif choose_deserts == deserts[1] :
        count_deserts = int(input(f"how many {choose_deserts} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_deserts * chosen_item_price) + (count_deserts * tax), 2)
        print(f"u should pay {total_price} $")
    elif choose_deserts == deserts[2] :
        count_deserts = int(input(f"how many {choose_deserts} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_deserts * chosen_item_price) + (count_deserts * tax), 2)
        print(f"u should pay {total_price} $")
    elif choose_deserts == deserts[3] :
        count_deserts = int(input(f"how many {choose_deserts} do u want?: "))
        tax = (9*chosen_item_price)/100
        total_price = round((count_deserts * chosen_item_price) + (count_deserts * tax), 2)
        print(f"u should pay {total_price} $")
    else:
        print("plz check your answer and try again")

else:
    print("enter a valid value")
    
    

  
 



