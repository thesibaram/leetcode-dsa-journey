# """🌿 Problem 1: Add Two Numbers"""

# while True:
#     n = input("Enter two numbers (separated by a space): ")
#     numbers = n.split()
#     if len(numbers) == 2:
#         try:
#             num1, num2 = int(numbers[0]), int(numbers[1])
#             print(num1 + num2)
#             break
#         except ValueError:
#             print("Please enter valid numbers.")
#     else:
#         print("Invalid. Please enter exactly two numbers.")

#LeetcodeQ
# nums = [2,7,11,15]
# target = 9

# for n in range(len(nums)):
#     for m in range(n+1, len(nums)):
#         if nums[n] + nums[m] == target:
#             print(nums[n], nums[m])

#LeetcodeQ
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            print("Invalid Input.")
        s = list(set(nums))
        k = 0
        for ele in s:
            if ele in nums:
                k += 1
                s.append("_")
        print(k, s)

s = Solution()
n = [1,1,2]
s.removeDuplicates(n)



