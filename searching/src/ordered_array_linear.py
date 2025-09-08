def linear_search(arr, value):
    """
    Perform a linear search on an ordered array.

    Parameters:
    arr (list): An ordered list of elements.
    value: The value to search for in the list.

    Returns:
    int: The index of the value if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == value:
            return arr[i]
        
    return -1


if __name__ == "__main__":
    returned_value = linear_search([3,14,35,50,75,101,202], 22)
    if returned_value == -1:
        print(f"Unable to find the provided value")
    else:
        print(returned_value)