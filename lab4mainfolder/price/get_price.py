#esha alvi sp23-bai-015  maintainer



def get_price(self, quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative. Please use positive values only.")

    if quantity < 10:
        discount = 0
    elif quantity < 100:
        discount = 0.1
    else:
        discount = 0.2

    total_price = self.price * quantity
    discount_amount = total_price * discount
    total_price -= discount_amount

    return total_price

