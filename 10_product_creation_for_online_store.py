def create_product(name, price, quantity):
    def change_price(new_price):
        nonlocal price
        price = new_price

    def get_info():
        return f"Product: {name}, Price: {price}, Quantity: {quantity}"

    return {
        "change_price": change_price,
        "get_info": get_info
    }


new_product = create_product("Notebook", 1000, 10)
print(new_product['get_info']())
new_product['change_price'](1500)
print(new_product['get_info']())
