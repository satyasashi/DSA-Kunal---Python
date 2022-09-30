class LinearSearch:
    """Search for a character in a string"""

    def linear_search_min(self, arr):
        # Base case: If string is empty, return None
        if len(arr) == 0:
            return None

        min = arr[0]
        for ele in arr:
            if ele < min:
                min = ele

        return min


if __name__ == "__main__":
    # Driver code.
    ls = LinearSearch()
    arr = [5, 3, 2, 1, 4, 2, 3, 4, 6, 3, 2]
    res = ls.linear_search_min(arr)
    print("Min element found: ", res)
