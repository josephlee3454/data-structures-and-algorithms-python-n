import pytest
from data_structures_and_algorithms_python_n import __version__
from data_structures_and_algorithms_python_n.code_challenges.kata import Checkout 
@pytest.fixture()
def checkout():
  checkout = Checkout()
  return checkout

def test_version():
  assert __version__ == '0.1.0'

# def test_can_init_checkout():
#   co = Checkout() ##tests the initilization of checkout class


# def test_can_add_item_price(checkout):
#   checkout.additemprice("a", 1)

# def test_canadditem(checkout):
#   checkout.add_item("a")

def test_Can_Cal_Total(checkout):
  checkout.additemprice("a",1)
  checkout.add_item("a")
  assert checkout.cal_total() == 1

def test_add_multiple_items(checkout):
  checkout.additemprice("a", 1)
  checkout.additemprice("b",2)
  checkout.add_item("a")
  checkout.add_item("b")
  assert checkout.cal_total() == 3


def test_addDiscountRule(checkout):
  checkout.add_discount("a", 3, 2)


# def test_canAPPlyDiscounts(checkout):
# checkout.add_discount ("a", 3, 2)
# checkout.add_item("a")
# checkout.add_item("a")
# checkout.add_item("a")
# asssert checkout.cal_total() == 2