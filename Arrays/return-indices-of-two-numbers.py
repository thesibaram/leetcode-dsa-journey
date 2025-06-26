#Problem
class Solution():
    
    """
    Problem: Given an array of integers,
    return indices of two numbers that add up to a target.

    Input: [2,7,11,15], target = 9
    Output: [0,1]
    """

    def indices(self, arr, target=9):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] == target:
                    return [i, j]


s = Solution()
print(s.indices([2,7,11,15], 9))

