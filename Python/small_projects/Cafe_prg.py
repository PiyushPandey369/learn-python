import time
menu_items = {
    "coffee": 50,
    "tea": 30,
    "shake": 60,
    "ganne ka juice":20,
    "aloo ke paratha":30,
    "pakode":50,
    "bhajiya":30
}

order_price = 0
quantity=1
order=[]

print("----Welcome To Palpasa Cafe----")
time.sleep(2)
def menu_print():
    print("----Menu-----")
    for item, price in menu_items.items():
        print(f"{item.capitalize()}: Rs {price}")
        time.sleep(0.2)

def take_orders():
    global order_price
    global order
    global quantity
    while True:
        item = input("Enter your order (or type 'done' to finish): ").lower()
        
        if item == 'done':
            break
        elif item in menu_items:
            quantity=int(input("Enter the quantity (How many Items):"))
            order_price += (quantity*menu_items[item])
            print(f"{item.capitalize()} costs you Rs: {(quantity*menu_items[item])}")
            order.append((item, quantity, menu_items[item] * quantity))
        else:
            print("Oops!! This item is not available...")
            menu_print()
        


def discount(order_price):
    if(499<order_price<=2000):
       time.sleep(2)
       print("Congralaution......")
       time.sleep(1)
       print("You got 20% off over bill")
       time.sleep(1)
       print(f"Inital cost: Rs {order_price}")
       discount=order_price*0.2
       print(f"Discount: Rs {discount}")
       time.sleep(1)
       print("Final cost: Rs",order_price-discount)
    elif(order_price>2000):
        time.sleep(2)
        print("Congralaution......")
        time.sleep(1)
        print("You got 40% off over bill")
        time.sleep(1)
        print(f"Inital cost: Rs {order_price}")
        discount=order_price*0.4
        print(f"Discount: Rs {discount}")
        time.sleep(1)
        print("Final cost: Rs",order_price-discount)
    else:
       time.sleep(2)
       print(f"Inital cost: Rs {order_price}")
       time.sleep(1)
       print("No discount alloted.")
       print(f"Final cost: Rs {order_price}")

def order_detail():
    print("\n----Order Details----")
    print(f"{'Item':<20}{'Quantity':<10}{'Cost'}")
    print("-" * 40)
    for item, qty, cost in order:
       print(f"{item.title():<20}{qty:<10}{cost}")


menu_print()
take_orders()
order_detail()
discount(order_price)
print("\nThank you for visiting Palpasa Cafe! ☕")
