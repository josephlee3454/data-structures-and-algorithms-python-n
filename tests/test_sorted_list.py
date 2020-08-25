# from data_structures_and_algorithms_python_n import __version__
from data_structures_and_algorithms_python_n.code_challenges.sorted_list import insertion_sort

# def test_version():
#     assert __version__ == '0.1.0'

def test_list_one():
  actual = insertion_sort([8,4,23,42,16,15])
  expected = [8,4,23,42,16,15]
  assert actual == expected