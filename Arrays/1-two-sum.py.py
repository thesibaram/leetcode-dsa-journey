#LeetcodeQ
class Solution(object):
    def twoSum(self, arr, target):

        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        """
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target:
                    return [i, j]


nums = [2,7,11,15]
target = 9

s = Solution()
print(s.twoSum(nums, 9))


