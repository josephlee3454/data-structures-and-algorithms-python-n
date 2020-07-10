from data_structures_and_algorithms_python_n import __version__
from data_structures_and_algorithms_python_n.code_challenges.stack import Node, Stack

def test_version():
  assert __version__ == '0.1.0'



def test_str_val():
  x = Stack('1').__str__()
  y = 'the top is None'
  assert x == y

  def test_push_stuff():
    x = Stack('1').push()
    y = '1'
    assert x == y