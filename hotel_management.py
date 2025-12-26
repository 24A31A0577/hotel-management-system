## def login():
    user = input("Enter username: ")
    password = input("Enter password: ")
    if user == "hotel" and password == "hotellogin":
        print("Successfully logged in")
        return True
    else:
        return False
def room_status():
    available_rooms=0
    occupied_rooms=0
    print("\nRoom No | Floor | Type    | Cost | Status")
    print("-" * 45)
    for room in rooms:
        floor = room["room no"] // 100
        status = "Available" if room["available"] else "Occupied"
        if room["available"]:
            available_rooms += 1
        else:
            occupied_rooms += 1
        print(f"{room['room no']:<7} | {floor:<5} | {room['type']:<7} | {room['cost']:<4} | {status}")
    print("-" * 50)
    print("Total Rooms     :", len(rooms))
    print("Available Rooms :", available_rooms)
    print("Occupied Rooms  :", occupied_rooms)
def check_in():
    room_no = int(input("Enter room number: "))
    for room in rooms:
        if room["room no"] == room_no:
            if not room["available"]:
                print("Room already occupied")
                return
            name = input("Customer name: ")
            phone = input("Phone number (10 digits): ")
            if not phone.isdigit() or len(phone) != 10:
                print("Invalid phone number! Must contain exactly 10 digits.")
                return
            aadhar = input("Aadhar number (12 digits): ")
            if not aadhar.isdigit() or len(aadhar) != 12:
                print("Invalid Aadhar number! Must contain exactly 12 digits.")
                return
            address = input("Address: ")
            days = int(input("Number of days: "))
            # Bill calculation
            total_amount = days * room["cost"]
            advance_amount = total_amount * 0.30
            print("\n--- PAYMENT DETAILS ---")
            print("Total Amount :", total_amount)
            print("Advance (30%):", advance_amount)
            customers.append({
                "name": name,
                "phone": phone,
                "aadhar": aadhar,
                "address": address,
                "room no": room_no,
                "days": days,
                "total_amount": total_amount,
                "advance_paid": advance_amount,
                "food_bill": 0
            })
            room["available"] = False
            print("Check-in successful with advance payment")
            return
    print("Room number does not exist in hotel")
def check_out():
    room_no = int(input("Enter room number: "))
    for customer in customers:
        if customer["room no"] == room_no:
            room_bill = customer["total_amount"]
            food_bill = customer["food_bill"]
            advance = customer["advance_paid"]
            final_total = room_bill + food_bill
            remaining = final_total - advance
            print("\n--- FINAL BILL ---")
            print("Room Charges   :", room_bill)
            print("Food Charges   :", food_bill)
            print("Total Bill     :", final_total)
            print("Advance Paid   :", advance)
            print("Amount to Pay  :", remaining)
            for room in rooms:
                if room["room no"] == room_no:
                    room["available"] = True
                    customers.remove(customer)
                    print("Check-out successful")
                    return
    print("details not matched check it once!")
def show_food_menu():
    print("\n------ FOOD MENU ------")
    for category, items in food_menu.items():
        print(f"\n{category}:")
        for code, (name, price) in items.items():
            print(f"{code}. {name} - ₹{price}")
def order_food():
    room_no = int(input("Enter room number: "))

    # Find customer
    for customer in customers:
        if customer["room no"] == room_no:
            print(f"\nCustomer: {customer['name']}")
            
            while True:
                # Select meal type
                print("\nSelect meal type to order:")
                print("1. Breakfast")
                print("2. Lunch")
                print("3. Dinner")
                print("0. Finish ordering")
                
                try:
                    meal_choice = int(input("Enter choice: "))
                except ValueError:
                    print("Invalid input! Enter a number.")
                    continue

                if meal_choice == 0:
                    print("Finished ordering food.")
                    break

                if meal_choice == 1:
                    meal_type = "Breakfast"
                elif meal_choice == 2:
                    meal_type = "Lunch"
                elif meal_choice == 3:
                    meal_type = "Dinner"
                else:
                    print("Invalid choice. Try again.")
                    continue

                # Show menu for selected meal type
                print(f"\n--- {meal_type} MENU ---")
                for code, (name, price) in food_menu[meal_type].items():
                    print(f"{code}. {name} - ₹{price}")

                while True:
                    try:
                        choice = int(input("\nEnter item number to order (0 to go back to meal selection): "))
                    except ValueError:
                        print("Invalid input! Enter a number.")
                        continue

                    if choice == 0:
                        break  # Back to meal selection

                    if choice in food_menu[meal_type]:
                        item_name, price = food_menu[meal_type][choice]
                        try:
                            quantity = int(input(f"Enter quantity for {item_name}: "))
                        except ValueError:
                            print("Invalid input! Quantity must be a number.")
                            continue

                        cost = price * quantity
                        customer["food_bill"] += cost
                        print(f"{item_name} x {quantity} added. Cost: ₹{cost}")
                    else:
                        print("Invalid item number. Try again.")

            print(f"\nTotal food bill for {customer['name']}: ₹{customer['food_bill']}")
            return

    print("Room not found or customer not checked in.")

def main_menu():
    while True:
        print("\n1.View Rooms")
        print("2.Check-in")
        print("3.Order Food")
        print("4.Check-out")
        print("5.Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            room_status()
        elif choice == "2":
            check_in()
        elif choice == "4":
            check_out()
        elif choice == "3":
            order_food()
        elif choice == "5":
            print("Exited")
            break
        else:
            print("Invalid choice")
food_menu = {
    "Breakfast": {
        1: ("Tea", 30),
        2: ("Coffee", 30),
        3: ("Idli", 40),
        4: ("Vada", 50),
        5: ("Puri", 60),
        6: ("Dosa", 60)
    },

    "Lunch": {
        7: ("Veg Full Platter", 150),
        8: ("Veg Curries + Rice", 120),
        9: ("Paneer Curry", 150),          
        10: ("Non-Veg Full Platter", 200),
        11: ("Chicken Curry", 180),        
        12: ("Biryani", 220),
        13: ("Chapati", 40),
        14: ("Parotta", 50),
        15: ("Butter Naan", 50)
    },

    "Dinner": {
        16: ("Chapati", 40),
        17: ("Parotta", 50),
        18: ("Paneer Curry", 150),
        19: ("Chicken Curry", 180),
        20: ("Veg Full Platter", 150),
        21: ("Non-Veg Full Platter", 200),
        22: ("Idli", 40),
        23: ("Dosa", 60),
        24: ("Butter Naan", 50)
    }
}

rooms = []
for floor in range(1, 6):
    rooms.append({"room no": floor*100 + 1, "type": "AC", "cost":2000, "available":True})
    rooms.append({"room no": floor*100 + 2, "type": "AC", "cost":2000, "available":True})
    rooms.append({"room no": floor*100 + 3, "type": "Non-AC", "cost":1500, "available":True})
    rooms.append({"room no": floor*100 + 4, "type": "Non-AC", "cost":1500, "available":True})
customers = []
if login():
    main_menu()
else:
    print("Invalid login")