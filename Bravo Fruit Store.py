fruits = ["Peaches", "Bananas", "Grapes", "Oranges", "Apples"]  # Store Inventory
fruit_price = [96, 69.96, 120, 40.10, 154]  # Advertised Price of Items
customer_cart = []  # It's what it says


# function to view cart
def cart_view_1():
    cart_view = input("Alisa: Would you like to view your cart?")
    while cart_view not in ("yes", "no"):
        cart_view = input("Please enter [yes] or [no]:")
    if cart_view == "yes":
        if customer_cart[0] == customer_cart[1]:
            customer_cart.remove(customer_cart[1])
            customer_cart[0] = customer_cart[0] + ": 2 kilos"
            print(customer_cart)
        else:
            print(customer_cart)
    elif cart_view == "no":
        input("Lizzie and Betty: We are now proceeding to checkout! UwU")


input("\"Hi! My name is Cindy and I will guide you in testing this program.\"")
Customer_name = input("Cindy: \"Can I have your name?\":")
while Customer_name == "":
    print("Brandon: \"I know you're a little shy, but we just gotta know.")
    Customer_name = input("Tell me your name\":")
input("Cindy: \"" + Customer_name + "...\"")
input("Cindy: \"What a nice name!\"")
Customer_gender = input("Cindy: \"Moving on, are you male or female?\":")
while Customer_gender not in ("male", "female"):
    print("Cindy: \"I didn't quite get that. I can only read [male] or [female]\"")
    print("Brandon: \"C'mon, buddy. This is taking too long already!\"")
    Customer_gender = input("Brandon: \"You a male or a female?\":")
    input("Cindy: \"Hehe- Sorry about that.\"")
    print("\"So... There we go!\"")
if Customer_gender == "male":
    honorific = "Mr. "
elif Customer_gender == "female":
    honorific = "Ms. "
input("Cindy: \"I think you're all set, " + honorific + Customer_name + "! I hope you have fun in this little program "
                                                                        "by my friends!\"")
# Store Introduction
input("Betty: \"Welcome to Bravo Fruit Store! We had all kinds of fruits in the world that you could ask for!\"")
input("Betty: \"Well... \"had\".. hehe.\"")
input("Betty: \"Due to our limited supply, we can now only take TWO orders from each customer.\"")
input("Betty: \"We are very sorry for the inconvenience. Despite that, however, "
      "we promise that the quality of the few fruits we have available will surely surpass your expectations!\"")
input("Betty: \"Happy shopping, " + honorific + Customer_name + "!\"")

# Store Menu
input("Lizzie: \"Oh, hi there! We have the following fruits in our menu for today!:\"")
input("Peaches.....          96")
input("Bananas.....          69.96")
input("Grapes......          120")
input("Oranges.....          40.10")
input("Apples......          154")

first_item = input("We accept orders one at a time. For now, please choose your first purchase!:")
# Taking first order
while first_item not in fruits:
    print("Lizzie: The item, [" + first_item + "], is not in our current menu. ")
    print("Your entry might not be accurate.")
    first_item = input("Betty: Please choose your first purchase strictly from "
                       "our menu, " + honorific + Customer_name + ".:")
if first_item in fruits:  # Verifying customer order 1
    item1_pos = fruits.index(first_item)
    item1_price = fruit_price[item1_pos]
    customer_cart.append(fruits[item1_pos])  # Adding of first item to cart
    print("Alisa: Added " + fruits[item1_pos] + " to your cart!")
    print((fruits[item1_pos] + " cost " + "₱{:.2f}".format(item1_price) + " per kilo."))  # Price Accounting 1
    cust_action = input("Do you want to add more items to your cart?:")
    while cust_action not in ("yes", "no"):
        print("Please answer [yes] or [no]:")
        cust_action = input("Do you want to add more items to your cart?:")
    if cust_action == "yes":  # Customer proceeds to take 2 orders
        second_item = input("Lizzie: Please choose your second purchase:")
        # Taking second order
        while second_item not in fruits:
            print("Lizzie: The item, [" + second_item + "], is not in our current menu.")
            print("Your entry might not be accurate.")
            second_item = input("Betty: Please choose your second purchase strictly from "
                                "our menu, " + honorific + Customer_name + ".:")
        if second_item in fruits:  # Verifying customer order 2
            item2_pos = fruits.index(second_item)
            item2_price = fruit_price[item2_pos]
            customer_cart.append(fruits[item2_pos])  # Adding of second item to cart
            print("Alisa: Added " + fruits[item2_pos] + " to your cart")
            if first_item != second_item:  # Price Accounting 2; skipped on customer's purchase of 2 of the same item
                print((fruits[item2_pos] + " cost " + "₱{:.2f}".format(item2_price) + " per kilo."))
            else:
                pass
            cart_view_1()  # Function call to view cart
            checkout_total2 = item1_price + item2_price  # Checkout for 2 items
            print("Betty: Your checkout total is " + "₱{:.2f}".format(checkout_total2))
            print("Thank you very much for shopping at Bravo Fruit Store!")
    elif cust_action == "no":  # Customer proceeds to take only 1 order
        cart_view_1()
        checkout_total = item1_price  # Checkout for 1 item
        print("Betty: Your checkout total is " + "₱{:.2f}".format(checkout_total))
        print("Thank you for shopping at Bravo Fruit Store!")
else:
    print(first_item)  # Loop to ask customer to answer properly
