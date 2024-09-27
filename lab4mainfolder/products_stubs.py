#esha alvi sp23-bai-015  maintainer 
#cybil fatima sp23-bai-013 collaborator
class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price
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

    return total_price# coded by cybil fatima sp23-bai-013  collaborator


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

product = Product("Laptop", 150, 1000)  


try:
    product.make_purchase(5)  
except ValueError as e:
    print(e)

try:
    product.make_purchase(10)  
    print(e)

try:
    product.make_purchase(100) 
except ValueError as e:
    print(e)

try:
    product.make_purchase(200)  
    print(e)

try:
    product.make_purchase(-1)  
except ValueError as e:
    print(e)


print(f"Final stock for {product.name}: {product.amount}")


     