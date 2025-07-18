#LeetcodeQ
class Solution():
        def removeElement(self, nums, val):
            """
            Given an integer array nums and an integer val,
            remove all occurrences of val in nums in-place.
            The order of the elements may be changed.
            Then return the number of elements in nums which are not equal to val.

            Consider the number of elements in nums which are notequal to val be k,
            to get accepted,you need to do the following things:

            Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
            Return k.

            Input: nums = [3,2,2,3], val = 3
            Output: 2, nums = [2,2,_,_]
            Explanation: Your function should return k = 2, with the first two elements of nums being 2.
            It does not matter what you leave beyond the returned k (hence they are underscores).
            """

            k = 0
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[k] = nums[i]
                    k += 1
            return k


s = Solution()
print(s.removeElement([3,2,2,3], 3))
# print(s.removeElement([0,1,2,2,3,0,4,2], 2))

