from math import log10


# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
class FindNumbersLinearSearch:
    """
    Find the # of digits in a given number and
    print # of digits that are EVEN in count of its digits.
    """

    def digits_count(self, num):
        if num < 0:
            num = num * -1

        if num == 0:
            return 1

        count = 0
        while num > 0:
            count += 1
            num = num // 10

        return count

    def digits_count_2(self, num):
        # Formula for counting # of digits in a number.
        return int(log10(num)) + 1

    def even_or_odd(self, num):
        num_of_digits = self.digits_count_2(num)

        if num_of_digits % 2 == 0:
            return True
        else:
            return False

    def find_numbers(self, arr):
        # Base case: if array is empty, return None
        if len(arr) == 0:
            return None

        even_count = 0

        for n in arr:
            result = self.even_or_odd(n)
            if result:
                even_count += 1

        return even_count


if __name__ == "__main__":
    # Driver code
    find_even_count = FindNumbersLinearSearch()
    arr = [12, 345, 2, 6, 789]
    res = find_even_count.find_numbers(arr)
    print(res)
