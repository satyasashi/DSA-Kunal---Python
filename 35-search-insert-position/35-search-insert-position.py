class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Base case: arr is empty
        if len(nums) == 0:
            return None

        start = 0
        end = len(nums) - 1

        while start <= end:
            # (start + end) // 2 at some point when we do
            # (start + end) might exceed integer limit.
            # Doing start + (end - start) // 2 is optmized way.
            mid = start + (end - start) // 2
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            elif target == nums[mid]:
                return mid

        return end + 1

if __name__ == "__main__":
    # Driver code.
    bs = Solution()
    arr = [1, 4, 6, 7, 8, 9]
    res = bs.searchInsert(arr, 7)
    if res is not None or res == 0:
        print("Element found at index: ", res)
    else:
        print("Element not found.")