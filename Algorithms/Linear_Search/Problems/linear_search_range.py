class LinearSearch:
    """Search for a character in a string"""

    def linear_search(self, start, end, a_string, target):
        # Base case: If string is empty, return None
        if len(a_string) == 0:
            return None

        for c in list(a_string)[start:end]:
            if c == target:
                return True

        # If nothing is found
        return None


if __name__ == "__main__":
    # Driver code.
    ls = LinearSearch()
    a_string = "Elon Musk"
    target = "M"
    start = 2
    end = 7
    result = ls.linear_search(start, end, a_string, target)

    if result:
        print("Target Found: ", result)
    else:
        print("Target not found.")
