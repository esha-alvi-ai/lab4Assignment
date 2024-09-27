# coded by cybil fatima sp23-bai-013  collaborator


def make_purchase(self, quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative. Please put a positive number.")
    if quantity > self.amount:
        raise ValueError("Cannot purchase more items than are in stock.")

    total_price = self.get_price(quantity)
    self.amount -= quantity  

    print(str(quantity) + " " + self.name + "(s) purchased for $" + format(total_price, ".2f") + ".")
    print("Stock left: " + str(self.amount))
    
    return total_price
