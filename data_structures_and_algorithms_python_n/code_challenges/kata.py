class Checkout:
  class Discount:
    def __init__(self, num_items, price):
      self.num_items = num_items
      self.price = price

  def __init__(self):
    self.prices = {}
    self.discounts = {}
    self.items = {}

  

  def additemprice(self, item, price):
    self.prices[item] = price
  def add_discount(self, item, num_items, price):
    discount = discount(num_items, price)
    self.discount[item] = discount

  def add_item(self, item):
    if item in self.items:
      self.items[item] += 1
    else: 
      self.items[item] = 1
  def cal_total(self):
    total = 0
    for item, cnt in self.items.items():
      total += self.prices[item] * cnt
    return total


