from ..src.ordered_array_linear import linear_search

def test_linear_search():
    assert linear_search([3,14,35,50,75,101,202], 22) == -1
    assert linear_search([3,14,35,50,75,101,202], 75) == 75
    assert linear_search([1,2,3,4,5], 1) == 1
    assert linear_search([1,2,3,4,5], 5) == 5
    assert linear_search([], 10) == -1
    assert linear_search([10], 10) == 10
    assert linear_search([10], 5) == -1
    print("All tests passed.")

test_linear_search()