from operator import indexOf


class LinearSearch:
    """Search for an element in a given array
    and return the Index or Boolean if the element
    was found. Else return -1"""

    def linear_search(self, arr, target):
        # Base case: if array is empty, return -1
        if len(arr) == 0:
            return None

        # Loop through and find the target.
        for num in arr:
            if num == target:
                return arr.index(num)

        # If target not found in the array
        return None


if __name__ == "__main__":
    # Driver code.
    ls = LinearSearch()
    arr = [4, 2, 1, 6, 3, 9, 10]
    target = 6
    result = ls.linear_search(arr, target)
    if result:
        print("Element found at: ", result)
    else:
        print("Element Not Found.")
