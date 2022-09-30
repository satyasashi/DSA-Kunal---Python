from typing import List


# https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for person in accounts:
            # individual person's bank balance (row sum)
            person_balance_total = 0
            for bank_balance in person:
                person_balance_total += bank_balance

            # Capture the max bank balance (row sum)
            if person_balance_total > max_wealth:
                max_wealth = person_balance_total
        return max_wealth


if __name__ == "__main__":
    # Driver code
    sol = Solution()
    accounts = [[1, 2, 3], [3, 2, 1]]
    max_wealth = sol.maximumWealth(accounts)
    print("Max wealth of person is: ", max_wealth)
