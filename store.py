from catalog import store_items     # import dictionary 

# Global Variable
cart = []

# HELPER Functions
# STORE AND MENU

def header(text):
    print("------------------------------")
    print(text)
    print("------------------------------")

def menu():
    print("Menu")
    print(" 1. - View Catalog")
    print(" 2. - Search Product")
    print(" 3. - View Cart")
    # Add more features
    print(" Q. -Quit")

# CATALOG and CART FUNCTIONS

def print_catalog():
    header(" - Our Catalog -")
    for prod in store_items:
        print(f' | {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')

    answer = input("Type ID to add (N to close): ")
    if answer.lower() == "n":
        return
    else: 
        add_product_to_cart(answer)


def add_product_to_cart(prod_id):
    found = False
    for prod in store_items:
        if str(prod["id"]) == str(prod_id):  # matches user option to dictionary product
            found = True
            cart.append(prod)       # adds product to cart
            print(f'{prod["title"]} added to your cart.')
            break   # stops after finding to products 
        if not found:
            print("*** ERROR: product doesn't exist")

def search_product():
    text = input("Search product by title: ").lower()
    found = False
    for prod in store_items:
        if text in prod["title"].lower():
            found = True
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')
            choice = input("Do you want to add this item to your cart? (y/n): ")
            if choice.lower() == "y":
                add_product_to_cart(prod["id"])
            break # stop after first match and added to the cart
    if not found:
        print("Sorry, this item doesn't exist")

def view_cart():
    header("Your Cart")
    if not cart:
        print("Your cart is empty.")
    else:
        for prod in cart:
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')


# Main Program Loop
option = ""
while option != "q" and option != "Q":
    header("Welcome to Valentina Store")
    menu()

    option = input("Choose a menu option: ")

    if option == "1":
        print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "q" or option == "Q":
        print("Thank you for shopping")
        break
    else:
        print("** ERROR: Invalid Option")
        print("---------------------------")
    
