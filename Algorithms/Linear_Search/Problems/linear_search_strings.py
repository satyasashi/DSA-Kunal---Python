class LinearSearch:
    """Search for a character in a string"""

    def linear_search(self, a_string, target):
        # Base case: If string is empty, return None
        if len(a_string) == 0:
            return None

        for c in a_string:
            if c == target:
                return True

        # If nothing is found
        return None


if __name__ == "__main__":
    # Driver code.
    ls = LinearSearch()
    a_string = "Elon Musk"
    target = "M"
    result = ls.linear_search(a_string, target)

    if result:
        print("Target Found: ", result)
    else:
        print("Target not found.")
