discount = 0.1
vip_discount = 0.1
order_price = 100


def create_order(price):
    final_price = price - (price * discount)
    print(f"Price after the main discount: {final_price:.2f}")

    def apply_additional_discount(additional_discount):
        nonlocal final_price
        final_price -= price * additional_discount
        print(f"Price after additional discount: {final_price:.2f}")

    return final_price, apply_additional_discount


final_price, apply_vip_discount = create_order(order_price)
apply_vip_discount(vip_discount)
