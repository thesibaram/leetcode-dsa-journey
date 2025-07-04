#LeetCodeQ
class Solution(object):
    def plusOne(self, digits):

        """
        You are given a large integer represented as an integer array digits,
        where each digits[i] is the ith digit of the integer.
        The digits are ordered from most significant to least significant in left-to-right order.
        The large integer does not contain any leading 0's.

        Increment the large integer by one and return the resulting array of digits.

        Input: digits = [1,2,3]
        Output: [1,2,4]
        Explanation: The array represents the integer 123.
        Incrementing by one gives 123 + 1 = 124.
        Thus, the result should be [1,2,4].
        """

        a = int("".join(str(i)for i in digits)) + 1
        b = [int(ele)for ele in str(a)]
        return b

s = Solution()
print(s.plusOne([9]))
