from src.ordered_array_binary import binary_search

def test_binary_search():
    assert binary_search([3,14,35,50,75,101,202], 22) == -1
    assert binary_search([3,14,35,50,75,101,202], 75) == 75
    assert binary_search([], 5) == -1
    assert binary_search([1,2,3,4,5], 1) == 1
    assert binary_search([1,2,3,4,5], 5) == 5
    assert binary_search([10], 10) == 10
    assert binary_search([10], 5) == -1