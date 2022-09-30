class LinearSearch:
    """Search for a character in a string"""

    def linear_search_2D_arr(self, arr_2D, target):
        # Base case: If string is empty, return None
        if len(arr_2D) == 0:
            return None

        for indx_row, row in enumerate(arr_2D):
            for indx_col, ele in enumerate(row):
                if ele == target:
                    return [indx_row, indx_col]

        return None

    def max_ele(self, arr_2D):
        # Base case: If string is empty, return None
        if len(arr_2D) == 0:
            return None

        max_element = arr_2D[0][0]
        for row in arr_2D:
            for ele in row:
                if ele > max_element:
                    max_element = ele

        return max_element


if __name__ == "__main__":
    # Driver code.
    ls = LinearSearch()
    target = 22
    arr = [[8, 2, 5, 3], [1, 2, 4, 6], [9, 3, 2, 4], [9, 4, 22, 89]]
    res = ls.max_ele(arr)
    if res:
        print("Max Element Found: ", res)
    else:
        print("Max Element not found in 2D array or Array is empty.")
