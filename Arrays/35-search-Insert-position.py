#LeetcodeQ
class Solution(object):
    def searchInsert(self, nums, target):

        """
        Given a sorted array of distinct integers and a target value,
        return the index if the target is found. If not,
        return the index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.

        Input: nums = [1,3,5,6], target = 5
        Output: 2

        Input: nums = [1,3,5,6], target = 2
        Output: 1
        """

        for indx in range(len(nums)):
            if nums[indx] >= target:
                return indx
        return len(nums)

s = Solution()
# print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
# print(s.searchInsert([1,3,5,6], 4))
