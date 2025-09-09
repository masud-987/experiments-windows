def binary_search(arr, value_to_search):
    """
    Performs binary search on an Ordered Array.

    Parameters:
    arr(list): A list of ordered array.
    value: A vlaue to search for in the array.

    """
    lower_bound = 0
    upper_bound = len(arr) - 1
    
    while lower_bound <= upper_bound:
        middle_point = (upper_bound + lower_bound) // 2

        if arr[middle_point] == value_to_search:
            return arr[middle_point]
        elif arr[middle_point] > value_to_search:
            upper_bound = middle_point - 1
        elif arr[middle_point] < value_to_search:
            lower_bound = middle_point + 1

    return -1



if __name__ == "__main__":
    returned_value = binary_search([3,14,35,50,75,101,202], 22)
    if returned_value == -1:
        print(f"Unable to find the provided value")
    else:
        print(returned_value)