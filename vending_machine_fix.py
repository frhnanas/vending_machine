drink_choices = [
    {'name':'Coca-cola','price': 10000},
    {'name':'Teh Pucuk','price': 5000},
    {'name':'Le Minerale','price': 3000},
    {'name':'Nescafe','price': 12000},
    {'name':'Yogurt','price': 29000}
]

notes_list = [[50000, 1], [20000, 2], [10000, 2], [5000, 3], [2000, 1], [1000, 1]]

# print(drink_choices[0]['name'])

def show_menu():
    menu_count = 1
    print("Drink: Price")
    for item in drink_choices:
        print(f"{menu_count}. {item['name']}: {item['price']}")
        menu_count += 1

def make_order():
    price = 0
    is_buy = True
    order_list = {}
    print("================================")
    while (is_buy):
        order_input = input("Type the number of your order (type 'done to finish'): ")
        if (order_input.lower() == 'done'):
            is_buy = False
            print("================================")
            if (not order_list):
                print("No order was added to the cart")
            else:
                print('Final Order:')
                for drink, quantity in order_list.items():
                    print(drink_choices[drink]['name'], ":", quantity)
                    price += drink_choices[drink]['price'] * quantity
                print("Total Price: ", price)
        elif(order_input.isdigit()):
            order_number = int(order_input)-1
            if (0 <= order_number < len(drink_choices)):
                print(drink_choices[order_number]['name'], "has been added to the cart successfully")
                if (order_number not in order_list):
                    order_list[order_number] = 1
                else:
                    order_list[order_number] += 1
            else:
                print("Invalid order, please try again")
        else:
            print("Invalid order, please try again")
    return price

def process_payment(price):
    change_list = {}
    print("================================")
    if (price == 0):
        print("No payment to be made")
        return change_list
    notes_input = input("Type the amount of your notes: ")
    if (not notes_input.isdigit()):
        return change_list
    notes_number = int(notes_input)
    change = notes_number - price
    if (notes_number < price):
        print("================================")
        print("Not enough notes to process payment")
        return change_list
#     old code starts from here

#     for notes in notes_list:
#         notes_quantity = change // notes
#         change = change % notes
#         change_list[notes] = notes_quantity

#     until here
    for notes in notes_list:
        if (change <= 0):
            break
        if (notes[0] <= change):
            notes_quantity = change // notes[0]
            if (notes_quantity <= notes[1]):
                change_list[notes[0]] = notes_quantity
                change = change - (notes[0] * notes_quantity)
            else:
                change_list[notes[0]] = notes[1]
                change = change - (notes[0] * notes[1])
    if (change > 0):
        print("================================")
        print("Insufficient notes to process payment")
        return {}
    return change_list

def show_change(change):
    print("================================")
    if (not change):
        print("No change to be shown")
    else:
        print("Note: Quantity")
        for notes, quantity in change.items():
            print("- ", notes, ":", quantity)

show_menu()
total_price = make_order()
total_change = process_payment(total_price)
show_change(total_change)