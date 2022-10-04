class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        indices = [-1, -1]
        start = self.find_first_last_position(arr, target, True)
        end = self.find_first_last_position(arr, target, False)

        indices = [start, end]
        return indices
    
    def find_first_last_position(self, arr, target, find_starting_val):
        # arr = [5, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 10]
        #        0  1  2  3  4  5  6  7  8  9  10 11 12 13
        ans = -1
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2

            # Reduce the search space by adjusting the
            # pointers.
            if target < arr[mid]:
                end = mid - 1
            elif target > arr[mid]:
                start = mid + 1
            else:
                # When found a potential element position,
                # store it and update later if necessary.
                ans = mid

                # If we found it, there might be chances we
                # want to search either left side or right side.
                if find_starting_val:
                    end = mid - 1
                else:
                    start = mid + 1
        return ans

if __name__ == "__main__":
    first_last_element_position = Solution()
    arr = [5, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 10]
    target = 10
    res = first_last_element_position.searchRange(arr, target)
    print("Final result: ", res)