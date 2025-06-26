class Solution(object):
    def isPalindrome(self, s):

        s = "".join(s.lower().split())
        for ele in s:
            if not ele.isalnum():
                s = s.replace(ele, "")
        if str(s) == str(s[::-1]):
            return True
        else:
            return False


a = Solution()
print(a.isPalindrome("race a car"))
