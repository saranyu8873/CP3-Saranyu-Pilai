username = input("Username :")
password = int(input("Password :"))

if username=="saranyu" and password==7748:
    print("Welcome to Borntodev Shop")
    print("A = 1,500 THB")
    print("B = 2,500 THB")

    product_a = 1500
    product_b = 2500
    product = input("Please choose product :")

    if product == "a" :
        qty_a = int(input("How much quantity do you need?"))
        print(product_a*qty_a,"THB")

    elif product == "b" :
        qty_b = int(input("How much quantity do you need?"))
        print(product_a * qty_b, "THB")

    else :
        print("Thank you for come in")
        print("See you next time")

